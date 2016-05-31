import re
import sqlite3
from collections import Counter
from string import punctuation
from math import sqrt

# initialize the connection to the database
connection = sqlite3.connect('chatbot.sqlite')
cursor = connection.cursor()

# lage tabbelen vi trenger for programmet
try:
    # lager en tabell som inneholder ordene
    cursor.execute('''
        CREATE TABLE words (
            word TEXT UNIQUE
        )
    ''')
    # lager en tabell som inneholder setnignene
    cursor.execute('''
        CREATE TABLE sentences (
            sentence TEXT UNIQUE,
            used INT NOT NULL DEFAULT 0
        )''')
    # create association between weighted words and the next sentence
    #
    cursor.execute('''
        CREATE TABLE associations (
            word_id INT NOT NULL,
            sentence_id INT NOT NULL,
            weight REAL NOT NULL)
    ''')
except:
    pass

def get_id(entityName, text):
    """Retrieve an entity's unique ID from the database, given its associated text.
    If the row is not already present, it is inserted.
    The entity can either be a sentence or a word."""
    # Retunerer en unik ID fra databasen. Retunerer en setning eller et ord.
    tableName = entityName + 's'
    columnName = entityName
    cursor.execute('SELECT rowid FROM ' + tableName + ' WHERE ' + columnName + ' = ?', (text,))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        cursor.execute('INSERT INTO ' + tableName + ' (' + columnName + ') VALUES (?)', (text,))
        return cursor.lastrowid

def get_words(text):
    """Retrieve the words present in a given string of text.
    The return value is a list of tuples where the first member is a lowercase word,
    and the second member the number of time it is present in the text."""
    # Retunerer ordene som er i
    wordsRegexpString = '(?:\w+|[' + re.escape(punctuation) + ']+)'
    wordsRegexp = re.compile(wordsRegexpString)
    wordsList = wordsRegexp.findall(text.lower())
    return Counter(wordsList).items()


B = 'Hello!'
while True:
    # output bot's melding.
    print('B: ' + B)
    # Spør bruker om input, hvis blank, quit loopen.
    H = raw_input('H: ').strip()
    if H == '':
        break
    # lagrer koblingen mellom bot's meldinger og ordene kundes respons
    words = get_words(B)
    words_length = sum([n * len(word) for word, n in words])
    sentence_id = get_id('sentence', H)
    for word, n in words:
        word_id = get_id('word', word)
        weight = sqrt(n / float(words_length))
        cursor.execute('INSERT INTO associations VALUES (?, ?, ?)', (word_id, sentence_id, weight))
    connection.commit()
    # Retunerer den mest sannsynlig svaret fra databasen.
    cursor.execute('CREATE TEMPORARY TABLE results(sentence_id INT, sentence TEXT, weight REAL)')
    words = get_words(H)
    words_length = sum([n * len(word) for word, n in words])
    for word, n in words:
        weight = sqrt(n / float(words_length))
        cursor.execute('INSERT INTO results SELECT associations.sentence_id, sentences.sentence, ?*associations.weight/(4+sentences.used) FROM words INNER JOIN associations ON associations.word_id=words.rowid INNER JOIN sentences ON sentences.rowid=associations.sentence_id WHERE words.word=?', (weight, word,))
    # hvis den fant en match, gis det beste svaret.
    cursor.execute('SELECT sentence_id, sentence, SUM(weight) AS sum_weight FROM results GROUP BY sentence_id ORDER BY sum_weight DESC LIMIT 1')
    row = cursor.fetchone()
    cursor.execute('DROP TABLE results')
    # hvis ikke, så ramdomly velg en av de minst brukte setningene.
    if row is None:
        cursor.execute('SELECT rowid, sentence FROM sentences WHERE used = (SELECT MIN(used) FROM sentences) ORDER BY RANDOM() LIMIT 1')
        row = cursor.fetchone()
    # sier til databasen at setningen har blitt brukt engang til. 
    B = row[1]
    cursor.execute('UPDATE sentences SET used=used+1 WHERE rowid=?', (row[0],))

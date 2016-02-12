# -*- coding: utf-8 -*-
# Gruppe: Team Timeplan
# Yngve Olsen Ranestad
# Steffen Sande
# Even Nilsen
# Øistein Fongaard
# Håkon Gilje

import random
'''numhands = 4
for c in range(1, numhands):
	c = [r+s for r in '2345789TJQKA' for s in 'SHDC']

for x in range(1, numhands):
	random.shuffle(x)
'''

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, numdecks=1, deck=mydeck):
    random.shuffle(deck)
    for s in range(numdecks - 1):
        deck = deck + mydeck
    #hands = []
    #for s in range(1, numhands):
        #for r in range(1, 5):
            #hands[s] = hands[s] + deck.pop()
            #hands[r].append(deck.pop())
    return [deck[n*i:n*(i+1)] for i in range(numhands)]
    #return [[deck.pop() for n in range(n)] for h in range(numhands)]
    #return hands
pranks = ["high card", "Pair", "Two Pair", "Three of a kind", "Straight", \
          "Flush", "Full house", "Four of a kind", "Straight flush"]

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    #print "The winning hand had: " + \
        #pranks[hand_rank(allmax(hands,key=hand_rank))[0]]
    #print hand_rank(allmax(hands,key=hand_rank))
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    result, maxcal = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    if len(result) == 1:
        result = result[0]
    return result

#def allmax(iterable, key=None):
#	iterable.sort(key=key,reverse=True)
#	result = [iterable[0]]
#	maxValue = key(iterable[0]) if key else iterable[0]
#	for value in iterable[1:]:
#		v = key(value) if key else value
#		if v == maxValue: result.append(value)
#		else: break
#	return result

#def allmax(iterable, key=None):
#	best_hands = []
#	max_hand = max(iterable, key=hand_rank)
#	for hand in iterable:
#		if hand_rank(hand) == hand_rank(max_hand):
#			best_hands.append(hand)
#	return best_hands
#/	ismax = max(iterable, key=hand_rank)
#/	return ismax


def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

#def flush(hand):
#	"Return True if all the cards have the same suit."
#	suits = [s for r,s in hand]
#	return len(set(suits)) == 1

def flush(hand):
    checkflush = [s for r, s in hand]
    return checkflush.count(checkflush[1]) == 5

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has exactly n-of-a-kind of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

#def two_pair(ranks):
#    "If there are two pair here, return the two ranks of the two pairs, else None."
#    pair = kind(2, ranks)
#    lowpair = kind(2, list(reversed(ranks)))
#    if pair and lowpair != pair:
#        return (pair, lowpair)
#    else:
#        return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    pairlist = ()
    for r in ranks:
        if ranks.count(r) == 2: pairlist = pairlist +(r, )
    set(pairlist)
    pairlist = tuple(set(pairlist))
    if len(pairlist) == 2:
        return pairlist
    else:
        return None

def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
    sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    fl = "AH KH JH 6H TH".split() # Flush
    st = "AH KC QD JD TS".split() # Straight
    tk = "2H 2C 2D AC TD".split() # Three of kind
    tp = "TD 9H TH 7C 9S".split() # Two Pair
    op = "TD TC AD KD QD".split() # One Pair
    hq = "2D 3D 4C 5H 7H".split() # High card
    al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
    tp1 = "7H 7D 9C 3C 9S".split() #Two Pair
    sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    op1 = "KH 7C 5S KS 2S".split() # One pair
    tp2 = "TH 3S 2H 3D TC".split() # Two pair
    tk1 = "TH JD JH 8C JC".split() # Three of kind
    hq1 = "TH 9D 5C 3H 2C".split() # High card
    fk3 = "TC TS TH 2C TD".split() # Four of a Kind
    f3 = "2C 4C 6C 7C TC".split() # Flush
    s3 = "3C 4D 5H 6D 7H".split() # Straight
    assert poker([fk3, f3, s3]) == fk3 #gilje start
    assert poker([sf, 20*fk]) == sf
    assert poker([fk3, 5*f3]) == fk3
    assert card_ranks(fk3) == [10, 10, 10, 10, 2]
    assert card_ranks(f3) == [10, 7, 6, 4, 2]
    assert hand_rank(fk3) == (7, 10, 2)
    assert hand_rank(f3) == (5, [10, 7, 6, 4, 2])
    assert flush(f3) == True
    assert straight(card_ranks(s3)) == True
    assert straight(card_ranks(f3)) == False #gilje slutt
    assert poker([fh, tk, hq]) == fh #oistein start
    assert poker([fl, sf1, tk]) == sf1
    assert poker([op, al, fh]) == fh
    assert poker([st, fk, tp]) == fk
    assert poker([tk, tp, op]) == tk
    assert poker([hq, op, hq]) == op
    assert card_ranks(op1) == [13, 13, 7, 5, 2]
    assert card_ranks(tp2) == [10, 10, 3, 3, 2]
    assert card_ranks(tk1) == [11, 11, 11, 10, 8]
    assert card_ranks(hq1) == [10, 9, 5, 3, 2] #oistein slutt
    assert poker([tk, op, al]) == al #hakon dale start
    assert poker([tp, tp1]) == tp
    assert hand_rank(tp1) == (2, (9, 7), [9, 9, 7, 7, 3])
    assert hand_rank(hq) == (0, [7, 5, 4, 3, 2])
    assert hand_rank(st) == (4, 14)
    assert card_ranks(op) ==[14, 13, 12, 10, 10]
    assert card_ranks(tp1) == [9, 9, 7, 7, 3]
    assert kind(3, tpranks) == None
    assert kind(2, tpranks) == 10, 9
    assert kind(1, tpranks) == 7 #hakon dale slutt
    assert poker([hq, tp, op]) == tp#steffen start
    assert poker([al, st]) == st
    assert poker([al, st, fl]) == fl
    assert card_ranks(hq) == [7, 5, 4, 3, 2]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]#steffen slutt
    assert poker([sf2, tk, al]) == sf2#arild start
    assert poker([hq, st]) == st
    assert poker([al, st, fk]) == fk
    assert flush(fl) == True
    assert straight(card_ranks(tp)) == False
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(hq) == [7, 5, 4, 3, 2]
    assert hand_rank(tk) == (3, 2, [14, 10, 2, 2, 2])
    assert hand_rank(st) == (4, 14)
    assert kind(5, tpranks) == None#arild slutt
    assert poker([tp, op]) == tp #Even start
    assert poker([hq, tk]) == tk
    assert poker([sf1] + 50*[fl]) == sf1
    assert card_ranks(sf1) == [10, 9, 8, 7, 6]
    assert card_ranks(tk) == [14, 10, 2, 2, 2]
    assert card_ranks(st) == [14, 13, 12, 11, 10]
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, tpranks) == 10
    assert kind(1, fkranks) == 7 #Even slutt
    assert poker([sf1, fk, fh]) == sf1
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == [fh, fh]
    assert poker([sf1]) == sf1
    assert poker([sf1] + 99*[fh]) == sf1
    assert hand_rank(sf1) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert straight(card_ranks(al)) == True
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    return 'You did good, and you should feel good about yourself :)'

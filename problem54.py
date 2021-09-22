
"""
FUUUUUUUUUUUUUUUU

like literally 4 hours later

That was not a math problem
-----

this code is extremely brittle,
I just kept running it till it gave me the right answer once

this is not the right way to write code

but, uhg, fuck
"""


test_line = "8C TS KC 9H 4S 7D 2S 5D 3S AC"
hand1 = test_line.split()[:5]
hand2 = test_line.split()[5:]

#test straight flush
test_line = "3C 4C 5C 6C 7C 3D 4D 5D 6D 7D"
hand1 = test_line.split()[:5]
hand2 = test_line.split()[5:]
#find_winner(hand1, hand2)

# test 4 of a kind
test_line = "2i 2g 27 2b 4f 2a 2b 2c 2d 5e"
hand1 = test_line.split()[:5]
hand2 = test_line.split()[5:]
#find_winner(hand1, hand2)




def test_for_flush(hand):
    # NOTE hand is still in orignal string form
    suit = hand[0][1]
    for card in hand:
        if card[1] != suit:
            return False
    return True

def hand_to_list(hand):
    d = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T" : 10, "J":11, "Q":12, "K":13, "A":14}
    l = []
    for card in hand:
        l.append( d[card[0]])
    l.sort()
    l = [a - 2 for a in l]
    a = [0]*13
    for card in l:
        a[card] +=1
    a.reverse()
    return a


def test_for_straight(hand):
    if hand.count(1) != 5:
        return False
    # lists are perhaps not the way to do this....
    
    # this would be wrap-around straights, but let's say no
    #hand.append(hand[0])
    hand.append(0)
    
    count = 0
    for i in range(len(hand)-1):
        if hand[i] == 1 and hand[i+1] == 0:
            count +=1
    if count > 1:
        return False
    return True
    


def find_winner(hand1, hand2):
    h1_f = test_for_flush(hand1)
    h2_f = test_for_flush(hand2)
    
    h1 = hand_to_list(hand1)
    h2 = hand_to_list(hand2)
    
    h1_s = test_for_straight(h1)
    h2_s = test_for_straight(h2)
    
    compare = [ a - b for (a,b) in zip(h1, h2)]
    if not(h1_f or h2_f) and (compare == [0]*13):
        # This is just a tie, but we were told that doesn't happen
        raise Exception
    
    # straight flush
    h1_sf = h1_s and h1_f
    h2_sf = h2_s and h2_f
    
    if h1_sf and not h2_sf:
        print("sf 1")
        return 1
    if h2_sf and not h1_sf:
        print("sf 1")
        return 2
    if h1_sf and h2_sf:
        print("both sf")
        diff = hi.index(1) - h2.index(1)
        if diff > 0:
            return 1
        if diff < 0:
            return 2
        raise Exception
    
    
    # 4 of a kind
    h1_4 = h1.count(4) == 1
    h2_4 = h2.count(4) == 1
    
    if h1_4 and not h2_4:
        print("four 1")
        return 1
    if h2_4 and not h1_4:
        print("four 2")
        return 2
    if h1_4 and h2_4:
        print("both four")
        diff = h1.index(4) - h2.index(4)
        if diff > 0:
            return 1
        if diff < 0:
            return 2
        diff = h1.index(1) - h2.index(1)
        if diff > 0:
            return 1
        if diff < 0:
            return 2
        raise Exception
    
    
    # full house
    h1_fh = h1.count(3) == 1 and h1.count(2) == 1
    h2_fh = h2.count(3) == 1 and h2.count(2) == 1
    
    # okay I think this is a much better way to do this
    if h1_fh and not h2_fh:
        print("full house 1")
        return 1
    if h2_fh and not h1_fh:
        print("full house 2")
        return 2
    if h1_fh and h2_fh:
        print("both full house")
        h1_3 = h1.index(3)
        h2_3 = h2.index(3)
        if h1_3 < h2_3:
            return 1
        if h2_3 < h1_3:
            return 2
        # with only 52 cards the bellow should never happen
        raise Exception
        if h1_3 == h2_3:
            h1_1 = h1.index(2)
            h2_2 = h2.index(2)
            if h1_2 < h2_2:
                return 1
            if h2_2 < h1_2:
                return 2
            if h1_2 == h2_2:
                raise Exception
    
    # flush
    if h1_f and not h2_f:
        print("flush 1")
        return 1
    if h2_f and not h1_f:
        print("flush 2")
        return 2
    if h1_f and h2_f:
        print("both flush")
        # high card
        # no pairs or greater possible in 52 card deck
        for c in compare:
            if c > 0:
                return 1
            if c < 0:
                return 2
        raise Exception
    
    #straight
    if h1_s and not h2_s:
        print("straight 1")
        return 1
    if h2_s and not h1_s:
        print("straight 2")
        return 2
    if h1_s and h2_s:
        print("both straights")
        for c in compare:
            if c > 0:
                return 1
            if c < 0:
                return 2
        raise Exception
    
    # 3 of a kind
    h1_3 = h1.count(3) == 1
    h2_3 = h2.count(3) == 1
    
    if h1_3 and not h2_3:
        print("three 1")
        return 1
    if h2_3 and not h1_3:
        print("three 2")
        return 2
    if h1_3 and h2_3:
        print("both 3")
        # high 3
        hi_3 = h1.index(3) - h2.index(3)
        if hi_3 < 0:
            return 1
        if hi_3 > 0:
            return 2
        # high card
        for c in compare:
            if c == 1:
                return 1
            if c == -1:
                return 2
        raise Exception    
    
    # two pairs
    h1_2 = h1.count(2) == 2
    h2_2 = h2.count(2) == 2
    if h1_2 and not h2_2:
        print("two pair 1")
        return 1
    if h2_2 and not h1_2:
        print("two pair 2")
        return 2
    if h1_2 and h2_2:
        print("both two pairs")
        # first high pair
        hi_2 = h1.index(2) - h2.index(2)
        if hi_2 < 0:
            return 1
        if hi_2 > 0:
            return 2
        # 2nd high pair
        first_2_index = h1.index(2)
        h1.pop(first_2_index)
        h2.pop(first_2_index)
        hi_2 = h1.index(2) - h2.index(2)
        if hi_2 < 0:
            return 1
        if hi_2 > 0:
            return 2
        # high card
        for c in compare:
            if c == 1:
                return 1
            if c == -1:
                return 2
        raise Exception
    
    # pair
    h1_2 = h1.count(2)
    h2_2 = h2.count(2)
    if h1_2 and not h2_2:
        print("pair 1")
        return 1
    if h2_2 and not h1_2:
        print("pair 2")
        return 2
    if h1_2 and h2_2:
        print("both pairs")
        # high pair
        hi_2 = h1.index(2) - h2.index(2)
        if hi_2 < 0:
            return 1
        if hi_2 > 0:
            return 2
        # high card
        for c in compare:
            if c == 1:
                return 1
            if c == -1:
                return 2
        raise Exception
    
    # high card
    for c in compare:
        if c > 0:
            print("high card 1")
            return 1
        if c < 0:
            print("high card 2")
            return 2
    raise Exception
     
    
    return 'still working here'

wins = 0
ls = 0
with open("p054_poker.txt") as file:
    for round in file:
        hand1 = round.split()[:5]
        hand2 = round.split()[5:]
        
        r = find_winner(hand1, hand2)
        if r == 1:
            wins += 1
        else:
            ls +=1

print( wins)



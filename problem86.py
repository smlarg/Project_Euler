"""
2.75s

I don't want to talk about how long I spent on this. basically whole day
(I guess I talked about it)
I probably drank too much last night
first a number of hours solving the shortest path with calculus, before I drew the two sides next to each other....
then it was mostly tripping up on the combinatorics
"""


from fractions import Fraction

def count_unique_decompositions(a,b):
    a, b = max(a,b), min(a,b)
    return (b//2 + max(b-(a-1)//2, 0) )
    # I kept fucking up the second term, and only got that from trial and error

def count_unique_decompositions_n_hack(a,b,n):
    a, b = max(a,b), min(a,b)
    if a > n: return( max(b-(a-1)//2, 0))
    return (b//2 + max(b-(a-1)//2, 0) )

def add_to_pairs(M):
    for m in range(1,int(4*M**.5)):
        for n in range(1,m):
            if Fraction(m,n).numerator != m : continue
            if (m*n)%2 : continue
            a = m**2 - n**2
            b = 2*m*n
            a,b = max(a,b), min(a,b)
            A = a
            B = b
            while( A < 2*M+1 and B < M+1):
                pairs.append([A,B])
                A += a
                B += b


def find_pairs_and_add_their_count(M):
    count = 0
    for pair in pairs:
        if pair[0] <= 2*M and pair[1] <= M:
            count += count_unique_decompositions_n_hack(pair[0],pair[1],M)
    return count

guess = 2
pairs = []
add_to_pairs(guess)

c = 0
M = 0
while c < 1000000:
    M+=1
    if M > guess:
        guess *=2
        pairs = []
        add_to_pairs(guess)
    c = find_pairs_and_add_their_count(M)

print(M)


primativeTrips100 = [
[3, 4, 5], [5, 12, 13], [8, 15, 17], [7, 24, 25],
[20, 21, 29], [12, 35, 37], [9, 40, 41], [28, 45, 53],
[11, 60, 61], [16, 63, 65], [33, 56, 65], [48, 55, 73],
[13, 84, 85], [36, 77, 85], [39, 80, 89], [65, 72, 97] ]

primativeTrips100_to_300 = [
[20, 99, 101], [60, 91, 109], [15, 112, 113], [44, 117, 125],
[88, 105, 137], [17, 144, 145], [24, 143, 145], [51, 140, 149],
[85, 132, 157], [119, 120, 169], [52, 165, 173], [19, 180, 181],
[57, 176, 185], [104, 153, 185], [95, 168, 193], [28, 195, 197],
[84, 187, 205], [133, 156, 205], [21, 220, 221], [140, 171, 221],
[60, 221, 229], [105, 208, 233], [120, 209, 241], [32, 255, 257],
[23, 264, 265], [96, 247, 265], [69, 260, 269], [115, 252, 277],
[160, 231, 281], [161, 240, 289], [68, 285, 293] ]


"""
This actually isn't that much worse than the above, oddly

7.5s
"""


"""
goddammit

Oh, no one side can exceed 100, not the total of all sides.

mrr,
"""
"""
from fractions import Fraction

def count_unique_decompositions(a,b):
    a, b = max(a,b), min(a,b)
    return (b//2 + max(b-(a-1)//2, 0) )
    # I kept fucking up the second term, and only got that from trial and error

def count_unique_decompositions_n_hack(a,b,n):
    a, b = max(a,b), min(a,b)
    if a > n: return( max(b-(a-1)//2, 0))
    return (b//2 + max(b-(a-1)//2, 0) )


def count_up_to_M(M):
    limit = int(2*M**.5)
    big_sum = 0
    for m in range(1,limit):
        for n in range(1,m):
            if Fraction(m,n).numerator != m : continue
            if (m*n)%2 : continue
            a = m**2 - n**2
            b = 2*m*n
            a,b = max(a,b), min(a,b)
            A = a
            B = b
            little_sum = 0
            while( A< 2*M+1 and B < M+1):
                #print(A, B)
                little_sum += count_unique_decompositions_n_hack(A,B,M)
                A += a
                B += b
            big_sum += little_sum
    return big_sum


c = 0
M = 0
while c < 1000000:
    M +=1
    c = count_up_to_M(M)

print( M )
"""
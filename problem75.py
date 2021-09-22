"""
1.63s

I kept having bugs and submitting answers till one was right, so, I feel like I wasn't thinking clearly on this one
"""

"""
https://en.wikipedia.org/wiki/Pythagorean_triple
"""

from math import sqrt
from fractions import Fraction

L = 1500000

anArray = [0]*L
limit = int(sqrt(L))
for m in range(1,limit):
    for n in range(1,m):
        if Fraction(m,n).numerator != m : continue
        if (m*n)%2 : continue # if both are odd it's not a primative, even if co-prime?
                              # yes that is correct, hmm, why?
                              # ah, because a,b will not be co-prime then, but if even and odd they will?
                              # yes, if they're both odd, a and b will both be even.
        a = m**2 - n**2
        b = 2*m*n
        #if Fraction(a,b).numerator != a : continue
        # not necessary with (m*n)%2 test above
        c = int(sqrt(a**2 + b**2))
        d = a + b + c 
        if d > L: break
        for p in range(1,L):
            e = d*p
            if e > L: break
            anArray[e-1] += 1


print(anArray.count(1))
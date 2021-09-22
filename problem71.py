"""
3.42s

and actually this code is overkill, you only need the search the first 7 numbers below 1000000

This is the Farey sequence, fyi
https://en.wikipedia.org/wiki/Farey_sequence
"""

from fractions import Fraction

x = Fraction(0,1)
for i in range(1,1000000):
    num = int( (3/7) / (1/i))
    F = Fraction(num,i)
    if F == Fraction(3,7): continue
    x = max(x,F)


print( x.numerator )

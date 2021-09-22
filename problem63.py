"""
this takes 36ms, so that's probably a lower bound on running python at all

"""

from math import ceil

s = 0
for i in range(1,30):
    l , u = ceil((10**(i-1))**(1/i)), (10**(i))**(1/i)
    s += 10-l

print( s )

"""
1m4s, so could use work


memoizing intermediate values in a hash table (i.e. search O(1) structure) would be the most obvious (to me) next step
oh, actually, just lengths of full chains of already checked numbers might be helpful itself
yeah, you get into lower numbers very often I see just fucking around a bit
"""


from math import factorial

f = [factorial(0), factorial(1), factorial(2), factorial(3), factorial(4), factorial(5), factorial(6), factorial(7), factorial(8), factorial(9)]
# this saves about 4 seconds, so, okay

def do_this_thing(n):
    a = 0
    for b in str(n):
        a+=f[int(b)]
    return a


def count_for_this_guy(n):
    so_far = []
    while n not in so_far:
        so_far.append(n)
        n = do_this_thing(n)
    return len(so_far)


c = 0
for i in range(1000000):
    if count_for_this_guy(i) == 60:
        c += 1

print(c)
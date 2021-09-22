"""
35ms, so

would have been possible to calculate them all, but this guess was correct, so
Ah, great, the next problem makes you do that anyway.
"""

primes = [2,3,5,7,11,13,17,23,29,31]

n = 1
for p in primes:
    n*=p
    if n > 1000000:
        n//=p
        break

print(n)

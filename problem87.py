"""
1.84s
"""

def SieveOfEratosthenes(n):
    # stolen from https://www.geeksforgeeks.org/sieve-of-eratosthenes/
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return [a for a,b in zip(range(2,n+1),prime[2:]) if b]

# squared_primes = SieveOfEratosthenes(2*int(limit**.5))
# cubed_primes = SieveOfEratosthenes(2*int(limit**(1/3)))
# quartified_primes = SieveOfEratosthenes(2*int(limit**.25))

# c = 0
# for i in squared_primes:
#     if i**2 > limit: break
#     for j in cubed_primes:
#         if i**2 + j**3 > limit: break
#         for k in quartified_primes:
#             if i**2 + j**3 + k**4 < limit:
#                 c +=1
#             else:
#                 break


limit = 5e7
primes = SieveOfEratosthenes(int(limit**.5))

c = 0
collection = []
for i in primes:
    if i**2 > limit: break
    for j in primes:
        if i**2 + j**3 > limit: break
        for k in primes:
            if i**2 + j**3 + k**4 < limit:
                c +=1
                collection.append(i**2 + j**3 + k**4)
            else:
                break


print( len(set(collection)))
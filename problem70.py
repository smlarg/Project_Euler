"""
Ignoring the prim sieve even, 71 seconds on Mandy,
so not great

the comments suggest only searching for two primes (you need at least two, and more reduces the ratio)
around sqrt(10**7)
I've added that code at the bottom, takes about 2.2s
"""

primes = [2]
max_to_check = 10**7

for i in range(primes[-1], max_to_check):
    j = 0
    p = 0
    is_prime = True
    while p*p < i:
        p = primes[j]
        j += 1
        if not(i%p):
            is_prime = False
            p = i
    if is_prime:
        primes.append(i)

num_primes = len(primes)
max_prime = primes[-1]
primeset = set(primes)

# actually, there's no need to pre-do this. Hmm.


# factor_vectors = [[-1], [-1]]
# for n in range(2,11):
#     prime_factor = []
#     if n in primeset:
#         prime_factor += [0]*primes.index(n)
#         prime_factor += [1]
#         factor_vectors.append(prime_factor)
#         continue
#     i = 0
#     while n > 1:
#         p = primes[i]
#         count = 0
#         while not (n%p):
#             count += 1
#             n //= p
#         prime_factor.append(count)
#         i+=1
#     factor_vectors.append(prime_factor)

# def find_factor_vector(n):
#     prime_factor = []
#     if n in primeset:
#         prime_factor += [0]*primes.index(n)
#         prime_factor += [1]
#         return prime_factor
#     i = 0
#     while n > 1:
#         p = primes[i]
#         count = 0
#         while not (n%p):
#             count += 1
#             n //= p
#         prime_factor.append(count)
#         i+=1
#     return (prime_factor)


def find_factor_vector(n):
    prime_factor = []
    i = 0
    while n > 1:
        if n in primeset:
            prime_factor.append([1,n])
            return prime_factor
        p = primes[i]
        if not (n%p):
            count = 0
            while not n%p:
                count += 1
                n //= p
            prime_factor.append([count,p])
        i += 1
    return (prime_factor)

def phi_from_factors(facts):
    phi = 1
    for guy in facts:
        phi *= guy[1]**guy[0] - guy[1]**(guy[0]-1)
    return phi

from time import perf_counter

hits = []
maxy = 0
start = perf_counter()
for i in range(2,10**7):
    
    a = find_factor_vector(i)
    phi = phi_from_factors(a)
    
    a = [int(d) for d in str(i)]
    a.sort()
    b = [int(d) for d in str(phi)]
    b.sort()
    if a == b:
        #hits.append([i,phi])
        if phi/i > maxy:
            maxy = phi/i
            best = i

total = perf_counter() - start


print(best)


"""
2.2s (1.09s on mandy)

From comments in the thread
"""
"""

from math import sqrt

primes = [2]
max_to_check = int(sqrt(10**7)*4)

for i in range(primes[-1], max_to_check):
    j = 0
    p = 0
    is_prime = True
    while p*p < i:
        p = primes[j]
        j += 1
        if not(i%p):
            is_prime = False
            p = i
    if is_prime:
        primes.append(i)

num_primes = len(primes)
max_prime = primes[-1]
primeset = set(primes)

maxy = 0
for i in range(num_primes):
    for j in range(i, num_primes):
        p1 = primes[i]
        p2 = primes[j]
        n = p1 * p2
        if n > 10**7: continue
        phi = (p1 -1) * (p2 -1)
        
        a = [int(d) for d in str(n)]
        a.sort()
        b = [int(d) for d in str(phi)]
        b.sort()
        if a == b:
            if phi/n > maxy:
                maxy = phi/n
                best = n


print(best)
"""

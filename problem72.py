"""
8-9s with old sieve
5.8s with better sieve
"""

# 10**7 takes a litlle more than 1s
# 10**9 seems to hit a memory limit on neptr, it doesn't even seem to finish
# actuall seems to be between 8*10**8 and 9*10**8
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

max_to_check = 10**6
primes = SieveOfEratosthenes(max_to_check)

num_primes = len(primes)
max_prime = primes[-1]
primeset = set(primes)

def find_factor_vector(n):
    prime_factor = []
    i = 0
    while n > 1:
        if n in primeset:
            prime_factor.append([1,n])
            return prime_factor
        p = primes[i]
        if p*p > n:
            # always searching primes in ascending order
            # this appears to save no time....
            prime_factor.append([1,n])
            return prime_factor
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


x = 0
for i in range(2,1000000+1):
    x += phi_from_factors(find_factor_vector(i))

print(x)

"""
# naive sieve
primes = [2]
max_to_check = 10**6

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

"""
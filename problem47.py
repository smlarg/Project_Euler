"""
17.5s
"""

primes = [2]
max_to_check = 1000000

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


prime_set = set(primes)

def factor_count(n):
    count = 0
    if n > primes[-1]:
        raise Exception
        return -1
    if n in prime_set:
        return 1
    i = 0
    while n > 1:
        p = primes[i]
        if not(n%p):
            count += 1
            while not(n%p):
                n /= p
        i += 1
    return count

consecutive_count = 0
goal = 4
for i in range(3, primes[-1]):
    fc = factor_count(i)
    if not fc == goal:
        consecutive_count = 0
        continue
    else:
        consecutive_count += 1
    if consecutive_count == goal:
        print( i-goal+1)
        break


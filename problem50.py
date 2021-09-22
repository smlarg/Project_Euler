
"""
I'm not even going to try to justify this
I think I need a break

7 seconds
"""

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

bests = []
sums = []

bestBest = 0
bestBestSum = 0

for i in range(100):
    good = True
    best = 0
    bestSum = -1
    for j in range(3,num_primes-i):
        if not good:
            break
        sum = 0
        for k in range(j):
            sum += primes[i + k]
            if sum > max_prime:
                good = False
                break
        if sum in primeset:
            best = j
            bestSum = sum
    bests.append(best)
    sums.append(bestSum)
    
    if best > bestBest:
        bestBest = best
        bestBestSum = bestSum


print(bestBestSum)


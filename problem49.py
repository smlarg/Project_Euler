"""
855ms
"""


primes = [2]
max_to_check = 20000

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

primeset = set(primes)

def check_perm(i,j,k):
    i = set(str(i))
    j = set(str(j))
    k = set(str(k))
    if i != j:
        return False
    if i != k:
        return False
    if j != k:
        return False
    return True

for i in range(1000,10000):
    if not i in primeset:
        continue
    if i == 1487:
        continue
    for j in range(2, 10000-i):
        if i + 2*j > 10000:
            # okay I could clearly do this in the range call....
            break
        if not i + j in primeset:
            continue
        if not i + 2*j in primeset:
            continue
        if not check_perm(i, i+j, i+2*j):
            continue
        print ( str(i) + str(i+j) + str(i+2*j) )


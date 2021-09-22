"""
6.3s
"""

all_primes = [2]
max_to_check = 10**6

for i in range(all_primes[-1], max_to_check):
    j = 0
    p = 0
    is_prime = True
    while p*p < i:
        p = all_primes[j]
        j += 1
        if not(i%p):
            is_prime = False
            p = i
    if is_prime:
        all_primes.append(i)


#start with 6 digits
primes = []
for i in all_primes:
    if i >99999 and i < 1000000:
        primes.append(i)

num_primes = len(primes)
max_prime = primes[-1]
primeset = set(primes)


# assume we need a repeat...
# assume all are replaced (it will be true at some integer, since we're only hitting 8)

for p in primes:
    for i in range(10):
        if str(p).count(str(i)) > 1:
            fail_count = 0
            for j in range(10):
                new_p = int( str(p).replace(str(i),str(j)) )
                if not new_p in primeset:
                    fail_count += 1
                if fail_count > 2:
                    continue
            if fail_count <= 2:
                print(p)


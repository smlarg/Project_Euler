"""
I see. I overthought this
17 ms (ignoring making the primes list)
"""

from time import time

primes = [2]
max_to_check = 10000000

start_time = time()
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

end_time = time()

print( int(end_time - start_time) )
# 96 seconds

prime_set = set(primes)

largest_prime = primes[-1]

start_time = time()
for i in range(3,10000):
    if i > largest_prime + 2:
        print('too many', i, largest_prime)
        break
    if not(i%2):
        continue
    if i in prime_set:
        continue
    for j in range(i):
        if (j*j > i):
            print( 'oh')
            print(i)
            break
        k = i - 2*j*j
        if k in prime_set:
            #print( i, k, j)
            break

end_time = time()
print ( int( (end_time - start_time)*1000))



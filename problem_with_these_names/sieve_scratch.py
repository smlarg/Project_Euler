

# 10**7 takes a litlle more than 1s
# 10**9 seems to hit a memory limit on neptr, it doesn't even seem to finish
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

from time import perf_counter

def do_the_test(n):
    start = perf_counter()
    trash = SieveOfEratosthenes(n)
    del(trash)
    return perf_counter() - start



# how about as bitwise? need numpy I think
# this is 1.5-2 orders of magnitude slower :-(
# I also tried using uints instead of bytes, in case 64bit words matter, but there's no detectable change
def SieveOfEratosthenesNumpy(n):
    import numpy as np
    from math import ceil
    max = n
    size = int(ceil(((max+1)/8)))
    prime = np.array([255]*size, dtype = np.byte )
    mask = np.zeros(8, dtype = np.byte )
    for i in range(8):
        mask[i] = 2**i
    p = 2
    while (p * p <= max):
        p_index = p//8
        byte = prime[p//8]
        p_offset = p%8
        if np.bitwise_and(byte, mask[p_offset]):
            for i in range(p * p, max+1, p):
                i_index = i//8
                i_offset = i%8
                prime[i_index] = np.bitwise_and(prime[i_index], np.invert(mask[i_offset]))
        p += 1
    
    list_of_primes = []
    for i in range(2,max+1):
        i_index = i//8
        i_offset = i%8
        byte = prime[i_index]
        if np.bitwise_and(byte, mask[i_offset]):
            list_of_primes.append(i)
    
    return list_of_primes

from time import perf_counter

def do_the_test_numpy(n):
    start = perf_counter()
    trash = SieveOfEratosthenesNumpy(n)
    del(trash)
    return perf_counter() - start

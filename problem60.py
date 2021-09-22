"""
18.4s

This is the wrong order to do the search in, as it has a set limit
it should...um, I'm not sure, which is why I did it this way
but somehow all the loops should go up in tadem, not waiting for each inner loop

the primeset should dynamically increase too, though in this case this small number was sufficient
"""


primes = [2]
max_to_check = 10**4

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

from random import randrange

def miller_rabin(p, k):
    # test p prime a total of k times
    
    if p == 2: return True
    if not(p%2): return False
    if p < 2: return False
    
    # find odd factor
    d = p - 1
    s = 0
    while not d%2:
        d //= 2
        s += 1
    
    for i in range(k):
        a = randrange(2,p)
        b = pow(a,d,p)
        if b == 1 or b == p-1:
            continue
        for j in range(s):
            b*=b
            b = pow(b,d,p)
            if b == p-1:
                # this is a janky way to do this (and I spend like 1/2 hr debugging it)
                # but, via iterative programing, it seems to work now
                j -= 1
                break
        if j == s - 1:
            return False
    
    return True


def check_concat_primality(a,b):
    sa = str(a)
    sb = str(b)
    ab = int(sa + sb)
    ba = int(sb + sa)
    if ab < max_prime:
        if not ab in primes: return False
    else:
        if not miller_rabin(ab,10): return False
    if ba < max_prime:
        if not ba in primes: return False
    else:
        if not miller_rabin(ba,10): return False
    return True

breakAll = False
for i in range(1,num_primes):
    a = primes[i]
    for j in range(i+1, num_primes):
        b = primes[j]
        if not check_concat_primality(a,b): continue
        for k in range(j+1, num_primes):
            c = primes[k]
            if not check_concat_primality(a,c): continue
            if not check_concat_primality(b,c): continue
            for l in range(k+1, num_primes):
                d = primes[l]
                if not check_concat_primality(a,d): continue
                if not check_concat_primality(b,d): continue
                if not check_concat_primality(c,d): continue
                for m in range(l+1, num_primes):
                    e = primes[m]
                    if not check_concat_primality(a,e): continue
                    if not check_concat_primality(b,e): continue
                    if not check_concat_primality(c,e): continue
                    if not check_concat_primality(d,e): continue
                    print(a, b ,c, d, e)
                    print (a + b + c + d)
                    breakAll = True
                    break
                if breakAll: break
            if breakAll: break
        if breakAll: break
    if breakAll: break


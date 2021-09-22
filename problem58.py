"""
as you can see, I had to go with a primality test
people in the comments saying they could use sieves etc, but the primes get into 9 digits so I don't know how they did that

I implemented the test "myself" in that I worked from the pseudocode on wikipedia, rather than copying from stackoverflow
so, I say that's not cheating

967ms
"""


from random import randrange

def miller_rabin(p, k):
    # test p prime a total of k times
    
    if p == 2:
        return True
    if not(p%2):
        return False
    if p < 2:
        return False
    
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

p = 1
q = 1
r = 0
k = 10
for n in range(1,100000):
    tr = p + 2*n
    tl = p + 4*n
    bl = p + 6*n
    p = p + 8*n
    q +=4
    if miller_rabin(tr,k):
        r +=1
    if miller_rabin(tl,k):
        r += 1
    if miller_rabin(bl,k):
        r += 1
    if q > 10*r:
        print( 'kaching')
        break

l = 2*n + 1

print(l)
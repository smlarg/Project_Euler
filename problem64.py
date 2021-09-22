"""
976ms

This could be improved/proved a lot more via math I think
first I don't have a proof that all periods are finite, I just assumed it from the question
 - oh wait no, I think it's trivial to show it's a bounded set of pairs of integers
and people in the comments of course have other tricks
but anyway, it works
"""


from math import gcd


def ncf(root, sub, numer):
    #      numer                 sqrt(root) + sub            sqrt(root) + sub
    #----------------- = numer * ---------------- == numer * ------------------
    # sqrt(root) - sub             root - sub**2                     d
    #
    #
    #
    #
    
    d = root - sub**2
    g = gcd(d, numer)
    if not g == numer:
        # no actually you can work it out, 
        # let a == p - c^2
        # b == c - n*a
        # p, c, n any integer
        # then you can expand and show a divides p - b**2 :
        # p - b**2  = p - (c - n*a)**2
        #           = (p - c**2) + 2*c*n*a - n**2 * a**2
        #           =    a        + 2*c*n*a - n**2 * a**2
        #           = a * ( 1 + 2*c*n - n**2 * a)
        print("that actually makes more sense")
        raise Exception
    d //=g
    numer = 'no more'
    i = int(root**.5)
    adder = 0
    while (-1*sub) < i:
        adder += 1
        sub -= d
    adder -= 1
    sub += d
    return adder, sub, d

def ncf2(root, sub, numer):
    d = root - sub**2
    d //= numer
    i = int(root**.5)
    adder = 0
    while (-1*sub) <= i:
        adder += 1
        sub -= d
    adder -= 1
    sub += d
    return adder, (root, -sub, d)

def check(n):
    if (round(n**.5))**2 == n:
        return [0]
    sigh = (int(n**.5),(n, int(n**.5), 1))
    myList = []
    while not sigh in myList:
        myList.append(sigh)
        b = sigh[1]
        sigh = ncf2(*b)
    myList.append(sigh)
    return myList


def check_up_to(n):
    #r = []
    count = 0
    for i in range(1,n+1):
        t = check(i)
        #if t == 0:
        #    r.append(0)
        #    continue
        r = len(t) - t.index(t[-1]) - 1
        if r%2:
            count +=1
    return count
    
print( check_up_to(10000))


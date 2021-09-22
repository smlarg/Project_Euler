"""
1.645s

Totally due to wikipedia's input though
-------
This is known as Pell's equation
https://en.wikipedia.org/wiki/Pell%27s_equation
and it looks like it's another continued fraction problem
"""
from math import sqrt

def wrong_way_to_find_minimal(n):
    if (round(sqrt(n)))**2 == n: return (-1,-1)
    m = 2
    while True:
        a = round(sqrt((m**2 -1)/n))
        if not (m**2 - n*a**2 -1):
            return m, a
        m +=1

def not_actually_much_better_way_to_find_minimal_pair(n):
    if (round(sqrt(n)))**2 == n: return (-1,-1)
    p = 2
    while True:
        a = 1 + n*p*p
        if (round(sqrt(a)))**2 == a:
            return int(round(sqrt(a))), p
        p += 1
        if not (p%1000000):
            #print(p)
            return -2,-2

#------------


def ncf(root, sub, numer):
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

from itertools import cycle
def seq_yielder(head, cyc):
    cyc = cycle(cyc)
    while head:
        yield head.pop(0)
    while True:
        yield next(cyc)

def get_seq_generator(n):
    if (round(n**.5))**2 == n: return [n]
    sigh = (int(n**.5),(n, int(n**.5), 1))
    myList = []
    while not sigh in myList:
        myList.append(sigh)
        a, b = sigh
        sigh = ncf(*b)
    cut = myList.index(sigh)
    head = [a for a,b in myList[:cut]]
    cyc = [a for a,b in myList[cut:]]
    return seq_yielder( head, cyc )

from fractions import Fraction
def cont_frac_to_degree_k_I_guess(n,k):
    a = get_seq_generator(n)
    got_to_go_backwards = []
    for i in range(k):
        got_to_go_backwards.append(next(a))
    got_to_go_backwards.reverse()
    F = Fraction(got_to_go_backwards.pop(0),1)
    for s in got_to_go_backwards:
        F = s + 1/F
    return F


def better_minimal_pair(n):
    if (round(sqrt(n)))**2 == n: return Fraction(-1,-1)
    p = 1
    while True:
        F = cont_frac_to_degree_k_I_guess(n,p)
        a = F.numerator
        b = F.denominator
        if not (a**2 - n*b**2 -1):
            return F
        p += 1

x = [0,0]
for i in range(2,1000):
    y = better_minimal_pair(i)
    x.append( y.numerator)

print( x.index(max(x)))
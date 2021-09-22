"""
kind of feels like cheating, but

93ms


oh, there was a trick, i see in the comments
b(n+1) = 1 + 1/(1+b(n)) => can get new numerator and denominator by simple additions
I don't right away see the proof gcd=1, but seems to be true
anyway
"""


from fractions import Fraction

def approx_to_root2(n):
    a = Fraction(0,1)
    for i in range(n):
        a = 2 + a
        a = 1 / a
    a += 1
    return a

# actually no need for that

count = 0
b = Fraction(0,1)
for n in range(1,1000):
    b = 2 + b
    b = 1 / b
    b = 1 + b
    nl = len(str(b.numerator))
    dl = len(str(b.denominator))
    if nl > dl:
    #if True:
        count += 1
        #print(n, b)
    b = b - 1

print( count )
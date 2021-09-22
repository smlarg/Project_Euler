"""
25.8 seconds
12.0s on mandy

people in the first few comments seem to have the exact same approach, but 4x faster (on 20 year old computers)
so I think it's the overhead of Fraction, or just Python
"""

"""
For all n in range (1,12001), find all fractions with gcd=1 in the interval (1,3) (1,2) ??

"""


"""
how to find the range?
for 2 we want nil (skipping 1/2)
for 3 we want nil (skipping 1/3)
for 4 we want nil (skipping 2/4)
for 5 we want 2/5
for 6 we want nil (skipping 2/6 and 3/6)
for 7 we want 3/7
for 8 we want 3/8
for 9 we want 4/9 (skipping 3/9)
for 10 we want 4/10 (skipping (5/10)
for 11 we we want 4/11, 5/11 ? yes, 3/11 < 3/10 < 1/3, 6/11 > 1/2

"""
for i in range(2,15):
    ll = i//3 + 1
    #if not i%3: ll +=1 No not necessary, if it's right on the line it's still cut off
    ul = i//2 + 1
    if not i%2: ul -=1
    
    get = []
    for j in range(ll,ul):
        get.append(j)
    
    #print(i, get)


from fractions import Fraction

for i in range(2,8+1):
    lower = i//3 + 1
    upper = i//2 + 1
    if not i%2: upper -= 1
    for j in range(lower, upper):
        F = Fraction(j,i)
        if F.numerator == j:
            #print(F)
            continue

count = 0
for i in range(2,12000+1):
    lower = i//3 + 1
    upper = i//2 + 1
    if not i%2: upper -= 1
    for j in range(lower, upper):
        F = Fraction(j,i)
        if F.numerator == j:
            count += 1


print( count)
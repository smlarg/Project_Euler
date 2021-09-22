"""
121ms

I feel like there's a way to avoid 10**200, by multipling and dividing in a different order
But there's pretty much no way to avoid 10**100, so who cares about 10**200 at that point?
Also - this does not take long to run
"""
"""
Uses Newton's method
https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
which usually is root = 0.5 * (x + (n / x))
but if you want to solve for superroot = root * M, then it's just
superroot/M = 0.5 *(x/M + n*M/X) => superroot = 0.5*(x + n*M**2/x)

"""



from math import sqrt


"""
n = 2
mask = 10**100 * 100
x = n * mask
int_part = int(sqrt(n))
while True:
    root = ( x + (mask**2 * n//x))//2
    if abs(root - x) < 1: break
    x = root

x //= 100
x -= int_part*mask//100
sum( [ int(s) for s in str(x)])
# not what they want!!!

n = 2
mask = 10**100
x = n * mask
int_part = int(sqrt(n))
while True:
    root = ( x + (mask**2 * n//x))//2
    if abs(root - x) < 1: break
    x = root

x //= 10**len(str(int_part))
sum( [ int(s) for s in str(x)])
"""



def get_that_sum(n):
    int_part = int(sqrt(n))
    if int_part**2 == n: return 0
    mask = 10**100  # I might want to add a saftey 10 here, then divide off later - nope, the website says it was okay
    x = n*mask
    while True:
        root = ( x + (mask**2 * n//x))//2
        if abs(root - x) < 1: break # can just be equality test
        x = root
    x //= 10**len(str(int_part)) # could also just use str(x)[:100] in the sum
    if len(str(x)) != 100: print( 'oh crap')
    return sum( [ int(s) for s in str(x)])


s = 0
for i in range(100):
    s+= get_that_sum(i)


print(s)

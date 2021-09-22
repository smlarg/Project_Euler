"""
40s

can get that down to 16s by adding this line (duh - but I didn't figure it out, it's from the comment section):
if not memo2[i]%1000000: break

Can also only store everything modulo 1000000, but that seems to have zero speed impact

and 9.94s on mandy (with fix)

someone in the comments has code which uses a dictionary instead of a list to memoize, and it's about 30% faster, which I wouldn't have guessed
(and does it with a clever decorator - I'll go ahead and steal it and paste it at the bottom
"""

"""
c.f.
https://mathworld.wolfram.com/PartitionFunctionP.html
https://en.wikipedia.org/wiki/Partition_function_(number_theory)
https://en.wikipedia.org/wiki/Pentagonal_number_theorem
https://en.wikipedia.org/wiki/Euler_function
"""



"""
#-------------
# sorry. of course no.
# this with range 10001 already takes minutes, and doesn't yet get any divisible by even 10e5

memo = []
for i in range(10001):
    memo.append([0]*10001)

for i in range(1,10001):
    for j in range(1,i+1):
        if j == 1:
            memo[i][j] = 1
            continue
        if j == i:
            memo[i][j] = memo[i][j-1] + 1
            continue
        memo[i][j] = memo[i][j-1] + memo[i-j][min(i-j,j)]



for i in range(2,10001):
    if not memo[i][i]%10000 : print (i, memo[i][i])

#-------------
"""
from time import perf_counter

start = perf_counter()
hard_wire_size = 10**5

memo2 = [0]*hard_wire_size
memo2[0] = 1

pent = lambda k : (k*(3*k-1))//2

for i in range(1,hard_wire_size):
    k = 1
    n = i - pent(k)
    while n >= 0:
        n = i - pent(k)
        t = memo2[n] * (-1)**(k%2+1)
        memo2[i] += t
        n = i - pent(-k)
        if n >= 0:
            t = memo2[n] * (-1)**(k%2+1)
            memo2[i] += t
            k +=1

end = perf_counter()
print( end - start )


for x in memo2:
    if not x%1000000:
        print( memo2.index(x))
        print( x )

# This has O( n sqrt(n)) complexity I believe, which seems pretty good, much better than I'd hoped actually
# but I get 10**5 takes 39 seconds, so 10**6 takes 39*10**1.5 ~= 40*30 = 20 minutes
# ...yeah, 15 min on mandy....

# oh shit it was only 55374, I already had it
# the next one isn't till 488324, fwiw; then 846699


"""
# stolen from the comments (from username ilan)

class Memoize:
    def __init__(self, func): 
        self.func = func
        self.cache = {}
    def __call__(self, arg):
        if arg not in self.cache: 
            self.cache[arg] = self.func(arg)
        return self.cache[arg]

@Memoize
def p(n):
    if n<0: return 0
    if n<2: return 1
    sm=0
    for k in range(1, n+1):
        n1 = n-k*(3*k-1)//2
        n2 = n-k*(3*k+1)//2
        sm += (-1)**(k%2+1) * (p(n1) + p(n2))
        if n1 <= 0:
            break
    return sm%1000000

n=0
start = perf_counter()
while p(n)!=0: n += 1

print (n)

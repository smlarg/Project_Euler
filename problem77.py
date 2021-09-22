"""
<40ms

*sigh* that shouldn't have taken so long
I'm not good at debugging recursions....
"""

class Memoize:
    def __init__(self, func): 
        self.func = func
        self.cache = {}
    def __call__(self, arg):
        if arg not in self.cache: 
            self.cache[arg] = self.func(arg)
        return self.cache[arg]

# should really implement that sieve
primes = [2]
max_to_check = 10**3
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


# this is stolen
# see problem 78
@Memoize
def express_n_using_x_or_less(a_tupple):
    # returns 0 for 1 and 1 for 0, fyi
    n, x = a_tupple
    if x == 2:
        return (n+1)%2
    if n == 0:
        return 1
    r = 0
    for p in primes:
        if p > n: break
        if p > x: break # I spent over an hour figuring out I forgot this line :-(
                        # (I literally made the name of the function a command to do this!)
        r += express_n_using_x_or_less( (n-p,min(n-p,p)) )
    return r




def express_n_using_x_or_less_db(n,x,l):
    print("n,x,l = ", n, x,l)
    if x == 2:
        if n%2:
            print ('bad')
            return 0
        else:
            print('good')
            return 1
    if n == 0:
        print ('good')
        return 1
    if n == 1:
        print('not good')
        return 0
    r = 0
    for p in primes:
        if p > n: break
        if p > x: break
        print ('p = ', p)
        r += express_n_using_x_or_less_db( n-p, min(n-p,p),l+1 )
    return r

#express_n_using_x_or_less_db(10,10,0)


x = 2
while True:
    if express_n_using_x_or_less((x,x)) > 5000 : break
    x += 1

print( x )


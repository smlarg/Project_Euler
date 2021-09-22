# I started out kind of strong, then this just got ridiculous by the end
# still takes a fraction of a second I'm afraid


#precompute the first sqrt(987654321) primes
#This is not good code, almost pseudocode, but takes 2 seconds
primes = [2]
for i in range(3,31426):
  is_prime = True
  primes_left = True
  j = 0
  while is_prime and primes_left:
   p = primes[j]
   is_prime = not(not(i%p))
   j += 1
   primes_left = (j<len(primes))
  if is_prime:
   primes.append(i)


def is_prime(n):
  for i in range(len(primes)):
    p = primes[i]
    if p == n:
      return True
    if not(n%p):
      return False
  return True


# this is not needed for anything but testing
def get_factors(n):
  f = []
  for i in range(len(primes)):
    p = primes[i]
    if p > n:
      return f
    if not(n%p):
      f.append(p)
  return f

#let's just assume it's 9 digits
# factorial(9) is 362880, so, fuck it?

from itertools import permutations

# this got fugly!
def find_first_prime(x):
  for perm in x:
    numb_str = ""
    for digit in perm:
      numb_str += str(digit)
    numb = int(numb_str)
    if is_prime(numb):
      return(numb)

numbies = (9,8,7,6,5,4,3,2,1)
perms = permutations(numbies)
find_first_prime(perms)
# huh! nope.

numbies = (9,8,7,6,5,4,3,2,1)
while (len(numbies) > 0):
  perms = permutations(numbies)
  find_first_prime(perms)
  numbies = numbies[1:]
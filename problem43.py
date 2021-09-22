#4.5 seconds

from itertools import permutations
numbies = (9,8,7,6,5,4,3,2,1,0)
primes = (2,3,5,7,11,13,17)

test_permie = (1,4,0,6,3,5,7,2,8,9)

def mr_function(perm, offset):
    return 100*perm[offset] + 10*perm[offset+1] + perm[offset+2]


def check_perm(perm):
    for offset in range(7):
        if(mr_function(perm,offset + 1)%primes[offset]):
            return False
    return True


def perm_to_int(perm):
    stringy = ""
    for digit in perm:
        stringy += str(digit)
    return int(stringy)

    
answer = 0
for perm in permutations(numbies):
    if check_perm(perm):
        answer += perm_to_int(perm)


print( answer )
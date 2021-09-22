"""
196ms
"""

def find_last_x(x,n):
    # this returns 1 for 0! Dammit
    original_n = n
    result = 1
    # I could filter out trailing 0s, but only 1 in 10 items would have that, so fuck it?
    # yeah, it saves 3 ms
    mask = 10**x
    while n > 0:
        result *= original_n
        n -=1
        result = result - mask*(result//mask)
        # um...I appear to have written out modulo. fine
    return result


answer = 0
also_mask = 10**10
for i in range(1,1000):
    answer += find_last_x(10,i)
    answer = answer%also_mask


if(len(str(answer)) == 10):
    print (answer)
else:
    print( 'you can do this yourself!')
    print( answer)


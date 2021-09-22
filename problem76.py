"""
65ms

oh my fucking god
getting the recursion correct took me FOREVER
litterally hours

the non-memoized version takes 1338 times longer (1m27s) fyi (this was the first way I solved it)(after, again, hours)
(I would love to see the brutality which happened to the stack there)

There should be a way to remove the j == i test with a better definition of the boundary,
but I thought it was just 1's along the zeros but that didn't work
so I think I'm going to give up for now

someone in the comments posted that this is a known problem
https://mathworld.wolfram.com/PartitionFunctionP.html
(In fact the answer is on that page)

My original, slow, non-memoized way is included as a comment at the bottom.
1m29s
"""


# nope, this creates 6 links to the SAME LIST
# memo = [[0]*6]*6

memo = []
for i in range(101):
    memo.append([0]*101)

for i in range(1,101):
    for j in range(1,i+1):
        if j == 1:
            memo[i][j] = 1
            continue
        if j == i:
            memo[i][j] = memo[i][j-1] + 1
            continue
        memo[i][j] = memo[i][j-1] + memo[i-j][min(i-j,j)]

print(memo[100][99])

"""
oh my fucking god
"""
"""
def a_given_b(a,b):
    if a == 0 or b == 0 : return 0
    if a == 1 or b == 1 : return 1
    
    if a == b : return a_given_b(a,b-1) + 1
    
    if b > a : return a_given_b(a, a)
    
    return a_given_b(a, b-1) + a_given_b(a-b,b)

x = a_given_b(100,99)

print(x)
"""

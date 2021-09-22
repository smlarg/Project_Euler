"""
80ms

okay, so I probably premtively optimized,
but I wrote the factorial myself (okay I probaly also could have used like scipy)
in all integer operations, carefully not to overflow the integers, so it could be made to work without type casting/checking

I think I had too much caffiene, honestly
"""



def factorial(n, k):
    # n pick k
    if n - k < k:
        k = n - k
    j = n - k
    if n%2:
        answer = n
        n -= 1
        l = 2
    else:
        answer = 1
        l = 2
    while n > j:
        answer *= n
        n -= 1
        if l <= k:
            answer //= l
            l += 1
    return answer

count = 0
for i in range(1,101):
    for j in range(1,i+1):
        if factorial(i,j) > 1000000:
            count +=1

print( count )
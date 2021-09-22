"""
I'm sorry it's preposterous that this works
I mean, I get it in terms of complexity analysis
but python makes this really easy

254ms
"""


def sum_of_digits(n):
    a = [char for char in str(n)]
    s = 0
    for c in a:
        s += int(c)
    return s

m = 0
for i in range(100):
    for j in range (100):
        x = i**j
        s = sum_of_digits(x)
        m = max(m, s)

print( m )
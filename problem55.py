"""
obviously I haven't even fixed the stupid function names here, so i didn't work hard on this
seems like this one was just informative

109ms
"""

def reversate_number(n):
    return int(str(n)[::-1])

def check_palindromateness(n):
    return str(n) == str(n)[::-1]

outer_count = 0
for i in range(10000):
    eye = i
    count = 0
    i += reversate_number(i)
    while (not check_palindromateness(i)) and (count < 50):
        i += reversate_number(i)
        count += 1
    if count > 49:
        #print( eye )
        outer_count += 1

print( outer_count )
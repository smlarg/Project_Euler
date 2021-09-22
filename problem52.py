"""
913ms

was really thinking I would have to bring bigger guns to this....
"""


def digitize(n):
    l = [char for char in str(n)]
    l = [int(char) for char in l]
    l.sort()
    return l


for i in range(1,10000000):
    d = digitize(i)
    j = 2
    while j<7:
        dd = digitize(i*j)
        if d != dd:
            break
        j += 1
    if j >= 7:
        print(  i, i*2, i*3, i*4, i*5, i*6 )
        break

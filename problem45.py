"""
164 ms, so fine
"""

max_n = 100000
tri = []
for n in range(1,max_n):
    tri.append(int(n*(n+1)/2))


pent = []
p = 1
n = 1
max_tri = tri[-1]
while ( p < max_tri ):
    p = int(n*(3*n-1)/2)
    pent.append(p)
    n+=1


hexx = []
h = 1
n = 1
while ( h < max_tri ):
    h = n*(2*n - 1)
    hexx.append(h)
    n+=1


penteset = set(pent)
hexeset = set(hexx)

for t in tri:
    if (t in penteset) and (t in hexeset):
        print( t )


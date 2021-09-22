"""
2.2s

comments point out you don't even need to count for each i,j, there's an analytic solution straight from m,n = m(m+1)n(n+1)/4
(comes from the fact that you make any rectangle by picking two lines down and two lines across, and m+1 choose 2 is m(m+1)/2 )
"""

def get_those_tots(m,n):
    tots = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            tots += (m-i+1)*(n-j+1)
    return tots

m = 1
n = 1
edges = []
while True:
    while True:
        if get_those_tots(m,n) > 2000000: break
        m +=1
    edges.append([m,n])
    n+=1
    if n > m: break
    m=1

best = 2000000
for edge in edges:
    tot = get_those_tots(edge[0],edge[1])
    if abs(tot - 2000000) < best:
        best = abs(tot - 2000000)
        winner = edge
    tot = get_those_tots(edge[0]-1,edge[1])
    if abs(tot - 2000000) < best:
        best = abs(tot - 2000000)
        winner = [edge[0]-1,edge[1]]


print( winner[0]*winner[1] )
"""
This doesn't prove the answer (I guessed and the website allowed it)
and even so takes a long time
so I'm not super happy
but I'm not going to dwell
"""

pents = []
more_pents = []
max_n = 10000
for n in range(1,max_n):
    pents.append(int(n*(3*n - 1)/2))


for n in range(1, 2*max_n):
    # should only need sqrt(2)* max_n, but I'll deal with that later
    more_pents.append(int(n*(3*n - 1)/2))
    

num_pents = len(pents)
penteset = set(more_pents)

for i in range(num_pents):
    for j in range(i+1, num_pents):
        s = pents[j] + pents[i]
        D = pents[j] - pents[i]
        if (s in penteset) and (D in penteset):
            print( pents[i], pents[j])


current_gap = 7042750 - 1560090

n = 0
while( (int(n*(3*n - 1)/2) - int((n-1)*(3*(n-1) - 1)/2)) < current_gap):
    n+=1
    # I do not choose to solve this algebraically


pents = []
more_pents = []
max_n = n

for n in range(1,max_n):
    pents.append(int(n*(3*n - 1)/2))


for n in range(1, 2*max_n):
    # should only need sqrt(2)* max_n, but I'll deal with that later
    more_pents.append(int(n*(3*n - 1)/2))


num_pents = len(pents)
penteset = set(more_pents)

for i in range(num_pents):
    for j in range(i+1, num_pents):
        s = pents[j] + pents[i]
        D = pents[j] - pents[i]
        if (s in penteset) and (D in penteset):
            print( pents[i], pents[j])


# okay this is actually taking a long time
# ah, okay I cheated, those were the right answer; I haven't proved it though
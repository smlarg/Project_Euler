"""
196ms

Gives the correct answer in terms of rankings, but the actual percentages don't match the test case

My suspicion is it has to do with rolling doubles - I'm unclear what happens if you roll *4* doubles, do both 3 and 4 bring you to jail?
And I think there was a rule about rolling again if you roll a double? I'm almost positive that wasn't in the problem description though
   oh! maybe the phrasing means after each roll, so if you roll a double it's like a second turn i.e. just the same?
I don't suspect the cards not being shuffled matters

but the Markov math works. for some reason I had to figure this out myself, it wasn't explictly in any of my books; it's this:
take the transition matrix and subtract the identity (since 1 is an eigen value) TMx = x => (TM-1)x == Ax = 0
this set of equations is now degenerate however, and if solved as is will give x=0, A*0 = 0,
so drop the last row and replace it with all ones, then sovle Ax=b where b = [0,0,...1] using simple row elimination
that is to say, the last row enforces the normalization condition

(you should also be able to solve for the eigenvectors, and keep the one with the greatest (=1) eigenvector
(but a: you don't need to do that, the above is simpler; and 2: when I did it it wasn't working, don't know why)

Uh, what I'm describing is litterally solving for the eigenvector, or the null-space, nothing special to Markov
there must be a reason this isn't the way...
"""


"""
Markov chain!!!!
"""

from fractions import Fraction
import numpy as np
from scipy.linalg import solve

nstates = 40
die = 4

transition_matrix = [[0]*nstates for _ in range(nstates)]
# actually I think this might be transposed from the way I want to think of it
# or rather, the way I have it below is transposed
# ah, no, rather you multiply the state vector on the left? okay

for i in range(nstates):
    # roll dice
    for j in range(1,die+1):
        for k in range(1,die+1):
            if j != k:
                transition_matrix[i][(i+j+k)%nstates] += Fraction(1,die*die)
            else:
                # 1 in die**2 chance the last two throws were doubles
                transition_matrix[i][(i+j+k)%nstates] += Fraction(1,die*die)*Fraction(die*die - 1,die*die)
                transition_matrix[i][10] += Fraction(1,die*die)*Fraction(1,die*die)
    
    
    # go to jain square
    transition_matrix[i][10] += transition_matrix[i][30]
    transition_matrix[i][30] = 0
    
    # community chest, at 2, 17, and 33
    for l in [2,17,33]:
        t = transition_matrix[i][l]
        transition_matrix[i][l]   = t * Fraction(14,16)
        transition_matrix[i][0]  += t * Fraction(1,16)
        transition_matrix[i][10] += t * Fraction(1,16)
    
    # chance, at 7, 22, and 36
    aDict = {7:15, 22:25, 36:5}
    for l in [7,22,36]:
        t = transition_matrix[i][l]
        transition_matrix[i][l]   = t * Fraction(6,16)
        transition_matrix[i][0]  += t * Fraction(1,16) # Go
        transition_matrix[i][10] += t * Fraction(1,16) # Jail
        transition_matrix[i][11] += t * Fraction(1,16) # C1
        transition_matrix[i][24] += t * Fraction(1,16) # E3
        transition_matrix[i][39] += t * Fraction(1,16) # H2
        transition_matrix[i][5]  += t * Fraction(1,16) # R1
        #x = ((l//10)*10 + 15)%40
        #fuckit
        x = aDict[l]
        transition_matrix[i][x]  += t * Fraction(2,16) # Next railroad (two cards)
        if l == 22:
            transition_matrix[i][28] += t * Fraction(1,16) # utility company
        else:
            transition_matrix[i][12] += t * Fraction(1,16)
        if l != 36:
            transition_matrix[i][l-3] += t * Fraction(1,16) # go back 3
        else:
            # oh boy
            transition_matrix[i][33] += t * Fraction(1,16)*Fraction(14,16)
            transition_matrix[i][0]  += t * Fraction(1,16)*Fraction(1,16)
            transition_matrix[i][10] += t * Fraction(1,16)*Fraction(1,16)
        

for i in range(nstates):
    sum(transition_matrix[i])

# scipy.linalg.solve?
# transpose
tmT = [[0]*(nstates) for _ in range(nstates)]
for i in range(nstates):
    for j in range(nstates):
        tmT[i][j] = transition_matrix[j][i]*1.0
        if i == j: tmT[i][j] -= 1

tmT[-1] = [1]*(nstates)
tmT = np.array(tmT)
b = np.zeros(nstates)
b[-1] = 1


x = solve(tmT, b)
# appears to work, but answer does not agree with provided solution. mrr.
# typos....and rules...
# just too much jail now...
# chance can land on commity chest!!!!
# still not it

y = [ n for n in x]
one = y.pop(y.index(max(y)))
two = y.pop(y.index(max(y)))
three = y.pop(y.index(max(y)))

y = [ n for n in x]
print( y.index(one), y.index(two), y.index(three))
# hmm, get's the right sequence...., just try it?
# Yes! But I'm not happy.

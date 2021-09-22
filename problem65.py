
"""
41ms
"""

es_sequence = []

for i in range(1,100+1):
    if not i%3: es_sequence.append(i//3 *2)
    else: es_sequence.append(1)

es_sequence[0] = 2
es_sequence.reverse()

from fractions import Fraction

F = Fraction(es_sequence.pop(0),1)

for s in es_sequence:
    F = s + 1/F


print ( sum( [int(x) for x in str(F.numerator)]))
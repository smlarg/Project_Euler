"""
210ms

I don't know why this problem was ranked at 25%

And actually, I'm surprised this works, this isn't the right way to do it
this checks every permutation, even if part of it has been disqualified
really I need to make the permutations myself, with like copy() and pop(index) or something

(9! is small is I think the problem here)
"""

from itertools import permutations

s = [9,8,7,6,5,4,3,2,1]

p = permutations(s)

listies = []
for ap in p:
    summy = 10 + ap[0] + ap[1]
    if not summy == ap[2] + ap[1] + ap[3]: continue
    if not summy == ap[4] + ap[3] + ap[5]: continue
    if not summy == ap[6] + ap[5] + ap[7]: continue
    if not summy == ap[8] + ap[7] + ap[0]: continue
    
    missordered_list = [[10,ap[0],ap[1]], 
      [ap[2] , ap[1] , ap[3]],
      [ap[4] , ap[3] , ap[5]],
      [ap[6] , ap[5] , ap[7]],
      [ap[8] , ap[7] , ap[0]]]*2
    outside = [10, ap[2], ap[4], ap[6], ap[8]]
    ind = outside.index(min(outside))
    ordered_list = missordered_list[ind:ind+5]
    listies.append(ordered_list)


# there's a way to do this in one line, but, well you see what's happening here
unwrap = []
for listacle in listies:
    temp = [str(num) for list2 in listacle for num in list2]
    temp = int("".join(temp))
    unwrap.append( temp)

print(max(unwrap))
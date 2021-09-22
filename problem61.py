"""
61ms

It would be better to refactor as some kind of recursive call rather than the hand-nested if's,
but I actually managed to only have one typo the first time I wrote this (a missed break)
"""


from itertools import permutations


m = []
p = -1
n = 1
while p < 10000:
    p = (n*(n+1))//2
    n += 1
    m.append(p)

m.pop()
nums_3 = [ t for t in m if t >999 and (t//10)%10]

m = []
p = -1
n = 1
while p < 10000:
    p = n*n
    n+=1
    m.append(p)

m.pop()
nums_4 = [ t for t in m if t >999 and (t//10)%10]


m = []
p = -1
n = 1
while p < 10000:
    p = (n*(3*n-1))//2
    n+=1
    m.append(p)

m.pop()
nums_5 = [ t for t in m if t >999 and (t//10)%10]

# breakAll= False
# for pent in nums_5:
#     suff = pent%100
#     others = (nums_3, nums_4)
#     for set1, set2 in permutations(others):
#         for num1 in set1:
#             if num1//100 == suff:
#                 suff1 = num1%100
#                 for num2 in set2:
#                     if num2//100 == suff1:
#                         if num2%100 == pent//100:
#                             print("k")
#                             breakAll = True
#                             break
                    
#                 if breakAll: break
#         if breakAll: break
#     if breakAll: break


m = []
p = -1
n = 1
while p < 10000:
    p = (n*(2*n-1))
    n+=1
    m.append(p)

m.pop()
nums_6 = [ t for t in m if t >999 and (t//10)%10]

m = []
p = -1
n = 1
while p < 10000:
    p = (n*(5*n-3))//2
    n+=1
    m.append(p)

m.pop()
nums_7 = [ t for t in m if t >999 and (t//10)%10]

m = []
p = -1
n = 1
while p < 10000:
    p = (n*(3*n-2))
    n+=1
    m.append(p)

m.pop()
nums_8 = [ t for t in m if t >999 and (t//10)%10]


others = (nums_3, nums_4, nums_5, nums_6, nums_7)
breakAll= False
for octa in nums_8:
    suff = octa%100
    for set1, set2, set3, set4, set5 in permutations(others):
        for num1 in set1:
            if num1//100 == suff:
                suff1 = num1%100
                for num2 in set2:
                    if num2//100 == suff1:
                        suff2 = num2%100
                        for num3 in set3:
                            if num3//100 == suff2:
                                suff3 = num3%100
                                for num4 in set4:
                                    if num4//100 == suff3:
                                        suff4 = num4%100
                                        for num5 in set5:
                                            if num5//100 == suff4:
                                                if octa//100 == num5%100:
                                                    print(octa, num1, num2, num3, num4, num5)
                                                    breakAll = True
                                                    break
                                            if breakAll: break
                                    if breakAll: break
                            if breakAll: break
                    if breakAll: break
            if breakAll: break
        if breakAll: break
    if breakAll: break


print (octa + num1 + num2 + num3 + num4 + num5)


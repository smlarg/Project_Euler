"""
9 seconds

somehow I thought set searches would save me from the factorial complexity of permutations
it did not
"""

from itertools import permutations

cubes = []
for i in range(10000):
    cubes.append(i**3)

#cubeset = set(cubes)

# def number_perms(n):
#     a = [x for x in str(n)]
#     b = [int("".join(x)) for x in permutations(a)]
#     l = len(str(n))
#     b = [x for x in b if x > 10**(l-1)]
#     b = set(b)
#     return b

# for c in cubes:
#     break
#     p = number_perms(c)
#     if len(p.intersection(cubeset)) >= 5:
#         print(c)
#         print( round( c **(1/3)))
#         break


def classify_perm_er_class(n):
    c = [0]*10
    for x in str(n):
        c[int(x)] += 1
    return c

cube_classes = []
for c in cubes:
    cube_classes.append(classify_perm_er_class(c))

counts = []
for c in cube_classes:
    e = 0
    for d in cube_classes:
        if c == d:
            e+=1
    counts.append(e)

NOT_THE_answer = counts.index(5)
answer = NOT_THE_answer**3

# x = cube_classes[NOT_THE_answer]
# cube_classes.pop(cube_classes.index(x))
# second = cube_classes.index(x) + 1
# cube_classes.pop(cube_classes.index(x))
# third = cube_classes.index(x) + 2
# cube_classes.pop(cube_classes.index(x))
# fourth = cube_classes.index(x) + 3
# cube_classes.pop(cube_classes.index(x))
# fifth = cube_classes.index(x) + 4


# print(NOT_THE_answer, second, third, fourth, fifth)
# print(answer, second**3, third**3, fourth**3, fifth**3)
print(answer)
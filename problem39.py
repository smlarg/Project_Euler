"""
obviously I didn't try very hard here,
but this only takes just under a minute
(the answer is 840, with 8, fyi)
"""

counts = []

for p in range(3,1001):
  count = 0
  for a in range(1,p-2):
    for b in range(1,a):
      if (p*p + 2*a*b - 2*p*(a+b) == 0):
        count += 1
  if count> 4:
    print (str(p) + ' : ' + str(count))




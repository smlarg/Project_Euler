"""
So. It took well under a second to do the below code in the end, because I keep having typos in my math,
and I wrote the below code to check my math, and, anyway
BUT
by hand you can solve by
the first 9 numbers take 9
the first 99 numbers take 9 + 90*2 = 189
the first 999 numbers take 9 + 90*2 + 900*3 = 2889
the first 9999 numbers take 2889 + 9000*4 = 38889
the first 99999 numbers take 488889

1 = 1 -> d_1 = 1
10 = 9 + 0*2 + 1
  10 + 0 = 10, the first digit of "10" is 1
    -> d_10 = 1
100 = 9 + 45*2 + 1
  10 + 45 = 55, the first digit of "55" is 5, d_100 = 5
1000 = 189 + 270*3 + 1
  100 + 270 = 370, the first digit is 3
10000 = 2889 + 1777*4 + 3
  1000 + 1777 = 2777, the THIRD digit is 7
100000 = 38889 + 12222*5 + 1
 10000 + 12222 = 22222, the first digit is 2
1000000 = 488889 + 85185*6 + 1
 100000 + 85185 = 185185, the first digit is 1
 
1*1*5*3*7*2*1 = 5*3*7*2 = 210
  
"""

x = ""
for i in range(1000000):
 x = x + str(i)

y = 1
for i in range(6):
 y *= int(x[10**i])

print(y)

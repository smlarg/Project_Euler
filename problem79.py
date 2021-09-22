"""
I just did it by hand
There turned out to be no repeated digits, so you could find the digit which never appears after any others, the one which only appears after that, etc.

would like to think of an algorithm though, so I left the array here

most naive way I can think of:
   take the set of all numbers with n digits
   use the numbers below as masks
   when the set is empty, increment n

improvement:
  make a set of all the digits which appear
  take the set of all numbers with n digits, which contain all of the digits below
  mask as above

Ah, that would mean the number has to be at least as long as set(all digits)
   -> no repeats, original algorithm works
if you then get a contradiction, there's at least one repeated (or missing? no we would just not know) digit
-> cycle through each digit assuming it's the repeated one, then all sets of two digits, etc

but I'm not sure what the repeated digit algoritm is

(if any triple below has a repeated digit, of course, then we know which it is; that's a third algorithm)

"""


s = """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716"""

i = [int(x) for x in s.split('\n')]

print( 73162890 )
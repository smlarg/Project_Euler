"""
lot of python structures built and destroyed, probably 1000x slow or more
but
1.6s

spent a long time trying to get the right test, I couldn't easily tune letter frequency
(the proper way would have been chi-squared on mutliple letters, but, I did not do that
(still thought it would have been workable though)
"""


cyphertext = []
with open("p059_cipher.txt") as file:
    for line in file:
        #only one, but
        for n in line.split(','):
            cyphertext.append(int(n))


a = ord('a')
z = ord('z')

char_count = len(cyphertext)

for i in range(a, z+1):
    for j in range(a, z+1):
        for k in range(a, z+1):
            keys = [i,j,k]*(int(char_count/3))
            plaintext = []
            good = False
            for cyph, k in zip(cyphertext, keys):
                plaintext.append(chr(cyph^k))
            text = "".join(plaintext)
            if (' the ' in text) and (' and ' in text) and (' to ' in text):
                result = 0
                for cyph, k in zip(cyphertext, keys):
                    result += cyph^k
                good = True
            if good:
                break
        if good:
            break
    if good:
        break

print( result)
print( text)


#i,j,k = 101, 120, 112
#keys = [i,j,k]*(int(char_count/3))
#plaintext = []
#for cyph, k in zip(cyphertext, keys):
#    plaintext.append(chr(cyph^k))
#text = "".join(plaintext)


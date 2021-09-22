# of course it's ugly, but it's 42ms, moving on

words_here = []

with open("p042_words.txt", 'r') as file:
  for line in file:
    for word in line.split(sep=','):
      words_here.append(word)

#whatever
words_here_X = words_here.copy()
words_here = []
for word in words_here_X:
  words_here.append(word[1:-1])


del(words_here_X)

def word_value(word):
  value = 0
  for char in word:
    value += (ord(char) - 64)
  return value


# let's see what the largest number is

m = 0
for word in words_here:
  m = max(m, word_value(word))

#192

triangle_numbers = []
n = 1
t = -1
while (t< m):
  t = int( 0.5*n*(n-1))
  triangle_numbers.append(t)
  n +=1

triangle_numbers = set(triangle_numbers)

answer = 0
for word in words_here:
  if word_value(word) in triangle_numbers:
    answer +=1

print ( answer)
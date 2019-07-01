'''
Program to scramble the letters in words
'''
import random
words = ['rabbit', 'horse', 'elephant', 'goat', 'bear', 'chicken']
# Strings are immutable
list_words = [list(w) for w in words]
print(list_words)

for w in list_words:
    random.shuffle(w)

scrambled_words = [''.join(w) for w in list_words]
print(scrambled_words)
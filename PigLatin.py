word = input("Enter a word: ")

VOWELS = 'aeiouy'

if word[0] in VOWELS:
    output = word[1:] + word[0] + 'ay'
else:
    output = word[1:] + 'way'

print(output)
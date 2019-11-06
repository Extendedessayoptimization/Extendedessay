import random
import string


password = list("abcdefghijklmnopqrstuvwxyz")
random.shuffle(password)
print(''.join(password))

textfile=open('Dorian Grey_extract1.txt')
outfile=open('output_test_3.txt', 'w')
for line in textfile:
    for letter in line:
        if (letter.isalpha()):
            c = string.ascii_lowercase.index(letter.lower())
            letter = password[c]
        outfile.write(letter)

outfile.close()
textfile.close()


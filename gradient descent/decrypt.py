import random
import string


password = list("sqehfokpavudyixmbtnlzcrjgw")

alphabet=list("abcdefghijklmnopqrstuvwxyz")
reverse_password=[None]*26
for index in range (0,26):
    a=alphabet[index]
    pa=password[index]
    reverse_password[string.ascii_lowercase.index(pa)]=a


textfile=open('output_test_1.txt')
outfile=open('output_test_2.txt', 'w')
for line in textfile:
    for letter in line:
        if (letter.isalpha()):
            c = string.ascii_lowercase.index(letter.lower())
            letter = reverse_password[c]
        outfile.write(letter)

outfile.close()
textfile.close()


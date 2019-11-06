import numpy
import string
import re
import math
import random

def recursion():
    trial_count=0
    success_rate=0
    while (trial_count<=100):
        gradient_descent(s_filtered, frec)
        evaluation(pwd)
    print(success_rate,trial_count)


def evaluation(pwd):
    if (pwd==list("abcdefghijklmnopqrstuvwxyz")):
        s=s+1

def position_quadgram(q):
    return string.ascii_lowercase.index(q[0])*26**3+string.ascii_lowercase.index(q[1])*26**2+string.ascii_lowercase.index(q[2])*26+string.ascii_lowercase.index(q[3])

def score(s,f):
    result=0.0
    for i in range(0,len(s)-4):
        q=s[i:i+4]
        p=position_quadgram(q)
        result=result+math.log(f[p]+1)
    return result

def decrypt(letters,password,letters_new):
    for i in range(0, len(letters)):
        c = string.ascii_lowercase.index(letters[i])
        letters_new[i]=password[c]

def switch(b,c,password):
    a = password[b]
    password[b] = password[c]
    password[c] = a

def gradient_descent(s_filtered,frec):
    password=list("abcdefghijklmnopqrstuvwxyz")
    s_decrypted=s_filtered[:]
    decrypt(s_filtered,password, s_decrypted)
    score_actual=score(s_decrypted,frec)
    counter=0
    trial_count=trial_count+1
    while(counter<1000):
        b=random.randint(0,25)
        c=random.randint(0,25)
        switch(b,c,password)
        decrypt(s_filtered,password,s_decrypted)
        score_new=score(s_decrypted,frec)
        if(score_actual<score_new):
            score_actual=score_new
            counter=0
            print(score_actual)
        else:
            switch(b,c,password)
            counter=counter+1
            print(counter)
    return password


def simulated_annealing(s_filtered,frec):
    password=list("abcdefghijklmnopqrstuvwxyz")
    s_decrypted=s_filtered[:]
    decrypt(s_filtered,password, s_decrypted)
    score_actual=score(s_decrypted,frec)
    counter=0
    for temperature in numpy.arange(10,0,-0.01):
        for counter in range(1,100):
            b=random.randint(0,25)
            c=random.randint(0,25)
            switch(b,c,password)
            decrypt(s_filtered,password,s_decrypted)
            score_new=score(s_decrypted,frec)
            r=random.uniform(0,1)
            v=math.exp((score_new-score_actual)/temperature)
            if(r<v):
                score_actual=score_new
            else:
                switch(b,c,password)
        print(temperature)
    return password

quadfile=open('english_quadgrams.txt')
frec=numpy.zeros([26**4,1],numpy.uint32)
for line in quadfile:
    quadgram,count=line.split(" ")
    frec[position_quadgram(quadgram.lower())]=int(count)
quadfile.close()

textfile=open('output_test_4.txt')
s = textfile.read()
regex = re.compile('[^a-zA-Z]')
s_filtered = regex.sub('',s)
s_filtered = s_filtered.lower()
s_filtered=list(s_filtered)

l=score(s_filtered,frec)


pwd=gradient_descent(s_filtered,frec)

textfile.seek(0,0)
outfile=open('unencrypted_gd.txt', 'w')
for line in textfile:
    for letter in line:
        if (letter.isalpha()):
            c = string.ascii_lowercase.index(letter.lower())
            letter = pwd[c]
        outfile.write(letter)

outfile.close()
textfile.close()


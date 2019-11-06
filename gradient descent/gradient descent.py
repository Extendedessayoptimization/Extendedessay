import random
import numpy
import csv



def cost(p, a, b):
    [x, y] = p
    return numpy.sum((x*a+b-y)**2)



def gradient_descent(p):
    a = random.randrange(1, 50)
    b = random.randrange(1, 100)
    c = 0
    epsilona = 1.0
    epsilonb = 1.0
    while epsilona > 0.001 or epsilonb > 0.001:
        if (cost(p, a + epsilona, b) < cost(p, a, b)):
            a = a + epsilona
        elif (cost(p, a - epsilona, b) < cost(p, a, b)):
            a = a - epsilona
        else:
            epsilona = epsilona / 2

        if (cost(p, a, b + epsilonb) < cost(p, a, b)):
            b = b + epsilonb
        elif (cost(p, a, b - epsilonb) < cost(p, a, b)):
            b = b - epsilonb
        else:
            epsilonb = epsilonb / 2

        c=c+1

    print(a, b)
    print (c)
    print (epsilona)




#Initialize empty p matrix
p=numpy.array([0 , 0])
#Open file with data
file = open('data_1.csv', 'r')
try:
    #Read file as CSV with
    reader = csv.reader(file, delimiter=',')
    #Read each line
    for line in reader:
        #Get a line
        [i,j]=line
        i=float(i)
        j=float(j)
        #Convert values from string to numerical values
        #Add the values to p
        p = numpy.vstack([p, [i,j]])
finally:
    file.close()


p = p[1:, :]
p = numpy.transpose(p)

gradient_descent(p)




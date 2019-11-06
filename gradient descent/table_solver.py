import random
import numpy
import csv



def cost(array_friendship, placement):
    l=0
    for t in range(0,10):
        p = numpy.where(placement==t)
        p = p[0]
        for i in range(0,9):
            for j in range(i+1,10):
                l = l+(1-array_friendship[p[i],p[j]])
    return l



def gradient_descent(array_friend):

    place = numpy.zeros([100], numpy.uint8)
    for table in range(0, 10):
        place[table * 10:table * 10 + 10] = range(0, 10)

    c_old = cost(array_friend, place)
    k=0
    while(c_old>0 and k<10000):
        i=random.randint(0,99)
        j=random.randint(0,99)
        a=place[i]
        place[i]=place[j]
        place[j]=a
        c_new=cost(array_friend,place)
        if(c_new>=c_old):
            a = place[i]
            place[i] = place[j]
            place[j] = a
            k=k+1
        else:
            c_old=c_new
            k=0

        print (c_old, k)

    print (place)



    return place



array_friend = numpy.zeros([100, 100], numpy.uint8)
file = open('data_table.csv', 'r')
k=0
try:
    reader = csv.reader(file, delimiter=';')
    for line in reader:
        array_friend[k, :] = line
        k=k+1
finally:
    file.close()





#print place
gradient_descent(array_friend)
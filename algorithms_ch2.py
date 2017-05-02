#chapter 2 of introduction to algorithms sorting methods coded
import matplotlib


def insertionSort(x):
    for c in range(1,len(x)):
        key = x[c]
        i = c
        while (i > 0 and x[i-1] > key):
            x[i] = x[i-1]
            i = i-1
        x[i] = key


a = [6,8,9,5,4,8]
b = [9,7,9,6,7,100,101]
c = [9,70,67,75,100,105]

insertionSort(a)
insertionSort(b)
insertionSort(c)

print(a,b,c)

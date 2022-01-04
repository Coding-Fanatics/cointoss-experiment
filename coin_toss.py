from random import randint as rand
import matplotlib.pyplot as plt

#creating a variable for number of coins
global coins
coins = int(input("number of coins you're using:"))


val = []
counts = {}


def count(n):
    for i in range(n):
        out = rand(0,coins)
        val.append(out)


 
 
n = input("enter the number of trials:")
n = int(n)
count(n) 

for value in val:
      if value in counts:
        counts[value] += 1
      else:
        counts.update({value : 1})
        

#plotting the observerd freaquencies

#sorting the dictionary in ascending order
l = list(counts.items())
l.sort()
counts = dict(l)

#defining the x and y axis
x = counts.keys()
y = counts.values()

plt.plot(x,y)

plt.show()


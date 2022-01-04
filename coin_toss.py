from random import randint as rand
import matplotlib.pyplot as plt
import numpy as np



#creating a variable for number of coins
global coins
global trial

#taking input from the user

coins = int(input("enter number of coins:"))
trial = int(input("enter the number of trials:"))


val = []
counts = {}

def coin_toss():
  output = rand(0,1)
  val.append(output)

def tosser():
  for i in range(coins):
    coin_toss()




def counter():
    global val
    val = np.array(val)
    value = val.sum()
    if value in counts:
      counts[value] += 1
    else:
      counts.update({value : 1})  

    val = []        


def start():
  global trial


  for i in range(trial):
    tosser()
    counter()

  
start()

l = list(counts.items())
l.sort()
counts = dict(l)  

#plotting graph
x = counts.keys()
y = counts.values()

plt.xlabel("values")
plt.ylabel("freaquency")

plt.plot(x,y)

plt.show()

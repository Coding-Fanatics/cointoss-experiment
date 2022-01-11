from random import randint as rand
import matplotlib.pyplot as plt
import numpy as np
from math import factorial
import pandas as pd



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


theor_freq =[]

def theorotical(N,n):
  #hello
  for r in range(n):
    theor_freq.append( (N* factorial(n))  / ( (factorial(n-r) * factorial(r) ) * (2**n) ))

  

def start():
  global trial


  for i in range(trial):
    tosser()
    counter()

  theorotical(trial,coins)  

  

start()

l = list(counts.items())
l.sort()
counts = dict(l)  

data = {"Number of Heads":counts.keys(),
"freaquency": counts.values()}

df = pd.DataFrame(data)

print(df)


#plotting graph
x = counts.keys()
y = counts.values()

#graph variables defining
x_thear = [i for i in range(coins)]
y_thear = theor_freq

#print(x_thear,y_thear)

k = np.array([str(x),str(y)])
#print(k)

data_th = {"Theoretical Number of Heads":x_thear,"Theoretical freaquency": y_thear}
df_th = pd.DataFrame(data_th)
print("Theoretical Random Distribution")
print(df_th)

plt.xlabel("values")
plt.ylabel("freaquency")

plt.plot(x,y)

plt.plot(x_thear,y_thear)

plt.legend(['Generated Random distribution','Theoretical Random distribution'], loc = 'lower right')

plt.show()

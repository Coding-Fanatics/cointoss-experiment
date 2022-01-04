from random import randint as rand
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image

#creating a variable for number of coins
global coins
global trial

#web app UI 
st.header(" ## Coin Toss experiment")

#getting the input from the user
coins = st.slider("number of coins you're using",1,100,12)
trial = st.slider("number of trials:",1,10000,400)


# to store random values

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
  for i in range(trial):
    tosser()
    counter()

button = st.button("show graph")

start()

l = list(counts.items())
l.sort()
counts = dict(l)  

print(counts)

if button:
  #plotting graph
  x = counts.keys()
  y = counts.values()

  plt.xlabel("values")
  plt.ylabel("freaquency")

  plt.plot(x,y)
  #saving graph as a figure
  
  plt.savefig("output.jpg")
  image = Image.open('output.jpg')
  st.image(image, caption = 'freaquency distribution', use_column_width = True)

#plt.plot(x,y)
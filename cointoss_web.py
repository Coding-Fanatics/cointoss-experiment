from random import randint as rand
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image
from math import factorial
import pandas as pd

#creating a variable for number of coins
global coins
global trial

#web app UI 
st.header("Coin Toss Experiment")

#getting the input from the user
coins = st.slider(" number of coins you're using",1,100,12)
trial = st.slider(" number of trials:",1,10000,400)


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

theor_freq =[]

#calculating theoretical values
def theorotical(N,n):
  for r in range(n):
    theor_freq.append( (N* factorial(n))  / ( (factorial(n-r) * factorial(r) ) * (2**n) ))


def start():
  for i in range(trial):
    tosser()
    counter()

  theorotical(trial,coins)  

button = st.button("show graph")
theoretical = st.checkbox("Show Theoretical distribution Also")


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
  plt.ylabel("Freaquency")
  if theoretical == 1 :

      #graph variables defining
      x_thear = [i for i in range(coins)]
      y_thear = theor_freq

      plt.plot(x,y)
      plt.plot(x_thear,y_thear)
      plt.legend(['Generated distribution','Theoretical distribution'], loc = 'upper left')

      #creating table:
      # initialize data of lists.
      data_th = {"Theoretical Number of Heads":x_thear,"Theoretical freaquency": y_thear}
      df_th = pd.DataFrame(data_th)
      st.write(" ## Theoretical Random Distribution")
      st.dataframe(df_th)
      data = {"Number of Heads":counts.keys(),"freaquency": counts.values()}
      df = pd.DataFrame(data)
      st.write("## Generated Random Distribution ")
      st.dataframe(df)
  
  else:
    plt.plot(x,y)
    #creating table:
    # initialize data of lists.
    data = {"Number of Heads":counts.keys(),"freaquency": counts.values()}
    df = pd.DataFrame(data)
    st.write("## Generated Random Distribution ")
    st.dataframe(df)
          


  #saving graph as a figure
  
  plt.savefig("output.jpg")
  image = Image.open('output.jpg')

  st.write(" ## Random Distribution Graph")
  st.image(image, caption = 'freaquency distribution', use_column_width = True)

  end_note = "\n"*10 + "Made with ❤️ \n ~'SVIT-CODING-FANATICS'"
  st.write(end_note)

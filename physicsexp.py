from random import randint as rand
import matplotlib.pyplot as plt



val = []
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0


def count(n):
    for i in range(n):
        out = rand(0,12)
        val.append(out)


 
 
n = input("enter the number of trials:")
n = int(n)
count(n) 

for value in val:
        
        if value == 0:
            a +=1
        elif value == 1:
            b +=1
        elif value == 2:
            c +=1
        elif value == 3:
            d +=1
        elif value == 4:
            e +=1
        elif value == 5:
            f +=1
        elif value == 6:
            g +=1
        elif value == 7:
            h +=1
        elif value == 8:
            i +=1
        elif value == 9:
            j +=1
        elif value == 10:
            k +=1
        elif value == 11:
            l +=1
        elif value == 12:
            m +=1
        
counts = [a,b,c,d,e,f,g,h,i,j,k,l,m]

print(counts)    

x = [0,1,2,3,4,5,6,7,8,9,10,11,12]
y = counts

plt.plot(x,y)


plt.show()
    
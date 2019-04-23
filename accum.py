import matplotlib.pyplot as plt
import numpy as np
n=int (input("enter the n value"))
sum=0
for i in range(1,n):
          sum=sum+i
          p=sum
          print (p)
          plt.plot(n,p)
plt.show( )
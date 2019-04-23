len1=int(input("enter a length "))
len2=int(input("enter a length "))
x=[]
y=[]
for i in range (0,len1,1):
	a=int(input("enter the value:"))
	x.append(a)
for i in range (0,len2,1):
	a=int(input("enter the number:"))
	y.append(a)
import numpy as np
z=np.zeros(len1+len2-1)
for n in range (0,len1+len2-1):
	b=0
	for k in range (0,len1):
		if ((n-k)>=0 and (n-k)<len2):
			b=b+x[k]*y[n-k]
	z[n]=b
print(z)






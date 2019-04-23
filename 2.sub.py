p=input("enter no. of rows of m1")
q=input("enter no. of columns of m1")
r=input("enter no. of rows of m2")
s=input("enter no. of columns of m2")
if(p==r):
     if(q==s):
	i=0
	a={}
	while(i<p):
		j=0
		while(j<q):
			
			m1=input("enter m1 elements")
			a[i,j]=m1
			j=j+1
		
		i=i+1
	b={}
	i=0
	while(i<r):
			j=0
			while(j<s):
				m2=input("enter m2 elements")
				b[i,j]=m2
				j=j+1
			i=i+1
	c={}
	i=0
	while(i<p):
			j=0
			while(j<s):
				c[i,j]=0
				k=0
				while(k<r):
					c[i,j]=a[i,j]-b[i,j]
					k=k+1
				j=j+1
			i=i+1
	i=0
	while(i<p):
			j=0
			while(j<s):
				print c[i,j]
				j=j+1
			i=i+1
	


	



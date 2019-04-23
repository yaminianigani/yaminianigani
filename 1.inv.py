def cofactor(a):
	c=len(a)
	cofa=[]
	for i in range(c):
		f=[]
		for j in range(c):
			b=[]
			for k in range(c):
				e=[]
				for l in range(c):
					if(i==k or j==l):
						continue
					e.append(a[k][l])
				if(e!=[]):
					b.append(e)
			if((i+j)%2==0):
				m=1
			else:
				m=-1
			y=det(b)
			f.append(y*m)
		cofa.append(f)
	return cofa
def det(a):
	c=len(a)
	if(c==1):
		d=a[0][0]*1.0
		return d
	elif(c==2):
		d=(a[0][0]*a[1][1]-a[0][1]*a[1][0])*1.0
		return d
	else:
		t=[]
		t=cofactor(a)
		d=0.0
		for l in range(c):
			d=d+(a[0][l]*t[0][l])
		return d
def transpose(a):
	c=len(a)
	b=[]
	for j in range(c):
		d=[]
		for i in range(c):
			d.append(a[i][j])
		b.append(d)
	return b
print "Enter the matrix in the following format\n[[a11,a12.....,a1n],[a21,a22.....a2n],......,[an1,an2,....ann]]"
print "Ex:[[1,2,3],[4,5,6],[7,8,9]]"
a=input("Enter a matrix :")
c=len(a)
d=det(a)
if(d==0):
	print "Inverse doesn't exist"
elif(c==1):
		inverse=[[1.0/a[0][0]]]
		print inverse
else:
	inverse=transpose(cofactor(a))
	for i in range(c):
		for j in range(c):
			inverse[i][j]=inverse[i][j]/d
	print inverse

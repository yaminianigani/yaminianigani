a=int(input('number of rows'))
b=int(input('number of columns'))
matrix1=[]
for i in range (0,a):
	matrix1+=[0]
for i in range (0,a):
	matrix1[i]=[0]*b
for i in range (0,a):
    for j in range (0,b):
        print ('entry in row: ',i+1,'column: ',j+1)
        matrix1[i][j] = int(input())
for i in range (0,a):
    for j in range (0,b):
        print(matrix1[i][j]),
    print
print('enter rows for second matrix')
print('enter columns for second matrix')

m=int(input('number of rows'))
n=int(input('number of columns'))
matrix2=[]
for i in range (0,m):
	matrix2+=[0]
for i in range (0,n):
	matrix2[i]=[0]*n
for i in range (0,m):
    for j in range (0,n):
        print ('entry in row: ',i+1,'column: ',j+1)
        matrix2[i][j] = int(input())
for i in range (0,m):
    for j in range (0,n):
        print(matrix2[i][j]),
    print
mul=[]
if(b!=m):
	print('cant multiply')
 
else:

	for i in range (0,a):
		mul+=[0]
	for i in range (0,a):
		mul[i]=[0]*b
	for i in range (0,a):
		for j in range (0,n):
			mul[i][j]=0;

			for k in range(0,m):
				mul[i][j] =mul[i][j]+matrix1[i][k]*matrix2[k][j]


print('resultant matrix')
for i in range (0,a):
    for j in range (0,n): 
        print(mul[i][j]),
    print


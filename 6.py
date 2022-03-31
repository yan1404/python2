x=input("")
x=list(x)
for i in range(len(x)):
	for j in range(len(x)):
		if x[i]>x[j]:
			temp=x[i]
			x[i]=x[j]
			x[j]=temp
MAX=""
for i in range(len(x)):
	MAX=MAX+str(x[i])

MIN=""
for i in range(len(x),0,-1):
	MIN=MIN+str(x[i-1])
print 最大值數列與最小值數列差值為：(int(MAX)-int(MIN))
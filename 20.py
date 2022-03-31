x=input("組數為:")

for i in range (int(x)):
	a=input("")
	a=a.split(" ")
	print("第"+str(i+1)+"組應收費用:"+str(int(a[0])*250+int(a[1])*175))

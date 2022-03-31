M=input("請輸入階乘值M:")
x=1
y=1
while(True):
	y=y*x
	if y>=M:
		print("超過Ｍ為"+str(M)+"的最小階層Ｎ值為："+str(x))
		break
	else: 
		x=x+1

x=input("輸入一組四位數字為:")
y=""
for i in range(len(x)):
	y=y+str((int(x[i])+7)%10)
ans=y[2]+y[3]+y[0]+y[1]
print("輸出加密後的數字為:"+ans)
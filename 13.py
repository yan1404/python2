x=str(input("輸入一字元為:"))
y=len(x)
ans="yes"
if(y%2==0):
	for i in range(y/2):
		if(x[i]!=x[y-i-1]):
			ans="NO"

else:
	for i in range(int((y/2)-0.5)):
		if(x[i]!=x[y-i-1]):
			ans="NO"
print(ans)
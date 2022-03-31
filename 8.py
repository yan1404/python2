x=input("n:")
y=(input("m:"))
y=y.split(" ")

reppet = 0
location = 0
for i in range(int(x)):
    temp=0
    for j in range(int(x)):
        if(y[i]==y[j]):
            temp = temp+1
    if(temp > reppet):
        reppet = temp
        location = i
if(reppet == 1):
    print("每個數字剛好只出現1次")
else:
    print("最大出現次數的數字為:"+y[location])
    print("出現次數為:"+str(reppet))
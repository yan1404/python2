x=input("")
y=x.split(" ")

reppet = 0
location = 0
for i in range(len(y)):
    temp=0
    for j in range(len(y)):
        if(y[i]==y[j]):
            temp = temp+1
    if(temp>reppet):
        reppet = temp
        location = i
if(len(y)/2<reppet):
    print(y[location])
else:
    print("NO")

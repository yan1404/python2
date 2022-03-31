s1=str(input("輸入s1為:"))
s2=str(input("輸入s2為:"))
ANS = "NO"
for i in range(len(s2)):
    if(i+len(s1)>len(s2)):
        break

    if(s2[i:i+len(s1)]==s1):
        ANS = "YES"
print(ANS)
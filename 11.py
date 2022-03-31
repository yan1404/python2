x=input("輸入月及日為:")
y=x.split(" ")
if((int(y[0])==1 and int(y[1])>=20) or (int(y[0])==2 and int(y[1])<=18)):
	print("Aquarius")
if((int(y[0])==2 and int(y[1])>=19) or (int(y[0])==3 and int(y[1])<=20)):
	print("Pisces")
if((int(y[0])==3 and int(y[1])>=21) or (int(y[0])==4 and int(y[1])<=20)):
	print("Aries")
if((int(y[0])==4 and int(y[1])>=21) or (int(y[0])==5 and int(y[1])<=21)):
	print("Taurus")
if((int(y[0])==5 and int(y[1])>=22) or (int(y[0])==6 and int(y[1])<=21)):
	print("Gemini")
if((int(y[0])==6 and int(y[1])>=22) or (int(y[0])==7 and int(y[1])<=22)):
	print("Cancer")
if((int(y[0])==7 and int(y[1])>=23) or (int(y[0])==8 and int(y[1])<=23)):
	print("Leo")
if((int(y[0])==8 and int(y[1])>=24) or (int(y[0])==9 and int(y[1])<=23)):
	print("Virgo")
if((int(y[0])==9 and int(y[1])>=23) or (int(y[0])==10 and int(y[1])<=23)):
	print("Libra")
if((int(y[0])==10 and int(y[1])>=24) or (int(y[0])==11 and int(y[1])<=22)):
	print("Scorpio")
if((int(y[0])==11 and int(y[1])>=23) or (int(y[0])==12 and int(y[1])<=21)):
	print("Sagittarius")
if((int(y[0])==12 and int(y[1])>=22) or (int(y[0])==1 and int(y[1])<=20)):
	print("Capricorn")
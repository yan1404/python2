in1=input('abc:')
x=0
y=0

if(in1<=120):
	x=(in1*2.10)
	y=(in1*2.10)
else:
	x=120*2.10
	y=120*2.10

	if(in1<=330):
		x=x+(in1-120)*3.02
		y=y+(in1-120)*2.68
	else:
		x=x+(330-120)*3.02
		y=y+(330-120)*2.68

		if(in1<=500):
			x=x+(in1-330)*4.39
			y=y+(in1-330)*3.61
		else:
			x=x+(500-330)*4.39
			y=y+(500-330)*3.61

			if(in1<=700):
				x=x+(in1-500)*4.97
				y=y+(in1-500)*4.01
			else:
				x=x+(700-500)*4.97
				y=y+(700-500)*4.01

				if(in1>700):
					x=x+(in1-700)*5.63
					y=y+(in1-700)*4.50
print("Summer months:"+str(x))
print("Non-Summer months:"+str(y))
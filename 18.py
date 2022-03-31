x = input("")
x = x.split(" ")
number = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
ans = number[x[0]]+number[x[1]]+number[x[2]]+number[x[3]]+number[x[4]]
print(ans)
a1,b1=map(int,input().split(' '))
a2,b2=map(int,input().split(' '))
a3,b3=map(int,input().split(' '))
if (a1==b2 and a2==a3) or(b1==b2 and b2==b3) or (abs(a1-a2)==abs(a2-a3) and abs(b1-b2)==abs(b2-b3)):
	print("yes")
else:
	print("no")
 

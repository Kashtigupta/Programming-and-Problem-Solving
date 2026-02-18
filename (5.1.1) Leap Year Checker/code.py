d=int(input())
m=int(input())
y=int(input())
flag = True 
if(y<1 or m<1 or m>12):
	flag = False
if m in (1,3,5,7,8,10,12):
	maxdays=31
elif m in (4,6,9,11):
	maxdays=30
else:
	if y % 4 == 0:
		maxdays = 29
	else:
		maxdays = 28


if d>maxdays:
	flag=False

d=d+1
if d>maxdays:
	d=1
	m=m+1
if m>12:
	m=1
	y=y+1

if flag:
	print(f"{d:02d}-{m:02d}-{y:04d}")
else:
	print("Invalid Date")

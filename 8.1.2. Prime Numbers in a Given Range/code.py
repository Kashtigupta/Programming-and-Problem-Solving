start = int(input())
stop = int(input())

F = False

for v in range(start, stop + 1):
	if v > 1:
		flag = True
		for i in range (2, int ((v** 0.5) + 1)):
			if (v % i) == 0:
				flag = False
				break
		if flag:
			print(v)
			F = True 

if not F:
	print("No primes")

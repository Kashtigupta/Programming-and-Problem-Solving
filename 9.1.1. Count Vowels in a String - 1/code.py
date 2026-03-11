st = input()
count = 0 

for i in st:
	if i in ('a', 'e','i','o','u','A','E','I','O','U'):
		count += 1

print(count)

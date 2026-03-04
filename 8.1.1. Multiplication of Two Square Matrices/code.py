n= int(input("dimension: "))
print("first matrix:")
A = []

for i in range(n):
	row =  list(map(int, input().split()))
	A.append(row)

print("second matrix:")
B = []

for i in range(n):
	row =  list(map(int, input().split()))
	B.append(row)

R = []
for i in range (n):
	R.append([0] * n)

for i in range(n):
	for j in range(n):
		for k in range(n):
			R[i][j] = R[i][j] + A[i][k] * B[k][j]

print("Resultant Matrix:")
for i in range(n):
	for j in range(n):
		if (j == n - 1):
			print(R[i][j], end = "")
		else:
			print(R[i][j], end = " ")
	print()


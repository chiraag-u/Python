def IsPrime(n):
	if (n <= 1):
		return False
	for i in range(2, n):
		print(i)
		if (n % i == 0):
			return False
	return True

Number = input("Enter a Number: ")

if IsPrime(int(Number)):
	print(str(Number) + " is a Prime Number")
else:
	print(str(Number) + " is a Composite Number")

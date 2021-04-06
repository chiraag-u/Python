def IsPrime(n):
	if (n <= 1):
		return False
	for i in range(2, n):
		if (n % i == 0):
			return False
	return True

Number = input("Enter a Number: ")

if IsPrime(int(Number)):
	print("True")
else:
	print("False")
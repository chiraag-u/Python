print("\nEven Or Odd")
print("A Program to find if a number is Even or Odd\n")
Number = input("Enter the Number: ")
try:
    if int(Number) % 2 == 0:
        print(str(Number) + " is an Even Number")
    else:
        print(str(Number) + " is an Odd Number")
except:
    print("\nEnter a Number")

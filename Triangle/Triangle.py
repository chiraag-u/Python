print("\nArea and Perimeter of Triangle\n\n    /|\n   / |\n  /  |\n /   |\n/____|\n")
Option = input("Do you want to calculate Area or Perimeter(A/P) ")
if Option.capitalize() == "A":
    print("\nLets Calculate the Area of the Triangle\n")
    Base = input("Enter Base: ")
    Height = input("Enter Height: ")
    try:            
        Area = int(Base) * int(Height) * .5
        print("The Area of triangle is " + str(Area) + " sq.unit")
    except:
        print("Please Provide a Number")
elif Option.capitalize() == "P":
    print("\nLets Calculate the Perimeter of Triangle\n")
    Side1 = input("Enter the Firt Side: ")
    Side2 = input("Enter the Second Side: ")
    Side3 = input("Enter the Third Side: ")
    try:
        Perimeter = int(Side1) + int(Side2) + int(Side3)
        print("The Perimeter of Triangle the is " + str(Perimeter) + " units")
    except:
        print("Please Provide a Number")
else:
    print("Please Enter either Area or Perimeter\n")

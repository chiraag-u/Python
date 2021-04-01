print("\nTriangle Caculator\n\n    /|\n   / |\n  /  |\n /   |\n/____|\n\nWhat do you want to Calculate\nArea or Perimeter\n")
Option = input("Tell Me ")
if Option.capitalize() == "Area":
    print("\nLets Calculate the Area of Triangle\n")
    Base = input("Base: ")
    Height = input("Height: ")
    try:            
        Area = int(Base) * int(Height) * .5
        print("The Area is " + str(Area) + " sq.unit\n\nThankyou for using Triangle Calculator")
    except:
        print("Please Provide a Number")
elif Option.capitalize() == "Perimeter":
    print("\nLets Calculate the Perimeter of Triangle\n")
    Side1 = input("Firt Side: ")
    Side2 = input("Second Side: ")
    Side3 = input("Third Side: ")
    try:
        Perimeter = int(Side1) + int(Side2) + int(Side3)
        print("The Perimeter is " + str(Perimeter) + " units\n\nThankyou for using Triangle Calculator")
    except:
        print("Please Provide a Number")
else:
    print("Sorry I did not understand\n")
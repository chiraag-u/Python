print("\nFatorial Calculator\n")
ANumber = int(input("Enter the postive number to Calculate the Factorial: "))
AnswerNumber = 1
if ANumber == 0 or ANumber == 1:
    print(1)
else:
    while ANumber != 1:
        AnswerNumber = AnswerNumber * ANumber
        ANumber = ANumber - 1
    print(AnswerNumber)
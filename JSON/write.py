import json
DataObject = {
    "Name":"Chiraag",
    "Data":"You can add your Data..."
}
Option = input("Read or Write: ").capitalize()
if Option == "Read":
    with open("ReadandWrite.json", "r") as Data:
        Data = json.load(Data)
    print(Data)
elif Option == "Write":
    with open("ReadandWrite.json", "w") as Data:
        json.dump(DataObject, Data)
else:
    print("Enter a Valid Command")
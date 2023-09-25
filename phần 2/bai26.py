dic=["a","e","i","o","u"]

userInput = input("Nhap chu cai: ")
if userInput in dic:
    print("Nguyen am!")
elif userInput == "y":
    print("Co the la Nguyen am! hoac Phu am!")
else:
    print("Phu am!")
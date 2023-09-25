userList = []
while True:
    userInput = int(input("Nhap so vao danh sach: "))
    if userInput == 0:
        break
    else:
        userList.append(userInput)

print(sorted(userList))
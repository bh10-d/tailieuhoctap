userList = []
while True:
    userInput = input("Nhap tu vao danh sach: ")
    if userInput == '':
        break
    else:
        if userInput in userList:
            continue
        else:
            userList.append(userInput)

print(userList)
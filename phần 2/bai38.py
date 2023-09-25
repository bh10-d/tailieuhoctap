userList = []
while True:
    userInput = input("Nhap so vao danh sach: ")
    if userInput == "":
        break
    else:
        userList.append(int(userInput))

negative_numbers = []
zero_numbers = []
positive_numbers = []
for number in userList:
    if number < 0:
        negative_numbers.append(number)
    elif number == 0:
        zero_numbers.append(number)
    else:
        positive_numbers.append(number)

mergeList = []
for i in range(0,len(negative_numbers)):
    mergeList.append(negative_numbers[i])
for i in range(0,len(zero_numbers)):
    mergeList.append(zero_numbers[i])
for i in range(0,len(positive_numbers)):
    mergeList.append(positive_numbers[i])


print(mergeList)
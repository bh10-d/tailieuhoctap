dic = {
    1: 31,
    2: [28,29],
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

userInput = input("Nhap thang: ")

for key, value in dic.items():
    if str(key) in userInput:
        print(value)
        break
dic = {
    3: 'tam giac',
    4: 'tu giac',
    5: 'ngu giac',
    6: 'luc giac',
    7: 'that giac',
    8: 'bat giac',
    9: 'cuu giac',
    10: 'thap giac'
}

userInput = int(input("Nhap so canh: "))
for key, value in dic.items():
    if userInput == key:
        print(value)
        break
    elif userInput <3 or userInput > 10:
        print("So canh vuot ra khoi pham vi la tu 3 den 10")
        break
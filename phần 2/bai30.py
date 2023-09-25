year = int(input("Nhập một năm: "))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(f"{year} là một năm nhuận.")
else:
    print(f"{year} không phải là năm nhuận.")

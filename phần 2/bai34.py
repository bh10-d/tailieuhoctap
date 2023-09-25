def decimal_to_binary(decimal):
    if decimal == 0:
        return "0b0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return "0b" + binary

decimal = int(input("Nhập một số thập phân: "))
binary = decimal_to_binary(decimal)
print(f"Số nhị phân tương ứng với {decimal} là {binary}.")

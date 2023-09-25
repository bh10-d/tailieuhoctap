def tinh_trung_binh(a, b, c):
    return (a + b + c) / 3

a = float(input("Nhập giá trị thứ nhất: "))
b = float(input("Nhập giá trị thứ hai: "))
c = float(input("Nhập giá trị thứ ba: "))

print("Giá trị trung bình của", a, ",", b, "và", c, "là:", tinh_trung_binh(a, b, c))

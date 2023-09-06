def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

area = calculate_area(a, b, c)
print(f"Diện tích của tam giác là {area:.2f}")
def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

area = calculate_area(a, b, c)
print(f"Diện tích của tam giác là {area:.2f}")

def calculate_area2(a):
    s = (a * 3) / 2
    area = (s * (s - a) ** 3) ** 0.5
    return area

# a = float(input("Nhập độ dài cạnh tam giác đều: "))

area = calculate_area2(a)
print(f"Diện tích của tam giác đều là {area:.2f}")
if calculate_area(a,b,c) == calculate_area2(a):
    print("Vậy cả 2 công thức đều cho ra kết quả như nhau")

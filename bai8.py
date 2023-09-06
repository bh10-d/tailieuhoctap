import math

def calculate_area(a):
    s = (a * 3) / 2
    area = (s * (s - a) ** 3) ** 0.5
    return area

a = float(input("Nhập độ dài cạnh tam giác đều: "))

area = calculate_area(a)
print(f"Diện tích của tam giác đều là {area:.2f}")
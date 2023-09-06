import math


r = float(input("Nhập bán kính của đáy hình trụ: "))
h = float(input("Nhập chiều cao của hình trụ: "))


volume = math.pi * r**2 * h


print(f"Thể tích của hình trụ là: {volume:.2f}")
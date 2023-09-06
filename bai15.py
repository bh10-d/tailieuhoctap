M = float(input("Nhập khối lượng của nước (gram): "))
T_0 = float(input("Nhập nhiệt độ ban đầu của nước (độ C): "))
T_1 = float(input("Nhập nhiệt độ mới của nước (độ C): "))

C = 4.186  # J/(g*C)
Q = M * C * (T_1 - T_0)
#cu phap Q:.2f cho phep lam tron den 2 so thap phan
print(f"Năng lượng cần thiết để thay đổi nhiệt độ của {M} gram nước từ {T_0} độ C đến {T_1} độ C là {Q:.2f} Joules.")
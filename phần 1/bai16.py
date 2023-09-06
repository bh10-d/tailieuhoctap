#chuong trinh xac dinh toc do di chuyen cua mot vat khi no cham dat
#nguoi dung se nhap chieu cao ma tu do vat duoc tha
from math import *
V_start = 0 #m/s
G = 9.8 #m/s^2
d = float(input("Nhập chiều cao: "))

result = sqrt(pow(V_start,2)+2*G*d)
print(f"Tốc độ là: {result:.2f}")

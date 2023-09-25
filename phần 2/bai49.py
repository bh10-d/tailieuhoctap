def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# for i in range(1,1001):
#     if la_so_nguyen_to(i):
#         print(i)
so_nguyen = int(input("Nhập một số nguyên: "))
if la_so_nguyen_to(so_nguyen):
    print(so_nguyen, "là số nguyên tố.")
else:
    print(so_nguyen, "không phải là số nguyên tố.")

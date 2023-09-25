def la_so_hoan_hao(n):
    tong_uoc_so = sum([i for i in range(1, n) if n % i == 0])
    return tong_uoc_so == n




so_nguyen_duong = int(input("Nhập một số nguyên dương: "))
if la_so_hoan_hao(so_nguyen_duong):
    print(so_nguyen_duong, "là một số hoàn hảo.")
else:
    print(so_nguyen_duong, "không phải là một số hoàn hảo.")

for i in range(1,10001):
    if la_so_hoan_hao(i):
        print(i)
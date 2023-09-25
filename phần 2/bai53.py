def danh_sach_con(lst):
    sublists = [[]]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublists.append(lst[i:j])
    return sublists

danh_sach = [1, 2, 3]
print(danh_sach_con(danh_sach))


def format_danh_sach(danh_sach):
    if len(danh_sach) == 1:
        return danh_sach[0]
    else:
        return ", ".join(danh_sach[:-1]) + " and " + danh_sach[-1]

chuoi_danh_sach = input("Nhập danh sách các từ: ")
danh_sach = chuoi_danh_sach.split(", ")
ket_qua = format_danh_sach(danh_sach)
print(ket_qua)

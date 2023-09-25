danh_sach = input("Nhap danh sach cac so: ")
danh_sach_format = danh_sach.split(",")
odd_list = []
for i in range(0,len(danh_sach_format)+1):
    if i%2!=0:
        odd_list.append(i)

print(odd_list)
import random

def tao_mat_khau_ngau_nhien():
    do_dai = random.randint(7, 10)
    mat_khau = ""
    for _ in range(do_dai):
        ky_tu = chr(random.randint(33, 126))
        mat_khau += ky_tu
    return mat_khau

mat_khau_ngau_nhien = tao_mat_khau_ngau_nhien()
print("Mật khẩu ngẫu nhiên:", mat_khau_ngau_nhien)

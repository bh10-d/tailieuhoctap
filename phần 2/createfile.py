import os
for x in range(8,55):
    f = open("bai"+str(x)+".py", "x")
    info = open("bai"+str(x)+".py", "a")
    info.write("#Chua Lam!!!")
    info.close()
    # xoa file
    # os.remove("bai"+str(x)+".py")
print("done")
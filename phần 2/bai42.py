def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Nhập một số nguyên dương: "))
print(f"Giai thừa của {n} là {factorial(n)}.")

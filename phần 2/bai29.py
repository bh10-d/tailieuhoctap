a, b, c = map(float, input("Nhập độ dài ba cạnh của tam giác (cách nhau bởi dấu cách): ").split())
print(a,b,c)

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác này là tam giác đều.")
    elif a == b or a == c or b == c:
        print("Tam giác này là tam giác cân.")
    elif a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        print("Tam giác này là tam giác vuông.")
    else:
        print("Tam giác này là tam giác thường.")
else:
    print("Đây không phải là ba cạnh của một tam giác.")
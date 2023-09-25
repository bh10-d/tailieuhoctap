def is_palindrome(string):
    string = string.lower()
    for i in range(len(string)):
        if string[i] != string[-i-1]:
            return False
    return True

string = input("Nhập một chuỗi: ")
if is_palindrome(string):
    print(f"Chuỗi '{string}' là Palindrome.")
else:
    print(f"Chuỗi '{string}' không phải là Palindrome.")

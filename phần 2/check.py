def checkEvenOdd(x):
    if x%2 == 0:
        print(x, "là số chẵn") 
    else:
        print(x, "là số lẻ")

def compareString(s1,s2):
    len1 = len(s1) 
    len2 = len(s2) 
    if len1 > len2: 
        print("chuỗi dài hơn:", s1) 
    elif len2 > len1: 
        print("Chuỗi dài hơn:",s2) 
    else:
        print("2 chuoi bang nhau")


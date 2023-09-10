

st1 = """!()-[]{};:""\,<>./?@#$%^&*_~"""

my_str = "Hello!!!, he said ---and went."


st2 = ""

for char in my_str:

    if char not in st1:

        st2 = st2 + char

# Hiển thị chuỗi sau khi loại bỏ

print(st2)
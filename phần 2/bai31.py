def caesar_cipher(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            cipher_text += shifted_char
        else:
            cipher_text += char
    return cipher_text

plain_text = input("Nhập một tin nhắn: ")
shift = int(input("Nhập số vị trí dịch chuyển: "))

cipher_text = caesar_cipher(plain_text, shift)
print(f"Tin nhắn đã được mã hóa: {cipher_text}")
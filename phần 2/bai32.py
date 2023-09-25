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

def caesar_decipher(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plain_text += shifted_char
        else:
            plain_text += char
    return plain_text

text = input("Nhập một tin nhắn: ")
shift = int(input("Nhập số ký tự dịch chuyển: "))

ciphered_text = caesar_cipher(text, shift)
print(f"Tin nhắn đã được mã hóa: {ciphered_text}")

deciphered_text = caesar_decipher(ciphered_text, shift)
print(f"Tin nhắn đã được giải mã: {deciphered_text}")

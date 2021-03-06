plain_text = input("Enter a message: ")
distance = int(input("Enter the distance value: "))

code = ""
for ch in plain_text:
    ordvalue = ord(ch)
    cipher_value = ordvalue + distance
    code += chr(cipher_value)
    print(ordvalue)
print(code)

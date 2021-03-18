# shift right 1
bits = input("Enter a string of bits: ")
new_bits = ""
length = len(bits)
new_bits = bits[length - 1]
new_bits += bits[0:length -1 ]
print(new_bits)

# shift left 1
bits = input("Enter a string of bits: ")
new_bits = ""
length = len(bits)
new_bits = bits[1:length]
new_bits += bits[0]
print(new_bits)
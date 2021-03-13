octal_string = input("Enter a string of octal digits: ")
decimal = 0
exponent = len(octal_string) - 1
for digit in octal_string:
    decimal = decimal + int(digit) * 8 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)
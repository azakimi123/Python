octal = int(input("Enter a decimal integer: "))
if octal == 0: 
    print(0)
else:
    bstring = ""
    while octal > 0:
        remainder = octal % 8
        octal = octal // 8
        bstring = str(remainder) + bstring
        print("%5d%8d%12s" % (octal, remainder, bstring))
    print("The octal representation is", bstring) 
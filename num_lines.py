# Put your code below:
file = input("Enter the input file name: ")
f1 = open(file, "r")
lines = []
count = 0
line1 = f1.readlines()
for line in line1:
    lines.append(line1[count])
    count += 1
print(f"The file has {count} lines.")

line_num = 1
while line_num != 0:
    line_num = int(input("Enter a line number [0 to quit]: "))
    if line_num == 0:
        break
    elif line_num > count:
        print(f"ERROR: line number must be less than {count}. The file has {count} lines.")
        line_num = int(input("Enter a line number [0 to quit]: "))
    print(lines[line_num - 1])
f1.close()

#loop to determine how many lines
#create list of lines

# line_num = int(input("Enter a line number [0 to quit]: "))

#conditional if statements
#quit if 0
#Error warning if line number is too high
#display line of number entered

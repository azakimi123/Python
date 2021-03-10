# Determines whether or not the contents of two text
# files are the same.  Outputs "Yes" if that is the
# case or "No" and the first two lines that differ if
# that is not the case.


# Put your code here
text1 = input("Enter the first file name: ")
text2 = input("Enter the second file name: ")

f1 = open(text1, "r")
f2 = open(text2, "r")
line1 = f1.readlines()
line2 = f2.readlines()
count = 0
output = "Yes"
for line in line1:
    if line1[count] != line2[count]:
        print('No')
        print(line1[count]) 
        print(line2[count])
        output = ""
        break
    count += 1
print(output)
f1.close()
f2.close()
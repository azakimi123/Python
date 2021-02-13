# from tabulate import _table_formats, tabulate

# getting user input and using variables to print text
# name = input('What is your name?')
# print('Hello', name)

#demonstration of splitting up a string on diffent lines
splitstring = 'this is \na test to see if\nthe string will\nprint on different\nlines'
print(splitstring)

#tab is \t
tabstring = 'this\tis\ta\ttabbed'
print(tabstring)

#tripple double quotes allows you to use quotes in strings and line breaks
print("""You don't have to 
do line breaks 
when using tripple
quotes""")


# from tabulate import tabulate

# table = [["Sun",696000,1989100000],["Earth",6371,5973.6],
# ...          ["Moon",1737,73.5],["Mars",3390,641.85]]
# print(tabulate(table))

# print("%4s%18s%10s%16s" % \
#   ("Year", "Starting Balance", "Interest", "Ending Balance"))

# print("%7s%20s%15s" % \
#    ("Morning", "Afternoon", "Night"))

# for meal in range(3):
#   print("%7s%16s%17s" % \
#     ("Breakfast", "Lunch", "Dinner"))


# Put your code here:
import math 
side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

# check to see if triangle is a right triangle
if (math.pow(side1,2)) + (math.pow(side2,2)) == (math.pow(side3,2)):
    print("The triangle is a right triangle.")
elif (side2 ** 2) + (side3 ** 2) == (side1 ** 2):
    print("The triangle is a right triangle.")
elif (side3 ** 2) + (side1 ** 2) == (side2 ** 2):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
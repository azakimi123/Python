# example of a while loop exiting on condition of user input "enter"
# while True:
#     i = input("Enter text (or Enter to quit): ")
#     if not i:
#         break
#     print("Your input:", i)
# print("While loop has exited")

theSum = 0.0
amount = 0
data = input("Enter a number or press enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    data = input("Enter a number or press enter to quit: ")
    amount += 1
    average = theSum/amount
    if data == "":
        break
        
print("The sum is", theSum)
print("The average is", average)


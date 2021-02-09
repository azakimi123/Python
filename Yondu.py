'''
Project Name: Yondu
Author: Aaron Zakimi
Due Date: 02/05/2021
Course: CS1400

This function takes in user input for number of Reavers and units collected.
The function then calculates the number of units the captain (Yondu), Peter, and the rest of the crew recieve.
The leftovers if the units can't be divided evently are put into a reavers benevolent fund (RBF).  
'''

def main():
    '''
    Program starts here.
    '''
    import math
    try:
        # (1) replace pass with your code
        reavers = int(input("Enter how many reavers: "))
        units = int(input("Enter how many units: "))
    except ValueError:
        print("Enter postive integers for reavers and units.")
        return
    
    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return
    
    # (2) replace pass with your code
    crew_members = reavers - 2
    lotus_money = (crew_members * 3)
    working_units = units - lotus_money
    yondu = math.floor(working_units * .13)
    working_units = working_units - yondu
    peter = math.floor(working_units * .11)
    working_units = working_units - peter
    crew_share = working_units // reavers
    yondu = yondu + crew_share
    peter = peter + crew_share
    RBF = working_units % reavers
    print("Yondu's share: ", yondu)
    print("Peter's share: ", peter)
    print("Crew: ", crew_share)
    print("RBF: ", RBF)
    

if __name__ == "__main__":
    main()

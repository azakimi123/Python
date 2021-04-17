'''
Project Name: Rabbits, Rabbits, Rabbits
Author: Aaron Zakimi
Due Date: 03/13/2021
Course: CS1400

This is the first time that I am writing to a CSV file. Learning about working with files in python is interesting.
'''
# Function containing program
def main():
  # CSV module from python
    import csv
  # Tabulate hels to format data
    from tabulate import tabulate
    '''
    Program starts here.
    '''
    # Inputs for program
    month = 1
    adults = 1
    babies = 0
    total = 1
    num_cages = 500

    # Initializes empty list to insert table data
    table = []

    # While loop runs until total reaches the number of cages available
    while total <= num_cages:
      # Adds new row to data set table - using a list
      table.append([month,adults,babies,total])
      month += 1
      babies = adults
      adults = total
      total = (adults + babies)

    # Prints output data
    print(tabulate(table, headers=["Month","Adult", "Babies", "Total"], numalign="right"))
    print(f"\nCages will run out in month {month}\nPress any key to continue...")
    
    # Using context manager "with" and "as" to allow file to close after indentation stops
    with open('rabbits.csv', 'w') as f:
      f.write(tabulate(table, headers=["Month","Adult", "Babies", "Total"], numalign="right"))
      f.write(f"\nCages will run out in month {month}\nPress any key to continue...")
    
# Calls the main() function
if __name__ == "__main__":
    main()
    

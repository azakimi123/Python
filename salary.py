# Put your code here
import math
starting_salary = int(input("Enter the starting salary: "))
annual_increase = int(input("Enter the annual increase: "))
years = int(input("Enter the number of years: "))

print("%4s%10s" %  
    ("Year", "Salary"))
print("===============")


for year in range(years):
    year = year + 1
    if year == 1:
        salary = starting_salary
        print("%4s%10s" % 
        ((year), format(salary,'.2f')))
    else:
        salary = starting_salary * (annual_increase/100 + 1)
        starting_salary = salary
        print("%4s%10s" % 
        ((year + 1), format(salary,'.2f')))
    # if year < 1:
    #     salary = starting_salary
    #     print("%4s%10s" % 
    #     ((year + 1), format(salary,'.2f')))
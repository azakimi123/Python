# import statistics to help with calculations
import statistics
#import csv to help with reading csv files
import csv
from csv import reader
import numpy as np
import pandas as pd
# df = pd.read_csv('BLS_report.csv', skiprows=12)

# test = []

# row = df.iterrows()
# for index, row in df.head(n=2).iterrows():
#      test.append(row['Jan'])
     
# print(test)


# 1. need to parse the correct data from csv file
# 2. create a dictionary of the correct data
# 3. create a function to get the total number of jobs

rows = []
with open('BLS_report.csv') as f:
  reader = csv.DictReader(f)

  for row in reader:
    print(row['Employment'])
  # data = reader(f)
  # found_section = False
  # header = None

  # for row in data:
  #   if not found_section:
  #     if len(row) > 0:
  #       if row[0] == "Year":
  #         header = next(data)
  #         # header = next(data)
  #         found_section = True
  #   else:
  #     break

  # print(header)

  # for row in data:
  #   # if row[0] == "Year":
  #   #   print(row)
  #   if row[0] == '1961':
  #     for num in row[1:]:
  #       rows.append(num)
  
  # print(rows)
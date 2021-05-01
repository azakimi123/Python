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


rows = []
with open('BLS_report.csv') as f:
  data = reader(f)

  for row in data:
    if row[0] == "Year":
      print(row)
    if row[0] == '1961':
      print(row)
  
  # print(rows)
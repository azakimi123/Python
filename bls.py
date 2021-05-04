# import statistics to help with calculations
import statistics
#import csv to help with reading csv files
import csv
from csv import reader
import numpy as np
import pandas as pd




# 1. need to parse the correct data from csv file
# 2. create a dictionary of the correct data
# 3. create a function to get the total number of jobs

demo_jobs = []
rep_jobs= []
with open('BLS_report.csv') as f:
  reader = csv.reader(f)
  
  for row in reader:
    if row[0] == 'Year':
      header = row
      # writing to csv file 
      with open('BLS_data.csv', 'w') as csvfile: 
          # creating a csv writer object 
          csvwriter = csv.writer(csvfile) 
              
          # writing the fields 
          csvwriter.writerow(header) 
  
          for rows in reader:
            # writing the data rows 
            csvwriter.writerow(rows)
            # print(rows)

with open('BLS_data.csv') as f:
  data = csv.DictReader(f)

  #Democratic 1
  for row in data:
    if row['Year'] == '1961':
      begin = int(row['Jan'])
    if row['Year'] == '1969':
      end = int(row['Jan'])
      demo_jobs.append(end - begin)

  # Republic 1
    if row['Year'] == '1969':
      begin = int(row['Feb'])
    if row['Year'] == '1977':
      end = int(row['Jan'])
      rep_jobs.append(end - begin)

  #Democratic 2
    if row['Year'] == '1977':
      begin = int(row['Feb'])
    if row['Year'] == '1981':
      end = int(row['Jan'])
      demo_jobs.append(end - begin)

  # Republic 2
    if row['Year'] == '1981':
      begin = int(row['Feb'])
    if row['Year'] == '1993':
      end = int(row['Jan'])
      rep_jobs.append(end - begin)
  
  #Democratic 3
    if row['Year'] == '1993':
      begin = int(row['Feb'])
    if row['Year'] == '2001':
      end = int(row['Jan'])
      demo_jobs.append(end - begin)

  # Republic 3
    if row['Year'] == '2001':
      begin = int(row['Feb'])
    if row['Year'] == '2009':
      end = int(row['Jan'])
      rep_jobs.append(end - begin)

  #Democratic 3
    if row['Year'] == '2009':
      begin = int(row['Feb'])
    if row['Year'] == '2012':
      end = int(row['Dec'])
      demo_jobs.append(end - begin)





  print('Democrats: ', sum(demo_jobs))
  print('Republicans: ', sum(rep_jobs))



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
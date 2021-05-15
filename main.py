
def Main():
  # import statistics to help with calculations
  import statistics
  #import csv to help with reading csv files
  import csv
  from csv import reader
  import numpy as np
  import pandas as pd

  # imports to help with graph
  from datetime import datetime
  import matplotlib.pyplot as plt
  from matplotlib import dates as mpl_dates




  # Basic steps I need to complete
  # 1. need to parse the correct data from csv file
  # 2. create a dictionary of the correct data
  # 3. create a function to get the total number of jobs

  # List to store data for outputs
  demo_jobs = []
  demo_plot = []
  demo_year_plot = []
  rep_jobs= []
  rep_plot = []
  rep_year_plot = []

  # Creates new csv file to extract data
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


  # Opens new csv file with the data
  with open('BLS_data.csv') as f:
    data = csv.DictReader(f)

    #Democratic 1
    for row in data:
      if row['Year'] == '1961':
        begin = int(row['Jan'])
      if row['Year'] == '1969':
        end = int(row['Jan'])
        demo_jobs.append(end - begin)
        demo_plot.append(sum(demo_jobs))
        demo_year_plot.append(datetime(int(row['Year']), 1, 1))

    # Republic 1
      if row['Year'] == '1969':
        begin = int(row['Feb'])
      if row['Year'] == '1977':
        end = int(row['Jan'])
        rep_jobs.append(end - begin)
        rep_plot.append(sum(rep_jobs))
        rep_year_plot.append(datetime(int(row['Year']), 1, 1))

    #Democratic 2
      if row['Year'] == '1977':
        begin = int(row['Feb'])
      if row['Year'] == '1981':
        end = int(row['Jan'])
        demo_jobs.append(end - begin)
        demo_plot.append(sum(demo_jobs))
        demo_year_plot.append(datetime(int(row['Year']), 1, 1))

    # Republic 2
      if row['Year'] == '1981':
        begin = int(row['Feb'])
      if row['Year'] == '1993':
        end = int(row['Jan'])
        rep_jobs.append(end - begin)
        rep_plot.append(sum(rep_jobs))
        rep_year_plot.append(datetime(int(row['Year']), 1, 1))
    
    #Democratic 3
      if row['Year'] == '1993':
        begin = int(row['Feb'])
      if row['Year'] == '2001':
        end = int(row['Jan'])
        demo_jobs.append(end - begin)
        demo_plot.append(sum(demo_jobs))
        demo_year_plot.append(datetime(int(row['Year']), 1, 1))

    # Republic 3
      if row['Year'] == '2001':
        begin = int(row['Feb'])
      if row['Year'] == '2009':
        end = int(row['Jan'])
        rep_jobs.append(end - begin)
        rep_plot.append(sum(rep_jobs))
        rep_year_plot.append(datetime(int(row['Year']), 1, 1))

    #Democratic 4
      if row['Year'] == '2009':
        begin = int(row['Feb'])
      if row['Year'] == '2012':
        end = int(row['Dec'])
        demo_jobs.append(end - begin)
        demo_plot.append(sum(demo_jobs))
        rep_plot.append(sum(rep_jobs))
        demo_year_plot.append(datetime(int(row['Year']), 12, 1))
        rep_year_plot.append(datetime(int(row['Year']), 12, 1))




    # Total results of jobs created
    print('Democrats: ', sum(demo_jobs))
    print('Republicans: ', sum(rep_jobs))

    democrat = np.array(demo_plot)
    republican = np.array(rep_plot)
    demo_years = np.array(demo_year_plot)
    rep_years = np.array(rep_year_plot)

    plt.plot(demo_years, democrat, color='blue', marker="o", linestyle='dashed', label='Democratic Jobs')
    plt.plot(rep_years, republican, color='red', marker="o", linestyle='dashed', label='Republican Jobs')

    plt.legend()
    plt.show()

Main()

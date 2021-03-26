'''
Project Name: Stocks Data
Author: Aaron Zakimi
Due Date: 03/25/2021
Course: CS1400

I haven't worked with importing data from a CSV file before.  This was interesting to learn how to extract data from another file to use in our code. 
'''

# import statistics to help with calculations
import statistics

def main():
  # # Initializes empty list to insert table data
  apple = []
  micro = []
  IBM = []
  total = []
  total_d = []


  apple_date = []
  micro_date = []
  IBM_date = []

  #to check to see if I imported all of the data
  apple_ct = 0
  micro_ct = 0
  IBM_ct = 0

  # f = open("stocks_data.csv", "r")
  # print(f.readline())
  # f.close()

  #import csv to help with reading csv files
  import csv

  with open('stocks_data.csv') as f:
    myreader = csv.reader(f)
    # datafile = open('stocks_data.csv', 'r')
    # myreader = csv.reader(datafile)

    #for loop to build the lists of data
    for row in myreader:
      if row[0] == "AAPL":
        apple.append(float(row[2]))
        apple_date.append((row[1]))
        apple_ct += 1
      elif row[0] == "IBM":
        IBM.append(float(row[2]))
        IBM_date.append((row[1]))
        IBM_ct += 1
      elif row[0] == "MSFT":
        micro.append(float(row[2]))
        micro_date.append((row[1]))
        micro_ct += 1
  
    apple_max = max(apple)  
    apple_min = min(apple)  
    IBM_max = max(IBM)  
    IBM_min= min(IBM)  
    micro_max = max(micro)  
    micro_min = min(micro)  

    #functions to calculate requested outputs
    def apple_calculations():
      apple_max = max(apple)
      apple_max_index = apple.index(apple_max)
      ap_max_d = apple_date[apple_max_index]
      apple_min = min(apple)
      apple_min_index = apple.index(apple_min)
      ap_min_d = apple_date[apple_min_index]
      ap_mean = statistics.fmean(apple)
      total.extend([apple_max, apple_min])
      total_d.extend([ap_max_d, ap_min_d])


      with open('stock_summary.txt', 'w') as f:
        f.write(
        f"""        AAPL
        ------
        MAX:  {apple_max} {ap_max_d}
        MIN:  {apple_min} {ap_min_d}
        MEAN: {ap_mean}""")

      print("AAPL")
      print("------")
      print("MAX: ", apple_max, ap_max_d)
      print("MIN: ", apple_min, ap_min_d)
      print("MEAN: ", ap_mean)

    def micro_calculations():
      micro_max = max(micro)
      micro_max_index = micro.index(micro_max)
      mi_max_d = micro_date[micro_max_index]
      micro_min = min(micro)
      micro_min_index = micro.index(micro_min)
      mi_min_d = micro_date[micro_min_index]
      mi_mean = statistics.fmean(micro)
      total.extend([micro_max, micro_min])
      total_d.extend([mi_max_d, mi_min_d])

      with open('stock_summary.txt', 'a') as f:
        f.write(
        f"""        
        
        MSFT
        ------
        MAX:  {micro_max} {mi_max_d}
        MIN:  {micro_min} {mi_min_d}
        MEAN: {mi_mean}""")

      print("MSFT")
      print("------")
      print("MAX: ", micro_max, mi_max_d)
      print("MIN: ", micro_min, mi_min_d)
      print("MEAN: ", mi_mean)
      

    def IBM_calculations():
      IBM_max = max(IBM)
      IBM_max_index = IBM.index(IBM_max)
      IBM_max_d = IBM_date[IBM_max_index]
      IBM_min = min(IBM)
      IBM_min_index = IBM.index(IBM_min)
      IBM_min_d = IBM_date[IBM_min_index]
      IBM_mean = statistics.fmean(IBM)
      total.extend([IBM_max, IBM_min])
      total_d.extend([IBM_max_d, IBM_min_d])

      with open('stock_summary.txt', 'a') as f:
        f.write(
        f"""        
        
        IBM
        ------
        MAX:  {IBM_max} {IBM_max_d}
        MIN:  {IBM_min} {IBM_min_d}
        MEAN: {IBM_mean}""")

      print("IBM")
      print("------")
      print("MAX: ", IBM_max, IBM_max_d)
      print("MIN: ", IBM_min, IBM_min_d)
      print("MEAN: ", IBM_mean)

      symbol_max = ""
      symbol_min = ""

  def overall():
      total_max = max(total)
      total_max_index = total.index(total_max)
      to__max_d = total_d[total_max_index]
      total_min = min(total)
      total_min_index = total.index(total_min)
      to_min_d = total_d[total_min_index]
      

      if total_max == apple_max:
        symbol_max = "AAPL"
        
      elif total_max == micro_max:
        symbol_max = "MSFT"
        
      elif total_max == IBM_max:
        symbol_max = "IBM"

      if total_min == apple_min:
        symbol_min = "AAPL"
        
      elif total_min == micro_min:
        symbol_min = "MSFT"
        
      elif total_min == IBM_min:
        symbol_min = "IBM"

      with open('stock_summary.txt', 'a') as f:
        f.write(
        f"""        
        
        {symbol_max} {total_max} {to__max_d}
        {symbol_min} {total_min} {to_min_d}""")
        

      print(symbol_max, total_max, to__max_d)
      print(symbol_min, total_min, to_min_d)

  apple_calculations()
  print()
  IBM_calculations()
  print()
  micro_calculations()
  print()
  overall()

main()

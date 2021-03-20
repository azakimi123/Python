binary = {   
  "0":"0000",
   "1":"0001",
   "2":"0010",
   "3":"0011",
   "4":"0100",
   "5":"0101",
   "6":"0110",    
   "7":"0111",
   "8":"1000",
   "9":"1001",
   "10":"1010",
   "11":"1011",
   "12":"1100",
   "13":"1101",
   "14":"1110",
   "15":"1111",
   "16":"10000"}

hex = {   
  "0":"0",
   "1":"1",
   "2":"2",
   "3":"3",
   "4":"4",
   "5":"5",
   "6":"6",    
   "7":"7",
   "8":"8",
   "9":"9",
   "10":"A"}

decimal = {   
  "0":"0",
   "1":"1",
   "2":"2",
   "3":"3",
   "4":"4",
   "5":"5",
   "6":"6",    
   "7":"7",
   "8":"8",
   "9":"9",
   "10":"10"}

octal = {   
  "0":"00",
   "1":"01",
   "2":"02",
   "3":"03",
   "4":"04",
   "5":"05",
   "6":"06",    
   "7":"07",
   "8":"10",
   "9":"11",
   "10":"12"}


def convert(number, table):
  """builds and returns the base two representation of number."""
  converter = ""
  if table == 10:
    converter = decimal
  elif table == 16:
    converter = hex
  elif table == 2:
    converter = binary
  elif table == 8:
    converter = octal
  else:
    print("choose another base")
  
  output = converter.get(str(number))
  # if number > 16:
  #   num = number - 16
  #   num2 = number - num
  # # x = table.keys()
  # output = int(table.get(str(num))) + int(table.get(str(num2)))
  print(output)

convert(10,2)
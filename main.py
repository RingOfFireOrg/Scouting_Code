import csv

number = input('Enter number to find: ')

csv_file = csv.reader(open('Scout Data.csv', "r"), delimiter=",")
var1 = 0
teleHigh = 0
teleLow = 0
autoHigh = 0
autoLow = 0
counter = 0
countah = []
countal = []
countth = []
counttl = []
climbtime= []

for row in csv_file:
  if number == row[7]:
    print(row[7]," ",row[5],row[10], row[11],row[14],row[15],row[20])
    try:
      countah.append(int(row[10]))
      countal.append(int(row[11]))
      countth.append(int(row[14]))
      counttl.append(int(row[15]))
      climbtime.append(int(row[20]))

    except:
      pass



print("Team Number: ", number)

def averager(list):
  var2 = 0
  for i in list:
    var2 = var2 + i
  return var2/len(list)

print()
#print(countah, countal, countth,counttl)
if len(countah)==0: #show if no entrys are recorded
  print("autoHigh: ", N/A)
else:
  print("autoHigh: ", averager(countah))
if len(countal)==0: #show if no entrys are recorded
  print("autoLow: ","N/A")
else:
  print("autoLow: ",averager(countal)) 
if len(countth)==0: #show if no entrys are recorded
  print("telehigh: ","N/A")
else:
  print("telehigh: ",averager(countth))
if len(countal)==0: #show if no entrys are recorded
  print("teleLow: ","N/A")
else:
  print("telelow: ",averager(counttl)) 
print("Climb: ", averager(climbtime), "seconds")
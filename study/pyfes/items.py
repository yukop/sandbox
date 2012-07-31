import csv
with open('items.csv', 'rb') as f:
  reader = csv.reader(f)
  itemNames = []
  for row in reader:
    itemName = row[1]
    itemNames.append(itemName) 
    itemDict = {}
    for itemName in itemNames:
      if itemName in itemDict:
        itemDict[itemName] += 1
      else:
        itemDict[itemName] = 1      
  print itemDict
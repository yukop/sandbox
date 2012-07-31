import csv
with open('items.csv', 'rb') as f:
  reader = csv.reader(f)
  itemDict = {}
  for row in reader:
    itemName = row[1].decode('cp932')
    if itemDict.has_key(itemName):
      itemDict[itemName] += 1
    else:
      itemDict[itemName] = 1      
  
  print itemDict
  
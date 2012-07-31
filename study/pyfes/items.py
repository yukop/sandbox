# coding: utf-8

def makeDictFromCsv(filename):
  import csv
  with open(filename, 'rb') as f:
    reader = csv.reader(f)
    itemDict = {}
    for row in reader:
      itemName = row[1].decode('cp932')
      if itemDict.has_key(itemName):
        itemDict[itemName] += 1
      else:
        itemDict[itemName] = 1
  return itemDict

def printResult(dict):
  for k, v in dict.items():
    print k, str(v) + u'個'

printResult(makeDictFromCsv('items.csv'))
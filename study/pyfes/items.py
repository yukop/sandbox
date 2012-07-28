import csv
with open('items.csv', 'rb') as f:
  reader = csv.reader(f)
  items = []
  for row in reader:
    items.append(row[1])
  print items
    
import csv
import math

f = open('data.csv')
csv_f = csv.reader(f)

D = []

header = next(csv_f)
for row in csv_f:
    if math.isnan(float(row[8])) == False:
        D.append(10**((float(row[8]) + 5)//5))

D.sort(reverse = True)

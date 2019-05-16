import csv
import math

f = open('data.csv')
csv_f = csv.reader(f)

ID = int(input("Star ID X: "))

x = []
y = []
z = []

soln = []
rows = []

x1 = 0
y1 = 0
z1 = 0

header = next(csv_f)

distance = []

for row in csv_f:
    rows.append(row)
    row [1] = float(row[1])
    row [2] = float(row[2])
    row [8] = float(row[8])
    x.append(row[8]*math.sin(row[1])*math.cos(row[2]))
    y.append(row[8]*math.sin(row[1])*math.sin(row[2]))
    z.append(row[8]*math.cos(row[1]))
    # print(x)
    if(int(row[0]) == ID):
        x1 = x
        y1 = y
        z1 = z

for row in csv_f:
    X = (x1 - x[row])**2
    Y = (y1 - y[row])**2
    Z = (z1 - z[row])**2
    distance.append((math.sqrt(X+Y+Z)))
    # print(math.sqrt(X+Y+Z))

distance.sort()
print(distance)
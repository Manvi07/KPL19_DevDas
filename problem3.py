import csv
import math

def Problem3():
    f = open('data.csv')
    csv_f = csv.reader(f)

    D = []

    header = next(csv_f)
    for row in csv_f:
        if math.isnan(float(row[8])) == False:
            D.append( (row[0], 10**((float(row[8]) + 5)/5) ) )

    #D.sort(reverse = True)
    Starlist = sorted(D, key=lambda x: x[1])

    return Starlist[:5]
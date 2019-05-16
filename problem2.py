import pandas as pd
#import matplotlib.pyplot as plt
import math



def checkOut(long, lat, d, distSun, rad, thicc):
    dis = 10**((d + 5)/5)
    x = dis*math.cos(math.radians(lat) )
    xx = x*math.cos(math.radians(180-long)) + distSun
    y = dis*math.sin(math.radians(lat) )
    xy = x*math.sin(math.radians(180-long))

    if (xy**2 + xx**2 > rad) or (abs(y) > thicc):
        return True
    return False


def Problem2():
    df = pd.read_csv('data.csv')
    distSun = 8122
    thicc = 300
    rad = 15000
    WaveRatio = []
    distMod = []
    extra = []
    for index, row in df.iterrows():
        if checkOut(row['Column 4'], row['Column 5'], row['Column 9'], distSun, rad, thicc):
            WaveRatio.append(1+row['Column 7'])
            distMod.append(row['Column 9'])
        else:
            extra.append(row['Column 1'])

    # plt.show()
    return extra
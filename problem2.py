import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv('data.csv')


distSun = 8122
thicc = 300
rad = 15000

def checkOut(long, lat, d):
    dis = 10**((d + 5)/5)
    x = dis*math.cos(math.radians(lat) )
    xx = x*math.cos(math.radians(180-long)) + distSun
    y = dis*math.sin(math.radians(lat) )
    xy = x*math.sin(math.radians(180-long))

    if (xy**2 + xx**2 > rad) or (abs(y) > thicc):
        return True
    return False

WaveRatio = []
distMod = []
extra = []

for index, row in df.iterrows():
    if checkOut(row['Column 4'], row['Column 5'], row['Column 9']):
        WaveRatio.append(1+row['Column 7'])
        distMod.append(row['Column 9'])
    else:
        extra.append(row['Column 1'])
       
plt.xlabel('distance modulus')
plt.ylabel('ratio of app vs real wavelength')
plt.scatter(distMod, WaveRatio)
# plt.show()
plt.savefig("plot.png")
print('ID of intragalactic sources',extra)
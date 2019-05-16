import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

WaveRatio = 1 + np.array(df['Column 7'])
distMod = np.array(df['Column 9'])

plt.scatter(distMod, WaveRatio)
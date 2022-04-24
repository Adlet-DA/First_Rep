import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('dz (1).csv', sep=";")
frame = pd.DataFrame(df)

print(frame['CTR, %'])
clics = frame['Количество кликов']
print(clics)
a = np.array(clics)
print(a)
shows = frame['Количетсво показов']
b = np.array(shows)
print(b)
plt.plot(b, a)
plt.show()

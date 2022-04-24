import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Задача 1")
data1 = pd.Series(np.random.randn(5).cumsum(), index=np.arange(0, 5, 1))
print(data1)
data1.plot(kind='bar', title='Гистограмма 5 столбцов', color='k')  # черный
plt.show()

print("Задача 2")
# data2 = np.random.randn(10, 4).cumsum(0)
# df = pd.DataFrame(data2, columns=['First','Second','Third','Fourth'])
# print(df)
# df.plot(subplots=True, title='4 ломанных линии', sharex=True, sharey=True, figsize=(10,10), legend=True, sort_columns=False)
# df.plot(title='4 ломанных линии', sharex=True, sharey=True, figsize=(10,10), legend=True, style='o--')
# plt.show()
fig, axes = plt.subplots(3, 1)
data3 = pd.Series(np.random.rand(10), index=list('zxcvbnmasd'))
print(data3)
data3.plot(ax=axes[0], color='red', alpha=0.9, title='График 1', figsize=(10, 10), legend=True)
data3.plot(ax=axes[1], color='blue', alpha=0.3, style='o--', sharex=True, sharey=True, title='Синяя прерывистая')
data3.plot.barh(ax=axes[2])
plt.show()

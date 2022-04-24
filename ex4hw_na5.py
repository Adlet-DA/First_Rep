import numpy as np
import matplotlib.pyplot as plt
from docx import Document
import pandas as pd

print('Домашнее задание №4. Тайранов А.')
print('Задача №1')
x = np.linspace(-100, 100,50)
y = [1/i for i in x]

plt.title("Зависимость y=1/x")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

plt.plot(x, y, color='red', linestyle='dashdot', alpha=0.5, linewidth=3)
plt.show()
print('График был показан', '\n')

print('Задача №2')
filename = 'Таблица для дз.docx'
document = Document(filename)
tables = document.tables
df_tables = []
for table in tables:
    df = [['' for i in range(len(table.columns))] for j in range(len(table.rows))]
    for i, row in enumerate(table.rows):
        for j, cell in enumerate(row.cells):
            if cell.text:
                df[i][j] = cell.text
    df_tables.append(pd.DataFrame(df))
offices = df_tables[0]

offices_1 = offices.drop(labels=[0], axis=0)

offices_2 = offices_1.rename(columns={0: "Office",
                                      1: "Stuff",
                                      2: "Number"})
print('"Таблица из файла "Таблица для дз.docx""', '\n')
print(offices_2, '\n')
offices_3 = offices_2['Number'].apply(lambda x: x.replace('№', ''))

offices_2['Number'] = offices_3
print('"Таблица с удаленным знаком №"', '\n')
print(offices_2, '\n')
offices_4 = offices_2['Number'].astype(np.int16)
offices_2['Number'] = offices_4
offices_5= offices_2['Stuff'].astype(np.int16)
offices_2['Stuff']=offices_5
print('"Таблица данных, где номер офиса меньше 350, а сотрудников меньше 700"', '\n')
#print(offices_2[offices_2.Number < 350][offices_2.Stuff < 700])
ixcam = offices_2.query('Number < 350 & Stuff < 700')
print(ixcam)

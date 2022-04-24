import glob
import tabula

print('Одна таблица на странице')
pdf_path = 'https://sedl.org/afterschool/toolkits/science/pdf/ast_sci_data_tables_sample.pdf'
dfs1 = tabula.read_pdf(pdf_path, pages='1')
print(len(dfs1))
print(dfs1)
dfs1[0].to_csv('первая таблица')

print()
print('Две таблицы на странице')
dfs2 = tabula.read_pdf(pdf_path, pages='2')
print(len(dfs2))
print(dfs2)
for i in range(len(dfs2)):
    dfs2[i].to_csv(f"таблица №{i+1} страница 2.csv")

print()
print('Таблицы на всех страницах')
dfs3 = tabula.read_pdf(pdf_path, pages='all')
print(len(dfs3))
print(dfs3)
for i in range(len(dfs3)):
    dfs3[i].to_csv(f"таблица №{i+1} со всех страниц.csv")


import pandas as pd

s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
print(s)
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11198846, 1303171835, 207847528]}
df = pd.DataFrame(data)
print(df)
print(s['c'])
print(s.c)
print(df[0:1])
print("")
print(df['Populacja'])
print(df.iloc[0, 0])
print(df.loc[0, 'Kraj'])
print(df.at[0, 'Kraj'])
print(df.loc[0])
print('kraj: ' + df.Kraj)
print(df.sample())
print(df.sample(2))
print("")
print(df.head())
print(df.tail(1))
print(df.describe())
print(df.T)
print(df.sample(frac=0.5))
print(df.sample(n=10, replace=True))
print("")
print(s[(s > 9)])
print(s.where(s > 10))
print(s.where(s > 10, 'za duże'))
seria = s.copy()
#seria.where(seria > 10, 'za duże', inplace=True)
print("-------------------------")
print(seria)
print(s[-(s > 10)])
print(s[(s < 13) & (s > 8)])
print(df[df['Populacja'] > 1200000000])
print(df[(df.Populacja > 1000000) & (df.index.isin([0, 2]))])
print("-------------------------")
szukaj = ['Belgia', 'Brasilia']
print(df.isin(szukaj))
s['e'] = 15
print(s.e)
s['f'] = 16
print(s)
df.loc[3] = 'dodane'
print(df)
df.loc[4] = ['Polska', 'Warszawa', 38675467]
print(df)
new_df = df.drop([3])
print(new_df)
df.drop([3], inplace=True)
#df.drop('Kraj', axis=1, inplace=True)
print(df)
df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
print(df)
print("-------------------------")
print(df.sort_values('Kraj'))
grouped = df.groupby(['Kontynent'])
print(grouped.get_group('Europa'))
print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))
print("-------------------------")
iris = pd.read_csv("iris.data")
excel_file = pd.ExcelFile("iris.xlsx")
excel = pd.read_excel(excel_file, header=None)
print(iris)
print(excel)

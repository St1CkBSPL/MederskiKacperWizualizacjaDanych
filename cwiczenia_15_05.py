import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#ts = pd.Series(np.random.randn(1000))
#ts = ts.cumsum()
#print(ts)
#ts.plot()
#plt.show()

#ZADANIE 1

data = pd.read_excel('imiona.xlsx')

grouped_data = data.groupby('Rok').sum()

plt.plot(grouped_data.index, grouped_data['Liczba'], marker='o', linestyle='-')

plt.title('Liczba urodzonych dzieci dla każdego roku')
plt.xlabel('Rok')
plt.ylabel('Liczba urodzonych dzieci')
plt.xticks(data['Rok'].unique())
plt.xticks(rotation=90)

plt.show()

#ZADANIE 2
grupa = data.groupby(['Plec']).agg({'Liczba':["sum"]})
wykres = grupa.plot.bar()
wykres.set_ylabel("Ilosc")
wykres.set_xlabel('Plec')
wykres.tick_params(axis='x', labelrotation=0)
wykres.legend()
wykres.set_title('Ilosc dzieci wykres slupkowy')
plt.savefig('wykres.png')
plt.show()

#ZADANIE 3
lata = data[data['Rok'] >= data['Rok'].max() - 4]

grupa_dzieci = lata.groupby('Plec').sum()

urodzenia = grupa_dzieci['Liczba'].sum()
grupa_dzieci['Procent'] = (grupa_dzieci['Liczba'] / urodzenia) * 100

plt.figure(figsize=(8, 6))
plt.pie(grupa_dzieci['Procent'], labels=grupa_dzieci.index, autopct='%1.1f%%', startangle=140)

plt.title('Procentowy udział urodzeń chłopców i dziewczynek\n w ostatnich 5 latach')

plt.axis('equal')
plt.show()

#ZADANIE 4

data = pd.read_csv('zamowienia.csv', header=0, sep=";",decimal=',')

orders_by_seller = data.groupby('Sprzedawca').size().reset_index(name='Liczba zamówień')

plt.bar(orders_by_seller['Sprzedawca'], orders_by_seller['Utarg'], color='skyblue')

plt.title('Ilość złożonych zamówień przez poszczególnych sprzedawców')
plt.xlabel('Sprzedawca')
plt.ylabel('Liczba zamówień')

plt.xticks(rotation=45, ha='right')

plt.savefig('wykres_4.png')
plt.show()


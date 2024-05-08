import pandas as pd
"""
# Wczytanie danych z pliku xlsx
#df = pd.read_excel('imiona.xlsx')

#ZADANIE 2

# Wyświetlenie rekordów, gdzie liczba nadanych imion była większa niż 1000 w danym roku
wynik = df[df['Liczba'] > 1000]

#print(wynik)

# Tylko moje imie
wynik_imie = df[df['Imie'] == 'KACPER']

#print(wynik_imie)

#suma dzieci
suma_dzieci = df['Liczba'].sum()

#print("Suma wszystkich urodzonych dzieci w całym okresie:", suma_dzieci)

#suma dzieci od 2000 do 2005
dzieci_2000_2005 = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]

suma_dzieci_2000_2005 = dzieci_2000_2005['Liczba'].sum()

#print("Suma dzieci urodzonych w latach 2000-2005:", suma_dzieci_2000_2005)

#suma chlopakow i dziewczynek
dzieci_chlopaki = df[df['Plec'] == 'M']
dzieci_dziewczyny = df[df['Plec'] == 'K']

suma_chlopaki = dzieci_chlopaki['Liczba'].sum()
suma_dziewczyny = dzieci_dziewczyny['Liczba'].sum()

#print("Suma chlopakow: ", suma_chlopaki)
#print("Suma dziewczyny: ", suma_dziewczyny)

#najczesciej brane imiona meskie i zenskie
dzieci_chlopaki = df[df['Plec'] == 'M']
dzieci_dziewczyny = df[df['Plec'] == 'K']

najpopularniejsze_imie = []

for rok in range(2000, 2018):
    najpopularniejsze_dziewczynka = dzieci_dziewczyny[dzieci_dziewczyny['Rok'] == rok]['Imie'].value_counts().idxmax()
    najpopularniejsze_chlopiec = dzieci_chlopaki[dzieci_chlopaki['Rok'] == rok]['Imie'].value_counts().idxmax()
    najpopularniejsze_imie.append({'Rok': rok, 'K': najpopularniejsze_dziewczynka, 'M': najpopularniejsze_chlopiec})

# Konwersja listy wyników do ramki danych
najpopularniejsze_imie_df = pd.DataFrame(najpopularniejsze_imie)

#print(najpopularniejsze_imie_df)

#najpopularniejsze caly okres
dzieci_chlopaki = df[df['Plec'] == 'M']
dzieci_dziewczyny = df[df['Plec'] == 'K']

najpopularniejsze_dziewczynki = dzieci_dziewczyny.groupby('Imie')['Liczba'].sum().idxmax()
najpopularniejsze_chlopcy = dzieci_chlopaki.groupby('Imie')['Liczba'].sum().idxmax()

#print("Najbardziej popularne imię dziewczynki:", najpopularniejsze_dziewczynki)
#print("Najbardziej popularne imię chłopca:", najpopularniejsze_chlopcy)
"""
#ZADANIE 3
#unikalne nazwiska
df = pd.read_csv('zamowienia.csv', header=0, sep=";",decimal=',')

unikalne_nazwiska = df['Sprzedawca'].unique()

#print("Unikalne nazwiska sprzedawców:")
#print(unikalne_nazwiska)

#najwyzsze zamowienia 5
najwyzsze_zamowienia = df['Utarg'].nlargest(5)

print("5 najwyższych wartości zamówień z kolumny Utarg:")
print(najwyzsze_zamowienia)











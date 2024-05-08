import math
import random


def zad1():
    for x in range(25,41):
        rownanie = (math.sin(x)+math.log(36,4))**(1/3)
        print(round(rownanie,2))

def zad2():
    min = int(input("Wpisz liczbe minimalną: "))
    max = int(input("Wpisz liczbe maksymalną: "))
    ile = int(input("Podaj ilość cyfr: "))
    n = int(input("Podaj ilosc cyfr w jednym wierszu: "))
    try:
        if ile < n:
            raise ValueError("Liczba elementów w liście nie może być mniejsza niż liczba elementów w wierszu.")
        lista = [random.randint(min, max) for _ in range(ile)]
        wiersze = [lista[i:i + n] for i in range(0, len(lista), n)]
        print(wiersze)
    except ValueError as e:
        print("Błąd:", e)
        return None

def zad3(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            linie = plik.readlines()
            kolumny = [[] for _ in range(len(linie[0].split()))]
            for linia in linie:
                liczby = list(map(int, linia.split()))
                for i, num in enumerate(liczby):
                    kolumny[i].append(num)
            najmniejsze_z_kolumn = [min(kolumna) for kolumna in kolumny]
            return najmniejsze_z_kolumn
    except FileNotFoundError:
        print("Plik nie został znaleziony")

def zad4():
    a = int(input("Podaj dlugosc pierwszego boku: "))
    b = int(input("Podaj dlugosc drugiego boku: "))
    h = int(input("Podaj wysokosc graniastoslupa: "))
    if a <= 0 or b <= 0 or h <= 0:
        print("No z tego nie wyjdzie graniastoslup ")
        return None
    pole_podstawy = (a * b)
    wynik = ((pole_podstawy) * h)
    print(wynik)

def main():
    nazwa_pliku = "liczby.txt"
    zad1()
    zad2()
    print(zad3(nazwa_pliku))
    zad4()

if __name__ == '__main__':
    main()
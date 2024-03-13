import math
import random


def piramida():
    n = int(input("Wpisz liczbe znakow: "))
    for i in range(1,n+1):
        print(" "*(n-i)+"A"*i+"A"*(i-1))
        if n > 10:
            print("Niestety za duzo!")
            break
def trojkat():
    n = int(input("Wpisz liczbe znakow: "))
    for i in range(1, n + 1):
        print(""*(n - i) + "A" * i)
        if n > 10:
            print("Niestety za duzo!")
            break

def matematyka():
    a = ((math.exp(4)) - math.log(34, 2)) ** (1/3)
    print(round(a, 2))
    b = (math.log(20) + math.cos(45) + math.e) ** (1/3)
    print(round(b,2))
    c = ((math.log(20, 3) + math.sin(45) * (5/8))) ** (1/4)
    print(round(c, 2))
    d = math.log(23, 3) + (math.sin(34) + 5) ** (1/3)
    print(round(d, 2))
    e = (math.log(32, 2) + math.pi + math.sin(56)) ** (1/4)
    print(round(e, 2))

def zad5():
    def randomow():
        lista = []
        n = int(input("Wpisz liczbę wierszy i kolumn: "))
        for i in range(n):
            wiersz = []
            for j in range(n):
                losowa_wartosc = random.randint(1, 1000)
                wiersz.append(losowa_wartosc)
            lista.append(wiersz)
        return lista

    macierz = randomow()
    print("Wygenerowana macierz:")
    for wiersz in macierz:
        print(wiersz)
        print(sum(wiersz))

def zad4():
    a = int(input('Podaj liczbe a: '))
    b = int(input('Podaj liczbe b: '))
    napis = str(a**b)
    print(f'Liczba {a} podniesiona do potegi {b} wynosi: {a**b}')
    print(f'Dlugosc wyniku {a**b} to {len(str(a**b))}')
    print(f'Ostatnia liczba wyniku {a**b} to {napis[-1]}')



def main():
    piramida()
    trojkat()
    matematyka()
    zad4()
    zad5()
if __name__ == '__main__':
    main()
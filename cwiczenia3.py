import random
import math

def zad1():
    A = [1 - x for x in range(1,11)]
    print(A)

    B = [4**n for n in range(0,7)]
    print(B)

    C = [x for x in B if x % 2 == 0]
    print(C)

def zad2():
    losowa_lista = []
    losowa_lista_parzysta = []
    for i in range(1,11):
        n = random.randint(1,1000)
        losowa_lista.append(n)
        if n % 2 == 0:
            losowa_lista_parzysta.append(n)
    print(losowa_lista)
    print(losowa_lista_parzysta)

def zad3():
    zakupy = {
        "jajka": 'sztuka',
        "mleko": 'sztuka',
        "ziemniaki": 'kilogram',
        "jablka": 'kilogram',
    }

    sztuki = [produkt for produkt, jednostka in zakupy.items() if jednostka == 'sztuka']

    print(zakupy)
    print(sztuki)

def zad4():
    a = int(input("Podaj pierwszą dlugość przyprostokątnej: "))
    b = int(input("Podaj drugą dlugość przyprostokątnej: "))
    c = int(input("Podaj długość przeciwprostokątnej: "))

    def czy_trojkat_prostokatny(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return False
        a, b, c = sorted([a, b, c])
        return a ** 2 + b ** 2 == c ** 2
    wynik = czy_trojkat_prostokatny(a, b, c)
    if wynik:
        print(f"Trójkąt o bokach {a}, {b}, {c} jest prostokątny.")
    else:
        print(f"Trójkąt o bokach {a}, {b}, {c} nie jest prostokątny.")

def zad5():
    a = int(input("Podaj dlugosc podstawy: "))
    b = int(input("Podaj dlugosc podstawy: "))
    h = int(input("Podaj wysokosc: "))
    trapez = ((a+b)*h)/2
    print(trapez)

def zad6(a=1, b=4, ile=10):
    wynik = a
    for i in range(1,ile):
        wynik *= b
    return wynik

    wynik1 = zad6()
    wynik2 = zad6(a=2, b=3, ile=5)
    print(wynik1)
    print(wynik2)


def zad7():
    a = int(input("Podaj liczbe calkowita nieujemna: "))
    if a < 0:
        print("To liczba ujemna!")
        return
    print(math.sqrt(a))

def main():
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()
    zad6()
    zad7()
if __name__ == '__main__':
    main()
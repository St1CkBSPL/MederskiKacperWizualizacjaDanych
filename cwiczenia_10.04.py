import numpy as np
"""
a = np.arange(12).reshape((3,4))
print(a)
#suma calej macierzy
print(a.sum())
#suma kazdej z kolumn
print(a.sum(axis=0))
#minimum kazdego rzedu
print(a.min(axis=1))
#skumulowana suma dla rzedu
print(a.cumsum(axis=1))
b = np.arange(3)
print(b)
print(np.exp(b))
print(np.sqrt(b))
c = np.array([2.,-1.,4.])
print(c)
print(np.add(b,c))
d = np.arange(15)
"""

def zad1():
    macierz1 = np.array([1, 2, 3])
    macierz2 = np.array([4, 5, 6])
    wynik = np.dot(macierz1, macierz2)

    print("Macierz 1:", macierz1)
    print("Macierz 2:", macierz2)
    print("Wynik mnożenia:", wynik)


def zad2():
    macierz_3x3 = np.arange(9).reshape((3,3))
    macierz_4x4 = np.arange(16).reshape((4,4))

    print("Najniższe wartości dla każdej kolumny w macierzy 3x3:")
    print(np.min(macierz_3x3, axis=0))  # Najniższe wartości dla każdej kolumny
    print("Najniższe wartości dla każdego rzędu w macierzy 3x3:")
    print(np.min(macierz_3x3, axis=1))  # Najniższe wartości dla każdego rzędu

    print("\nNajniższe wartości dla każdej kolumny w macierzy 4x4:")
    print(np.min(macierz_4x4, axis=0))  # Najniższe wartości dla każdej kolumny
    print("Najniższe wartości dla każdego rzędu w macierzy 4x4:")
    print(np.min(macierz_4x4, axis=1))  # Najniższe wartości dla każdego rzędu

def zad3():
    macierz1 = np.array([1, 2, 3])
    macierz2 = np.array([4, 5, 6])
    iloczyn_macierzy = np.dot(macierz1, macierz2)
    print(iloczyn_macierzy)

def zad4():
    macierz_calkowita = np.array([1, 2, 3], dtype=int)
    macierz_rzeczywista = np.array([1.5, 2.5, 3.5])
    wynik = np.multiply(macierz_calkowita, macierz_rzeczywista)
    print(wynik)

def zad5():
    macierz = np.arange(6).reshape((2,3))
    a = np.sin(macierz)
    print(a)

def zad6():
    macierz = np.arange(6).reshape((2,3))
    b = np.cos(macierz)
    print(b)

def main():
    #zad1()
    #zad2()
    #zad3()
    #zad4()
    #zad5()
    #zad6()

if __name__ == '__main__':
    main()
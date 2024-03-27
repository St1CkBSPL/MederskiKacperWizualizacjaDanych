import numpy as np

def zad1():
    a = np.arange(3, 3*16, 3)
    print(a)

def zad2():
    a = np.arange(1,2,0.1)
    b = a.astype('int64')
    print(a)
    print(b)
    print(a.dtype)
    print(b.dtype)

def zad3():
    n = int(input("Wpisz liczbe calkowita: "))
    a = np.arange(1, n*n, 1)
    print(a)

def zad4():
    n = int(input("Wpisz liczbe potegowana: "))
    p = int(input("Wpisz ilosc poteg liczby n: "))
    potegi = np.logspace(0, p - 1, num=p, base=n, dtype=int)
    print(potegi)

def zad5():
    n = int(input("Wpisz dlugosc wektora: "))
    wektor = np.arange(n, 0, -1)
    diagonalna = np.diag(wektor)
    print(diagonalna)

def zad6():
    slowo_kolumna = "KOSZ"
    slowo_wiersz = "PLOT"
    slowo_ukos = "MYSZ"
    n = max(len(slowo_kolumna), len(slowo_wiersz), len(slowo_ukos))
    macierz = np.full((n, n), ' ', dtype='<U1')
    for i, litera in enumerate(slowo_kolumna):
        macierz[i, 0] = litera
    for j, litera in enumerate(slowo_wiersz):
        macierz[0, j] = litera
    for k, litera in enumerate(slowo_ukos):
        macierz[k, n - 1 - k] = litera

    print(macierz)


def zad7():
    n = int(input("Wpisz rozmiar macierzy: "))
    macierz = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if i == j:
                macierz[i, j] = 2 * (j + 1)
            else:
                distance = abs(i - j)
                macierz[i, j] = 2 * (distance + 1)
    print(macierz)


def zad9():
    def fibonacci(n):
        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib

    def macierz_fib(n):
        fib_sequence = fibonacci(n ** 2)
        macierz = np.array(fib_sequence[:n ** 2]).reshape((n, n))
        return macierz

    print(macierz_fib(5))


def main():
    #zad1()
    #zad2()
    #zad3()
    #zad4()
    #zad5()
    zad6()
    #zad7()
    #zad9()


if __name__ == '__main__':
    main()

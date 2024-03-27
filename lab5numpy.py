import numpy as np

# a = np.arange(5)
# print(a)
# print(type(a))
# print(a.dtype)
# b = a.astype('float')
# print(b)
# print(b.dtype)
# print(b.shape)
# print(b.ndim)
# m = np.array([np.arange(2), np.arange(2)])
# print(m)
# print(m.shape)
# print(m.dtype)
# print(type(m))
# zera = np.zeros((5, 5))
# print(zera)
# pusta = np.empty((4, 4))
# print(pusta)
# macierz = np.array([[1, 2], [3, 4]])
# print(macierz)
# liczby = np.arange(1, 5, 0.1)
# print(liczby)
# liczby_lin = np.linspace(1, 2, 5)
# print(liczby_lin)
# z = np.indices((5, 3))
# print(z)
# x, y = np.mgrid[0:5, 0:5]
# print(x)
# print(y)
# mat_diag = np.diag([a for a in range(5)])
# print(mat_diag)
# z = np.fromiter(range(5), dtype = 'int32')
# print(z)
# marcin = b'Marcin'
# mar = np.frombuffer(marcin,dtype='S1')
# print(mar)
# mar_2 = np.frombuffer(marcin,dtype='S2')
# print(mar_2)
# marcin = 'Marcin'
# mar_3 = np.array(list(marcin))
# mar_4 = np.array(list(marcin), dtype='S1')
# mar_5 = np.array(list(b'Marcin'))
# mar_6 = np.fromiter(marcin,dtype='S1')
# mar_7 = np.fromiter(marcin,dtype='U1')
# print(mar_3)
# print(mar_4)
# print(mar_5)
# print(mar_6)
# print(mar_7)
# mat = np.ones((2, 2))
# mat_1 = np.ones((2, 2))
# mat = mat / mat_1
# print(mat)
# a = np.arange(10)
# print(a)
# s = slice(2, 7, 3)
# print(a[s])
# s = range(2, 7, 2)
# print(a[s])


def zad1():
    a = np.arange(3, 3*16, 3)
    print(a)


def zad2():
    a = np.arange(5, dtype='float')
    print(a)
    print(a.dtype)
    b = a.astype('int64')
    print(b)
    print(b.dtype)


def zad3(n):
    tablica = np.arange(1, n*n+1).reshape(n, n)
    print(tablica)


def zad4(p, i):
    potegi = np.logspace(1, i, num=i, base=p, dtype=int)
    print(potegi)


def zad5(n):
    wektor = np.arange(n, 0, -1)
    print(wektor)
    macierz = np.diag(wektor)
    print(macierz)


def zad6():


def main():
    # zad1()
    # zad2()
    # zad3(n=int(input("Podaj liczbe n: ")))
    # zad4(p=2, i=4)
    # zad5(n=5)
    zad6()


main()


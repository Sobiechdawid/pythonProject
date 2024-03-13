def zad1():
    z = input("Podaj zdanie ")
    ilosc = len(z.split())
    print("ilosc slow to ", ilosc)


def zad2():
    a = int(input("Podaj 1 liczbe "))
    b = int(input("Podaj 2 liczbe "))
    c = int(input("Podaj 3 liczbe "))
    wynik = (a**b)+c
    print(wynik)


def zad3():
    slowo = input("Podaj slowo ")
    slowo = slowo.lower()

    if slowo == slowo[::-1]:
        print("Podanie slowo jest palindromem")
    else:
        print("Podanie slowo nie jest palindromem")


def zad4():
    n = int(input("Podaj liczbe "))
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def zad5():




def main():
    #zad1()
    #zad2()
    #zad3()
    #if zad4():
    #    print("tak")
    #else:
    #    print("nie")
    zad5()


main()

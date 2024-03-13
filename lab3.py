import random


def zad1():
    a = [1 - x for x in range(1, 11)]
    b = [4**i for i in range(8)]
    c = [x for x in b if x % 2 == 0]
    print(a)
    print(b)
    print(c)


def zad2():
        lista1 = [random.randint(1, 100) for i in range(1, 11)]
        lista2 = [x for x in lista1 if x % 2 == 0]
        print(lista1)
        print(lista2)


def zad3():
    produkty_spozywcze = {
        "jablka": "kg",
        "jajka": "sztuki",
        "mleko": "litry",
        "chleb": "sztuki",
        "pomidory": "kg",
        "ogorek": "kg",
        "ser": "kg",
        "maslo": "sztuki"
    }
    produkty_sztuki = [i for i, x in produkty_spozywcze.items() if x == "sztuki"]
    print("Produkty w sztukach", produkty_sztuki)


def zad4():
    a = int(input("Podaj 1 bok trojkata "))
    b = int(input("Podaj 2 bok trojkata "))
    c = int(input("Podaj 3 bok trojkata "))
    if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        print("Trojkat jest prostokatny")
    else:
        print("Trojkat nie jest prostokatny")


def zad5():
    a = int(input("Podaj 1 bok trapezu "))
    b = int(input("Podaj 2 bok trapezu "))
    h = int(input("Podaj wysokosc trapezu "))
    c = (a+b)*h/2
    print(c)


def zad6():



def main():
    #zad1()
    #zad2()
    #zad3()
    #zad4()
    #zad5()
    zad6()


main()

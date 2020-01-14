import random

WORDS = ("rak", 'kon', "zuk", "lew", "lis")

nowe = random.choice(WORDS)
dlugosc = len(nowe)
szansa = 0

print("Komputer losuje nazwe zwierzaka na 3 litery")
print("Masz 3 szanse zeby je odgadnac")
print("za kazdym razem mozesz sie spytac czy dana litera wystepuje w slowie")
print("Zaczynamy,a wiec powodzenia!")
print("pierwsza litera slowa to: ", nowe[0], "")
print("dlugosc slowa to: ", dlugosc, "liter")

while szansa <= 2:
    pyt = input("Spytaj czy litera wystepuje w slowie: ")
    if pyt in nowe:
        print("tak")
    else:
        print("nie")
    szansa += 1

odp = input("podaj slowo: ")

prob = 1

while prob != 3:
    if odp == nowe:
        print("ZGADLES ")
        break
    else:
        print("NIE ZGADLES")

        prob += 1

        if prob <= 3:
            print("wykorystales limit prob, " + "haslo to: " + nowe)
            break
        else:
            odp = input("podaj slowo: ")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

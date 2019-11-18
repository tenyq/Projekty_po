import random

WORDS = ("rak",'kon',"zuk","lew","lis")

nowe= random.choice(WORDS)

print (nowe)

dlugosc = len(nowe)

print("Komputer losuje nazwe zwierzaka na 3 litery\n")
print("Masz 3 szanse zeby je odgadnac\n")
print("za kazdym razem mozesz sie spytac czy dana litera wystepuje w slowie\n")
print("Zaczynamy,a wiec powodzenia!\n")
print("pierwsza litera slowa to: ", nowe[0],"\n")
print("dlugosc slowa to: ", dlugosc, "liter\n")
szansa = 0
while szansa <= 2:
	pyt = input("Spytaj czy litera wystepuje w slowie: ")
	if pyt in nowe:
		print("tak")
	else:
		print("nie")
	szansa = szansa + 1


odp = input("podaj slowo: ")
if odp == nowe:
	print("ZGADLES ")
else:
	print("NIE ZGADLES")


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
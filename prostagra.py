print("Jestes rycerzem i masz 10 punktow zycia.")
print("Naciera na ciebie grupa przeciwnikow.")
print("Pogromienie kazdego z nich zabiera 2 punkty zycia.\n")

health = 10
trolls = 0
damage = 2

while health > 0:
    trolls += 1
    health -= damage

    print("Bohater pokonuje przeciwnika, " \
          "ale odnosi obrażenia i traci", damage, "punkty zdrowia.\n")

print("Twój bohater walczył dzielnie i pokonał", trolls, "przeciwnikow.")
print("Lecz niestety Twój bohater już nie żyje.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")


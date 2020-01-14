class Calculator():
    def dodaj(self, a, b):
        wynik = a + b
        print(wynik)

    def odejmij(self, a, b):
        wynik = a - b
        print(wynik)

    def podziel(self, a, b):
        wynik = a / b
        print(wynik)

    def pomnoz(self, a, b):
        print(a * b)

calc = Calculator()
calc.odejmij(5, 4)
calc.dodaj(5, 5)
calc.podziel(5, 5)
calc.pomnoz(5, 5)

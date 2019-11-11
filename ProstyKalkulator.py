class Calculator():
    def dodaj(self, a, b):
        wynik = a + b
        print(wynik)
    def odejmij(self, a, b):
        wynik = a - b
        print(wynik)


calc = Calculator()
calc.odejmij(5,4)
calc.dodaj(5,5)

class Automobil:
    # La inceput, definim atributele
    numar_roti = 4
    forma = None
    culoare = None
    numar_usi = 2

    # Mai jos definim metode ( functii )
    def printeaza_numar_roti(self):
        if self.numar_roti == 2:
            print(f'Numarul de roti este {self.numar_roti}')
            print('Automobilul nostru este motocicleta')

    def printeaza_forma(self, tablarie):
        self.forma = tablarie  # atributul metodei il
        if self.numar_roti == 'SUV':
            print(f'Numarul de roti este {self.numar_roti}')
            print('Automobilul este motocicleta')
        elif self.numar_usi == 2:
            print(f'Numarul de roti este {self.numar_roti}')
            print('Automobilul este masina sport')
        elif self.numar_roti == 4:
            print(f'Numarul de roti este {self.numar_roti}')
            print('Automobilul este masina de familie')

    def printeaza_culoare(self):
        if self.numar_roti == 0:
            print(f'Numarul de roti este {self.numar_roti}')
            print('Automobilul este motocicleta')

    def printeaza_numar_roti(self):
        if self.numar_roti == 0:
            print(f'Numarul de roti este {self.numar_roti}')
            print('Automobilul este motocicleta')
        elif self.numar_usi == 2:
            print(f'Numarul de roti este {self.numar_roti}')
            print('Automobilul este masina sport')
        elif self.numar_roti == 4:
            print(f'Numarul de roti este {self.numar_roti}')
            print('Automobilul este masina de familie')


# Aici am initializat clasa automobil in obiectul caruta

caruta = Automobil()

# Acum folosim proprietatile obictului caruta. Punem punct dupa ce am initializat clasa
# 1. Apelarea de atribute

print(caruta.numar_usi)

# 2. Apelarea de metode
caruta.numar_usi

# 3. apelare de metode si argumente
caruta.printeaza_forma("SUV")

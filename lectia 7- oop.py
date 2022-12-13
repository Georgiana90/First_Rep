# ---------------------- 1 pilon:Exception-------------------------
from abc import abstractmethod, ABC


#Try-Except # dupa except punem numele erorii
try:
    assert 1 == 2, 'comparatia nu este corecta' #propozitia dintre ghilimele este atribuita asserionerror
except AssertionError as e:         #e de la elias-
    print(e,' Programul nu a executat linia respectiva')    #printam eroarea

print('Hello')      #exclude eroarea si continua sa ruleze


# -------------------------Mostenirea---Enharathence--------------------------

# 2.Mostenirea - > classa figura geometrica (parinte) si ai clasa (copil) - cerc,patrat,triunghi

class Masina:
    def numar_roti(self):
        print('Masina are 4 roti')


class Jeep(Masina):
    def suspensii(self):
        print('Jeppul are suspensii mari')


hummer = Jeep()
hummer.numar_roti()  # cu . avem acces la toate clasele ( Jeepul fiind copil clasa Masina - parinte)
hummer.suspensii()
logan = Jeep()
logan.numar_roti()
logan.suspensii()
ford = Masina()  # avem acces doar metoda din prima clasa.Mostenirea e unimensionala ( parinte-copil)
ford.numar_roti()


# -------------------------------------Polimorfism------polymorphism-----------------
# -------------------------------------Abstractizare----

# 3.Polimorfism - se comporta diferit in anumite situatii
# printul -
# 4.Abstractizarea


class Masina(ABC):          # aici implementam o clasa abstracta ( interfata )
    @abstractmethod  # - punem abnotare
    def numar_roti(self):
        raise NotImplementedError

    @abstractmethod
    def culoare(self):
        raise NotImplementedError


class Suv(Masina):
    def __suspensii(self):
        print('Jeppul are suspensii mari')

    def numar_roti(self):
        print('Roti de teren')

    def culoare(self):
        print('Culoarea este negru')


class Sport(Masina):
    def numar_roti(self):
        print('4 Roti de circuit')

    def culoare(self):
        print('Culoarea este albastru')


ferrari = Sport()
ferrari.numar_roti()
volvo = Suv()
volvo.culoare()     #aici am implementat polymorfismul
ferrari.culoare()   #aici am implementat polymorfismul

#incapsulare
# volvo.suspensii()   #nu o gaseste pt ca am facut incapsulare cu __ in clasa SUV in metda si ne da erore.
#folosim exception

try:
    volvo.suspensii()
except NameError :
    print('Sunt expert pe tratarea erorilor ')
except AttributeError :
    print('Sunt expert pe tratarea erorilor ')

print('Test1')
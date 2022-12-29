# 2. Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum
# împreună).
# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’
from abc import abstractmethod, ABC


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print("Cel mai probabil am colturi")

    # INHERITANCE


# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură

class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.latura = latura

    # ENCAPSULATION
    # latura este proprietate privată
    # Implementează getter, setter, deleter pentru latură
    # Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
    # implementezi metoda abstractă aria)

    __latura = None


    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, latura):
        self.__latura = latura

    @latura.deleter
    def latura(self):
        self.__latura = None



    def aria(self):
        aria = self.__latura * self.__latura
        print(aria)




# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)

class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, raza):
        self.__raza = raza

    @raza.deleter
    def raza(self):
        self.__raza = None

    def aria(self):
        return FormaGeometrica.PI * self.__raza * self.__raza

    def descrie(self):
        print('Eu nu am colturi')

# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# Creează un obiect de tip Patrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui


patrat1 = Patrat(9)
patrat1.latura = 4
patrat1.aria()
print(patrat1.latura)
del patrat1.latura
print(patrat1.latura)
patrat1.descrie()



cerc1 = Cerc(4)
cerc1.raza = 7
print(cerc1.aria())
print(cerc1.raza)
del cerc1.raza
print(cerc1.raza)
cerc1.descrie()




# 3. Actualizează proiectul pe github facand un push la noul cod
# În Foldereul de teme ajunge să pui doar linkul cu proiectul tău public

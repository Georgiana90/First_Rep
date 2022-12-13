# #cheia repr intotdeauna o valoare, si este string => dict

lista_numere = [1, 2, 3, 56, 86]
print(type(lista_numere))
lista_numere[2] = 75 #suprascriem elem cu index 2 (3)
print(lista_numere)
var_str = 'abc'
noua_lista = lista_numere + list(var_str) # se ia fiecare element si se adauga in lista (a,b,c)
print(noua_lista)

#------------------------------------------------lista in lista--------------------------------
lista_lista = [43,21,[65,23,89]]
print(lista_lista)
print(lista_lista[2]) #=>se printeaza lista nr 2 din lista
print(lista_lista[2][1]) # =>se printeaza din lista nr 2, elementul cu index 1
#=> putem face mai multe liste in liste

lista_lista = [43,21,[65,23,(1,2,3)]]  # adaugand () -> se adauga un tuple
print(type(lista_lista[2][2]))
print(lista_lista[2][2][0]) #=> se printeaza un element din cadrul tuple(1,2,3)

# #----------------------------------------- Dict-------------------------------------------------

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.keys())
print(thisdict.get('brand'))

json_dict={
    "1": {
        "title": "example glossary",
		"2": {
            "title": "S",
			"3": {
                "4": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]}}}}}}



print(json_dict.get('1').get('2').get('3').get('4').get('ID')) # mergem din dictionar in dictionar sa aflam o anumita
# cheie
#

#------------------------------------------------SET si TUPLE----------------------------------------------------------

#-------------SET---------------
# printeaza random, nu are index

a= {1, 56, 43, 43, 76, 3, 90, 56, 23}
print(a)

# la SET nu printeaza duplicatele
print(a)
# print(a[2]) # nu poate vedea o pozitie, nu are index !
print(a)

#------------TUPLE---------------

# tuple se da cu paranteza ()
# ordinea va fi aceeasi
# duplicatul il ia in considerare si fiecare dintre ele au un index
# putem face apelare de index

a = (1, 56, 43, 43, 76, 3, 90, 56, 23)

print(a)
print(a[2])
print(a[3])

x = (765, 452) # stie deja ca e tuplu datorita parantezelor ()
b = () # am luat o variabila goala de tip tuplu
c = b.__add__(x) # adaugam valori
print(a.__add__(x))
print(c)

print(a+x)
a=a+x
print(a)
#
# # nu avem in tuplu append
# # in tuplu se sterge variabila cu totul, se reinitializeaza
# # in tuple nu poti muta valori ( nu poti folosi reverse )
#
#
#
lista1 = [1, 2, 3, 4]
lista1.reverse()
print(lista1)
#-----------------------------exercitii

#dictionarul nu are voie sa aiba key identice
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "old_year": 1964,
    "year": {               # in cadrul dictionarului am definit alt dictionar
        "year": 2020
    }
}
# CTRL + ALT + L => se face alinierea codului

dict = {}
print(type(dict))
key_elev = 'Ionica'     # se foloseste varianta asta pt a adauga key in dict gol
value_elev = 2          # se foloseste varianta asta pt a adauga valoare in dict gol
set1 = set ({})       # convertim un Dict in Set
print(type(set1))
dict [key_elev] = value_elev
dict ['ionica'] = 2         # adaugam fortat key cu [''] iar dupa punem = si adaugam valoare
print(dict)
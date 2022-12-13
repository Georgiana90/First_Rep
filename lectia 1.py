nume = 'banciu georgiana 32'
print(len(nume))
n = nume [17:19]
print(type(n))
n = int(n)

trei_doi = nume[:16:-1]
print(trei_doi[::-1])
print(nume [:16:-1][::-1])

# masina = input('Te rog introdu textul:')
# print(masina)

casa = 25.4
casa_int = int (casa.__round__())
print(casa_int)

#verificam ca typeul unei variabile e = cu typeul celei de a 2 a variabila # daca e false ne da eroare(float + int =err
assert type(casa)==casa_int

#daca typeul unei variabile = cu typeul celei de a 2 a variabile => conditie true ( tipul variabilei = int+ int )
assert type(int(casa))==type(casa_int)

#print, input, tipuri de date

variabila_true = True
assert variabila_true == 1

propozitie= 'ana are mere'
variabila2 = propozitie.upper()
#tinem apasat pe CTRL dupa . si ne deschide o noua clasa cu dictionare

print(variabila2)
print(len(variabila2))
print(variabila2[0:len(variabila2)-2]+propozitie[10:len(propozitie)])

print(variabila2[0:-2]+ ' aici printez')

print(variabila2[0:-2]+propozitie[10:12])

print(variabila2[:-2]+ propozitie [10:])

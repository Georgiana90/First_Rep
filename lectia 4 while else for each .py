# Cicluri repetitive while/ for each/ for
# sa iesim din ciclurile repetitive avem => break sau continue

propozitie = 'Ana are meRe'
for litera in propozitie:
    if litera == 'R'or litera == 'r':
        print(propozitie[5])
#

propozitie = 'Ana are meRe'
for litera in propozitie:
    if litera.upper() == 'R':
        print(propozitie[5])

index = 1
while 23 >= index:
    index += 1
    print(index)
    if index <= 25:
        print('Maine este vineri')
        if index == 25:
          break
    print(index)
else:
    print('Am terminat de rulat')


propozitie2 = 'Ana are mere'
for index in range(10):
    if index == 5:
        continue
    print(propozitie2[index])
else:
    print('Am terminat')


# paine = ['paine alba','paine Graham','paine secara']
# lista_cumparaturi = ['lapte','oua','apa',['creion','pix','radiera'],paine]
# for produs in lista_cumparaturi:
#     # print(lista_cumparaturi)  #face print ori de cate ori gaseste un produs= > 4 x
#     if type(produs) == list :
#         for subprodus in produs:
#             print(subprodus)

paine = ['paine alba','paine Graham','paine secara']
lista_cumparaturi = ['lapte','oua','apa',['creion','pix','radiera'],paine]
for cumparatura in lista_cumparaturi:
    print(type(cumparatura))
    if type(cumparatura) == list :
        # print(cumparatura)
        cumparatura_clona = cumparatura
        lista_cumparaturi.remove(cumparatura)
        lista_cumparaturi.extend(cumparatura_clona)
        # for subprodus in cumparatura:
        #     print(subprodus)
    print(lista_cumparaturi)


print(lista_cumparaturi)
print(lista_cumparaturi[3])   # printam a 2-a lista care are index 3,( lapte,oua,apa, lista noastra)
penar = lista_cumparaturi[3]
pix = penar[1]
print(pix)
print(lista_cumparaturi[3][1])   #printam indexul 1 din a 2-a lista
print(lista_cumparaturi[4][2])      #printam a 3-a lista de cumparaturi care are index 4, si scoatem elementul cu idx 2

# varianta andreei
paine = ['paine alba', 'paine Graham', 'paine secara']
lista_cumparaturi = ['lapte', 'oua', 'apa', ['creion', 'pix', 'radiera'], paine]
lista_cumparaturi2 = []
for produs in lista_cumparaturi:
    if type(produs) == list:
        for subprodus in produs:
            print(subprodus)
            lista_cumparaturi2.append(subprodus)
    else:
        # print(produs)
        lista_cumparaturi2.append(produs)
print(lista_cumparaturi2)

propotitie = 'Ana are mere'

x = 0
for litera in propotitie:
    if litera == 'r':
        x += 1
print(x)

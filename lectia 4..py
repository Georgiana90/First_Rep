def verifica_prezenta():
    lista = ['Ionel','Gicu','Popescu']
    for index in range(2):
        print(lista[index])
        # assert lista[index] is 'Ionel'
verifica_prezenta()
# # ----------------------------------------------------------------
string_masini = input('Scrie o lista de masini despartite cu ,: ')
print(string_masini)
lista_masini = string_masini.split(',')


def returneaza_litera(portocala,mar = 5):
    print(mar)
    for masina in portocala:
        if masina == 'Tractor':
            for indexlitera in range(len(masina)):
                if masina[indexlitera] == 'b':
                    return (masina[indexlitera])
                elif masina[indexlitera] == 't':
                    return (masina[indexlitera])

#
print(returneaza_litera(lista_masini,8))
list1 = [0, 1, 2, 3]
list2 = [0, 1, 4, 5]
list3 = list1 + list2
print(list(set(list3)))

index = 0
while index < 5:
    list1 = [0, 1, 2, 3, 4]
    print(list1[index])
    index = index + 1

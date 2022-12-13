# functia simpla nu primeste paremetru nu returneaza nimic, ea primeste cod si returneaza cod
def hi():
    print('Am inceput tema !')


# functia cu parametrii =

a = 5
b = 3

def sum(numar1, numar2):
    numar3 = numar1 + numar2
    return numar3
sum(a,b)

# functia cu return => returneaza ceva in schimb

def is_natural(numar):
    if numar >= 0:
        return 'numar este natural'
    else:
        return 'numarul nu este natural'


# functii cu parametrii si return

# functia este o zona de cod cu o mica logica proprie care poate fi folosita/refolosita apelata de oricate ori avem nevoie

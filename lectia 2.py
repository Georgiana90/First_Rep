a = 5
print(a)
a += 3 + a  # a = a+3
a = a + 3 + a
print(a)
if a == 28:
    print('Am ajuns aici')
elif a == 29:
    print('Am ajuns iarasi aici')
else:
    print('Nu am ajuns aici')

qwer = 'taste'

#aflam daca contine grupul de litere as
if qwer.__contains__('as'):
    print('Exista')
    qwer += '123' # facem suprascriere in cadrul if
    print(qwer)
# aflam daca are numar-> trebuie sa substragem elementul pe care l-am convertit in int
    if int(qwer[5])==1:
        print('Exista numar')

# in interiorul conditiei if pot exista mai multi 'if'
# putem avea si in interiorul lui else: un alt'if'

# aflam daca variabila se afla intr-un sir de numere
variabila = 40
if variabila in  range (30,50):
   numar = str(variabila) +' ani'
   print(numar)
   if numar.__contains__(' '):
       print('Contine spatiu')

       if numar.find(' '):
          print('Merge')

pret = 678
if pret >= 678:
    elev = 'Ionel a luat nota 6'
    # print(len(elev))
    # nota = elev[0:1:1]
    nota = elev[:17:-1]

    # print(nota[:len(nota)-2:-1])
    # nota = len(elev[::-1])
    # nota = int(elev[len(elev)-1:len(elev):1])
    print(nota)
    print(type(nota))
    nota = float(nota)   # 
    if nota>=4.5:
        print('Ai trecut')



class Figura_geometrica:
    lungime_latura = None
    latime_latura = None
    raza = None

    def __init__(self, a, b, c):            #Reprezinta constructorul
        self.lungime_latura = a
        self.latime_latura = b
        self.raza = c

    def printeaza_lungimea(self):
        print(f'Lungimea este {self.lungime_latura}')



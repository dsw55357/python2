#dodawanie, odejmowania, mnożenia i dzielenia liczb zespolonych
import cmath

class tComplex:
    def __init__(self, z1_, z2_):
        self.z1 = z1_
        self.z2 = z2_
        self.powitanie()

    def add(self):
        return print(self.z1 + self.z2)

    def sub(self):
        return print(self.z1 - self.z2)

    def mul(self):
        return print(self.z1 * self.z2)

    def div(self):
        try:
            result = self.z1 / self.z2
            return print()
        except ZeroDivisionError as e:
            print("ZeroDivisionError: complex division by zero ")

#    def area(self):
#        return 3.14 * (self.radius ** 2)

    def powitanie(self):
        print(">> Liczby zespolone: [{}, {}]".format(self.z1, self.z2))




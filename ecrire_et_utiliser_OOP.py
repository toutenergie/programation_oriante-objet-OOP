# Instanciez un objet
class Rectangle:
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color
    def calculalor_aer(self):
        return self.length*self.width

rect1 = Rectangle(4, 2, "blue")
rect2 = Rectangle(3, 1, color="pink")
print(rect1.calculalor_aer())
print(rect2.calculalor_aer())
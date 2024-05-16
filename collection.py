class Person:
    """Personne."""

    def __init__(self, name):
        """Donne un nom."""
        self.name = name
    
    def walk(self):
        """Marche."""
        print(f"{self.name} marche.")


volunteers = [Person("Alice"), Person("Bob"), Person("Carol")]
for volunteer in volunteers:
    volunteer.walk()

# Ici, nous reprenons nos outils !
"""toolbox = {
    "screwdriver": Screwdriver(50),
    "hammer": Hammer(),
    "nails": [Nail(), Nail(), Nail()],
}"""

#------------------------------------------------------------------------
class Humme:
    def run(self):
        print("je peux couri")

class Lion:
    def run(self):
        print("Roal !")
        
class Poission:
    def swin(self):
        print("elle nage:")

"""
entites =[Humme(),Lion(),Poission()]
for entity in entites:
    if entity in [Humme(),Lion()]:
        print(entity.run())
    else:
        print(entity.swin())
"""        
class A:
    def func(self):
        pass


class B:
    def func(self, number):
        pass


elements = [A(), B()]
for item in elements:
    item.func()
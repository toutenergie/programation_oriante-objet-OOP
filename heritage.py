class Film:
    def __init__(self,name):
        self.name=name
    
    def wath(self):
        print("BON VISSIONNAGE")

class FilmCassette(Film):
    """Un film en cassette !"""

    def __init__(self, name):
        """Initialise le nom et la bande magnetique."""
        self.name = name
        self.magnetic_tape = True
    
    def rewind(self):
        """Rembobine le film."""
        print("C'est long à rembobiner !")
        self.magnetic_tape = True

filme= Film("2001: odysee")
filemecacette=FilmCassette("blode runner")

print(filme.name)
print(filme.wath)

print(filemecacette.name)
print(filemecacette.wath)


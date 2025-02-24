    #class Vecteur2D
class Vecteur2D :
    #constructeur : 
    def __init__(self,x=0 , y=0):
        self.x=x
        self.y=y
    #method pour afficher les cordonnees de vecteur
    def afficher(self):
        print(f"({self.x,self.y})")
    #surcharge d'addition
    def __add__(self, other):
            return Vecteur2D(self.x + other.x, self.y + other.y)

# Classe Rectangle
class Rectangle:
    def __init__(self, longueur=1, largeur=1):
        self.longueur = longueur
        self.largeur = largeur
        self.nom = "rectangle"

    def afficher(self):
        print(f"{self.nom} - Longueur: {self.longueur}, Largeur: {self.largeur}")

    def surface(self):
        return self.longueur * self.largeur

# Classe Carre
class Carre(Rectangle):
    def __init__(self, cote=1):
        super().__init__(cote, cote)
        self.nom = "carré"

# Classe Point
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

# Classe Segment
class Segment:
    def __init__(self, x1, y1, x2, y2):
        self.orig = Point(x1, y1)
        self.extrem = Point(x2, y2)

    def afficher(self):
        print(f"Segment de {self.orig.x}, {self.orig.y} à {self.extrem.x}, {self.extrem.y}")

# Programme principal
if __name__ == "__main__":
    # Instanciation de Vecteur2D
    v1 = Vecteur2D()
    v2 = Vecteur2D(3, 4)
    v1.afficher()
    v2.afficher()
    v3 = v1 + v2
    v3.afficher()

    # Instanciation de Rectangle et Carre
    rect = Rectangle(5, 3)
    carre = Carre(4)
    rect.afficher()
    print(f"Surface du rectangle: {rect.surface()}")
    carre.afficher()
    print(f"Surface du carré: {carre.surface()}")

    # Instanciation de Segment
    segment = Segment(1, 2, 3, 4)
    segment.afficher()
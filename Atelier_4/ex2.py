class Etudiant:
    def __init__(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne

    def __repr__(self):
        return f"{self.prenom} {self.nom}, Age: {self.age}, CNE: {self.cne}, Moyenne: {self.moyenne}"

# Création d'une liste d'étudiants
liste_etudiants = [
    Etudiant("Dahbi", "mohamed", 20, "CNE001", 15.5),
    Etudiant("Misbah", "yassin", 22, "CNE002", 16.0),
    Etudiant("Ghandouri", "ayman", 19, "CNE003", 14.5),
    Etudiant("Misbahi", "akram", 21, "CNE004", 18.0),
    Etudiant("Maysour", "siraj", 20, "CNE005", 12.0),
]

# Tri de la liste selon l'âge puis la moyenne
liste_etudiants.sort(key=lambda etudiant: (etudiant.age, etudiant.moyenne))

# Affichage de la liste triée
for etudiant in liste_etudiants:
    print(etudiant)

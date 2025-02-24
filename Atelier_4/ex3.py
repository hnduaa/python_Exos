class Utilisateur:
    def __init__(self, nom, email, mot_de_passe, genre, age):
        self._nom = nom
        self._email = email
        self._mot_de_passe = mot_de_passe
        self._genre = genre
        self._age = age


class Professeur(Utilisateur):
    def __init__(self, nom, email, mot_de_passe, genre, age, ppr, grade):
        super().__init__(nom, email, mot_de_passe, genre, age)
        self.__ppr = ppr
        self.__grade = grade
        
    def assign_passport(self, AnneeAcademique):
        self.__AnneeAcademique = AnneeAcademique


class Etudiant(Utilisateur):
    def __init__(self, nom, email, mot_de_passe, genre, age, code_massar):
        super().__init__(nom, email, mot_de_passe, genre, age)
        self.__code_massar = code_massar
        self.__AnneesAcademique= []
    def assign_passport(self, AnneeAcademique):
        self.__AnneesAcademique.append(AnneeAcademique)
        AnneeAcademique.addEtudiant(AnneeAcademique)


class AnneeAcademique:
    def __init__(self, annee):
        self.__annee = annee
        self.__etudiants=[]
    def addEtudiant(self,etudiant):
        self.__etudiants.append(etudiant)


class Module:
    def __init__(self, nom, volume_horaire, semestre):
        self.__nom = nom
        self.__volume_horaire = volume_horaire
        self.__semestre = semestre
        self.__matieres = []  # Relation de composition avec Matiere


class Matiere:
    def __init__(self, nom, pourcentage):
        self.__nom = nom
        self.__pourcentage = pourcentage
        self.__evaluations = []  # Relation d'association avec Evaluation


class Evaluation:
    def __init__(self, note):
        self.__note = note
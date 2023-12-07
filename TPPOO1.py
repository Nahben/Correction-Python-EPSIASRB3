# -*- coding: utf-8 -*-
"""
**Exercice 1 (clé) :**

Question 1
"""

class Voiture:
    def __init__(self, modele, marque, prix):
        self.modele = modele
        self.marque = marque
        self.prix = prix

voiture1 = Voiture('Tesla', 'Model 3', 45000)
voiture2 = Voiture('Tesla', 'Model S', 65000)

print(voiture1.prix)
print(voiture2.prix)

"""Question 2"""

class Avion:
  def __init__(self, marque, modele, nbr_siege, distance):
    self.marque = marque
    self.modele =  modele
    self.nbr_siege =  nbr_siege
    self.distance = distance

avion1 = Avion("Airbus", "A380", 525, 20000)
avion2 = Avion("Airbus", "747-8", 467, 18000)

"""**Exercice 2 (clé) :**

Question 1
"""

class Humain:
  def __init__(self, age, nom, prenom):
    self.age = age
    self.nom = nom
    self.prenom = prenom

humain1 = Humain(25, "Jean", "David")
humain2 = Humain(42, "Dubois", "Liloo")

print("Je m'appelle", humain1.prenom, "et j'ai", humain1.age, "ans")
print("Je m'appelle", humain2.prenom, "et j'ai", humain2.age, "ans")

"""Question 2"""

class Humain:
  def __init__(self, age, nom, prenom):
    self.__age = age
    self.nom = nom
    self.prenom = prenom

  def setnom(self, nom):
    self.nom = nom

  def setprenom(self, prenom):
    self.prenom = prenom

humain1 = Humain(25, "Jean", "David")
print(humain1.prenom, humain1.nom)

print(humain1)
humain1.setnom("Octave")
humain1.setprenom("Martin")
print(humain1.prenom, humain1.nom)

"""Question 3"""

class Humain:
  def __init__(self, age, nom, prenom):
    self.age = age
    self.nom = nom
    self.prenom = prenom

  def grandir(self):
    self.age += 1

humain1 = Humain(25, "Jean", "David")
print(humain1.age)

humain1.grandir()
print(humain1.age)

"""Question 4 (bonus)"""

class Humain:
  def __init__(self, age, nom, prenom):
    self.age = age
    self.nom = nom
    self.prenom = prenom

  def grandir(self, age):
    self.age += age

humain1 = Humain(25, "Jean", "David")
print(humain1.age)

humain1.grandir(5)
print(humain1.age)

"""**Exercice 3 (clé) :**

"""

class CompteBancaire:
    def __init__(self, idNumber, nomPrenom, solde):
        self.idNumber = idNumber
        self.nomPrenom = nomPrenom
        self.solde = solde

    def versement(self, argent):
        self.solde += argent

    def retrait(self, argent):
        if(self.solde < argent):
            print(" Impossible d'effectuer l'opération. Solde insuffisant !")
        else:
            self.solde -= argent

    def afficher(self):
        print("Compte numéro : " , self.idNumber)
        print("Nom & Prénom : ", self.nomPrenom)
        print(" Solde  : ", self.solde , " € ")
        print("Sauf erreur ou omisssion ! ")

monCompte = CompteBancaire(16168891, " Bouvier David", 22300)
monCompte.versement(1500)
monCompte.retrait(24000)
monCompte.afficher()

"""**Exercice 4 (secondaire) :**"""

class Personne:
  def __init__(self, taille, poids, age):
    self.taille = taille
    self.poids = poids
    self.age = age

  def imc(self):
    return (self.poids)/(self.taille**2)

  def interpretation(self):
    if self.imc() <= 18.5:
      print("Insuffisance pondérale")
    elif self.imc() >= 30:
      print("obésité")
    else:
      print("IMC correct")

personne1 = Personne(1.8, 75, 24)
personne1.interpretation()

"""**Exercice 5 (secondaire) :**"""

class Article:

    def __init__(self, numero, nom, prix, quantite):
      self.numero = numero
      self.nom = nom
      self.prix = prix
      self.quantite = quantite

    def ToPrint(self):
      print("Numero : ", self.numero)
      print("Nom : ", self.nom)
      print("Prix : ", self.prix)
      print("Quantite : ", self.quantite)

class Stock:

    def __init__(self, id, liste_articles):
      self.id = id
      self.liste_articles = liste_articles

    def rechercher(self, numero, nom, intervalle_prix):
      if numero is not None:
        for article in self.liste_articles:
          if numero == article.numero:
            return article
        return False
      elif nom is not None:
        for article in self.liste_articles:
          if nom == article.nom:
            return article
        return False
      elif intervalle_prix is not None:
        for article in self.liste_articles:
          if article.prix >= intervalle_prix[0] and article.prix <= intervalle_prix[1]:
            return article
        return False

    def ajouter(self, article):
      if self.rechercher(article.numero, None, None) is not False:
        self.liste_articles.append(article)

    def supprimer(self, numero):
      article = self.rechercher(numero, None, None)
      self.liste_articles.remove(article)

    def affichage(self):
      for article in self.liste_articles:
        article.ToPrint()
      print("\n")

article1 = Article(0, "mangue", 4, 25)
article2 = Article(1, "salade", 1, 100)
article3 = Article(2, "radis", 1, 400)
article4 = Article(3, "pomme", 2, 100)
article5 = Article(4, "ananas", 5, 25)

liste_article = [article1, article2, article3, article4, article5]
stock1 = Stock(0, liste_article)

stock1.affichage()
article6 = stock1.rechercher(0, None, None)
article7 = stock1.rechercher(None, "ananas", None)
article8 = stock1.rechercher(None, None, [5, 10])
article6.ToPrint()
article7.ToPrint()
article8.ToPrint()
print("\n")
stock1.supprimer(1)
stock1.affichage()
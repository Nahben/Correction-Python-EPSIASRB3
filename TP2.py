# -*- coding: utf-8 -*-
"""
**Exercice 1 (clé) :**

=> Partie 1
"""

# a & b are integers
a = int(input("Valeur 1 : "))
b = int(input("Valeur 2 : "))

if a < b :
  print("Valeur la plus petite :", a)
else:
  print("Valeur la plus petite :", b)

print("Valeur la plus petite :", a) if a < b else print("Valeur la plus petite :", b)

"""=> Partie 2"""

a = int(input("Valeur 1 : "))
b = int(input("Valeur 2 : "))

if a < b :
  print("Valeur la plus petite :", a)
elif a == b:
  print("Les deux valeurs sont identiques")
else:
  print("Valeur la plus petite :", b)

"""**Exercice 2 (clé) :**"""

password="bonjour"

password_user = input("Veuillez saisir un mot de passe : ")

if password == password_user :
  print("Mot de passe correct")
else :
  print("Mot de passe incorrect")

"""**Exercice 3 (clé) :**

=> partie 1
"""

month = input("Veuillez saisir un mois de l'année :")

if (month == "janvier"):
    print(1)
elif (month == "février"):
    print(2)
elif (month == "fevrier"):
    print(2)
elif (month == "mars"):
    print(3)
elif (month == "avril"):
    print(4)
elif (month == "mai"):
    print(5)
elif (month == "juin"):
    print(6)
elif (month == "juillet"):
    print(7)
elif (month == "août"):
    print(8)
elif (month == "septembre"):
    print(9)
elif (month == "octobre"):
    print(10)
elif (month == "novembre"):
    print(11)
elif (month == "décembre"):
    print(12)
else :
    print("Erreur de saisi")

"""=> partie 2 (bonus)"""

month = input("Veuillez saisir un mois de l'année :").lower()

#month = month.lower()
#print(month)

if (month == "janvier"):
    print(1)
elif (month == "février"):
    print(2)
elif (month == "mars"):
    print(3)
elif (month == "avril"):
    print(4)
elif (month == "mai"):
    print(5)
elif (month == "juin"):
    print(6)
elif (month == "juillet"):
    print(7)
elif (month == "août"):
    print(8)
elif (month == "septembre"):
    print(9)
elif (month == "octobre"):
    print(10)
elif (month == "novembre"):
    print(11)
elif (month == "décembre"):
    print(12)
else :
    print("Erreur de saisi")

"""**Exercice 4 (secondaire):**"""

nbr = 10

if nbr % 2 == 0:
  print("Le nombre est pair")
else:
  print("Le nombre est impair")

"""**Exercice 5 (secondaire) :**"""

str1 = input("Veuillez saisir un mot : ")
str2 = input("Veuillez saisir un deuxième mot : ")

if len(str1) > len(str2):
  print("Le premier mot est le plus long")
elif len(str1) < len(str2):
  print("Le deuxième mot est le plus long")
else :
  print("Les deux mots font la même taille")

"""**Exercice 6 (secondaire) :**"""

voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
consonnes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
cara = input("Veuillez saisir un caractère : ")

if cara in voyelles :
  print("Le caractère saisi est une voyelle")
elif cara in consonnes :
  print("Le caractère saisi est une consonne")
else :
  print("Le caractère saisi n'est pas dans l'alphabet")

"""Solution alternative (dictionnaire)"""

alphabet = {'a':True, 'b':False, 'c':False, 'd':False, 'e':True, 'f':False, 'g':False, 'h':False, 'i':True, 'j':False, 'k':False, 'l':False, 'm':False, 'n':False, 'o':True, 'p':False, 'q':False, 'r':False, 's':False, 't':False, 'u':True, 'v':False, 'w':False, 'x':False, 'y':True, 'z':False}
cara = input("Veuillez saisir un caractère : ")

if cara in alphabet :
  if alphabet[cara]:
    print("Le caractère saisi est une voyelle")
  else :
    print("Le caractère saisi est une consonne")
else :
  print("Le caractère saisi n'est pas dans l'alphabet")
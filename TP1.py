""""

**Exercice 1 (clé) :**

Question 1
"""

print("Hello World")

"""Question 2"""

word = str(input("Mot :"))
print(word)

"""**Exercice 2 (clé) :**"""

a = 1
b = 2

# solution 1
c = b
b = a
a = c

print("a :", a)
print("b :", b)

a = 1
b = 2

# solution 2
a, b = b, a

print("a :", a)
print("b :", b)

"""**Exercice 3 (clé) :**"""

y = 2
x = y + 1

#solution 1
print(x)
print('\n') # permet un retour à la ligne

#solution 2
print("x est égal à", x, "\n")

#solution 2
print("x est égal à {}".format(x))

"""**Exercice 4 (clé) :**

=> Partie 1
"""

chaine="Hello World"
entier=10
decimal=4.2

# rappel : la fonction type() retourne le type d'une variable
print(type(chaine))
print(type(entier))
print(type(decimal))

"""=> Partie 2"""

chaine, entier, decimal = "Hello World", 10, 4.2

print(chaine, entier, decimal)

"""**Exercice 5 (secondaire) :**"""

entier = 10
chaine = "élèves"
somme = str(entier)+ " " + chaine

print (somme)
print (type(somme))

"""**Exercice 6 (secondaire) :**"""

h = float(input("Veuillez saisir la hauteur du rectangle h :"))
l = float(input("Veuillez saisir la longeur du rectangle l :"))

print(h*l)

"""**Exercice 7 (secondaire):**"""

from math import *

rayon_Ext = float(input("Rayon extérieur : "))
rayon_Int = float(input("Rayon intérieur : "))

sGrandDisque = pi * rayon_Ext**2
sDuTrou = pi * rayon_Int**2
surface = sGrandDisque - sDuTrou

print ("Surface du disque : ", surface)
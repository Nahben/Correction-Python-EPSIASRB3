"""
**Exercice 1 (clé) :**

=> Partie 1
"""
import random

for i in range (10):
  print("J'aime programmer avec Python !")

"""=> Partie 2"""

animaux = ["baleine", "chien", "chat", "brebis", "loup"]

for animal in animaux :
  print(animal)

#spacing
print('\n')

for i in range(len(animaux)) :
  print(animaux[i])

#spacing
print('\n')

for i in range(len(animaux)) :
  print("animal : ", animaux[i], '\n', "position : ", i, "\n")

"""**Exercice 2 (clé) :**"""

x = 0

while x <= 10 :
  print("valeur de x :", x)
  x += 1

nbr = int(input("Veuillez saisir un nombre : "))
print(nbr)

while nbr != 10 :
  nbr = int(input("Veuillez saisir un nombre : "))
  print(nbr)

"""**Exercice 3 (clé) :**"""

from random import *
nbr = random.randint(100)

nbr_input = int(input("Essayer de deviner le nombre :"))

while nbr_input != nbr :
  if nbr_input < nbr :
    print("Le nombre à trouver est plus grand")
  else :
    print("Le nombre à trouver est plus petit")
  nbr_input = int(input("Essayer un autre nombre : "))

print("Bravo vous avez trouvé le nombre !")

"""**Exercice 4 (clé) :**"""

print("*")

print("* "*20)

"""=> Partie 1"""

l = int(input("Veuillez saisir une longueur :"))
h = int(input("Veuillez saisir une largeur :"))

print('\n') # spacing

for i in range(h):
    print(('* ')*l)

l = int(input("Veuillez saisir une longeur :"))
h = int(input("Veuillez saisir une largeur :"))

print('\n') # spacing

for i in range(h):
    for j in range(l):
      print('* ', end='')
    print('')

"""=> Partie 2"""

l = int(input("Veuillez saisir une longeur :"))
h = int(input("Veuillez saisir une largeur :"))

symbol = str(input("Veuillez saisir un symbole :"))

print('\n') # spacing

if (len(symbol) == 1):
  for i in range(h):
    print((symbol+' ')*l)
else :
  print("Erreur de saisi")

"""**Exercice 5 (secondaire) :**"""

# Définition du caractère de remplissage
space = " "
# Définition du caractère de dessin du sapin
char_sapin = "^"
# Nombre de lignes constituant le sapin
nbre_ligne = 12
# Nombre de "blancs" à insérer avant le ^
padSize=nbre_ligne - 1
# Position actuelle en lignes dans le dessin du sapin
num_ligne = 0

# Saut d'un ligne pour ergonomie
print()

for num_ligne in range (1, nbre_ligne + 1):

  # Nombre de caractères sapin à dessiner
  if ( num_ligne == 1 ):
    nbre_char_sapin = 1
  else:
    nbre_char_sapin = 2 * num_ligne - 1

  # Affichage d'une ligne de sapin
  print( space * (padSize/2), char_sapin * nbre_char_sapin, space * (padSize/2))
  # Décrémenter le nombre de caractères de remplissage
  padSize -= 1

"""**Exercice 6 (ultime) :**"""

n = int(input())
hauteur = 2*n-1
largeur = hauteur
lv = 3
taille = 0

print('.' + ' ' * (hauteur/2) + '*')

for i in range(largeur-1,-1,-1):
    if taille < n-1:
        print(' '*i+'*'*lv)
    else:
        print(' '*i+'*'*(lv - 2*n)+' '*((2*n) - (lv - 2*n))+'*'*(lv - 2*n))

    taille += 1
    lv += 2
# -*- coding: utf-8 -*-
"""
## Partie 5 : Les fonctions

**Exercice 1 (clé) :**
"""

def mafonction(a, b):
  return (a+b)*2

x = 2
y = 4

print(mafonction(x, y))
print(mafonction(4, 6))

a = 2
b = 4

def moyenne(x, y):
  return (x+y)/2

print(moyenne(a, b))
print(moyenne(10, 5))

"""**Exercice 2 (clé) :**"""

def max(a, b):
  if a > b :
    return a
  else :
    return b

def min(a, b):
  if a < b :
    return a
  else :
    return b

nbr1 = int(input("Veuillez saisir un premier nombre : "))
nbr2 = int(input("Veuillez saisir un deuxième nombre : "))

print("max : ", max(nbr1, nbr2))
print("min : ", min(nbr1, nbr2))

def max(a, b):
  if a > b :
    return a
  else :
    return b

def min(a, b):
  if a < b :
    return a
  else :
    return b

nbr1 = int(input("Veuillez saisir un premier nombre : "))
nbr2 = int(input("Veuillez saisir un deuxième nombre : "))

if nbr1 == nbr2 :
  print("Les nombres sont égaux")
else :
  print("max : ", max(nbr1, nbr2))
  print("min : ", min(nbr1, nbr2))

"""**Exercice 3 (clé) :**

Question 1
"""

def aireTriangle(b, h):
  res_calcul = (1/2)*b * h
  return res_calcul

print(aireTriangle(3, 2))
print(aireTriangle(5, 4))

"""Question 2"""

import math

def pythagore(a, b):
  res_calcul = math.sqrt(a**2 + b**2)
  return res_calcul

print(pythagore(4, 4))
print(pythagore(5, 8))

"""**Exercice 4 (clé) :**

=> Question 1
"""

def getMax(list_nbr):
  max = 0
  for nbr in list_nbr:
    if abs(nbr) >= max :
      max = nbr
  return max

print(getMax([6, 9, 1, 2]))
print(getMax([10, 66, 12, 98]))
print(getMax([1, 1, 1, 1, 1]))

"""=> Question 2"""

def getSum(list_nbr):
  nbr_to_return = 0
  for nbr in list_nbr:
    nbr_to_return += nbr
  return nbr_to_return

print(getSum([6, 9, 1, 2]))
print(getSum([10, 66, 12, 98]))
print(getSum([1, 1, 1, 1, 1]))

"""=> Question 3"""

def getMean(list_nbr):
  return getSum(list_nbr)/len(list_nbr)

print(getMean([6, 9, 1, 2]))
print(getMean([10, 66, 12, 98]))
print(getMean([1, 1, 1, 1, 1]))

"""**Exercice 5 (secondaire) :**"""

def pair (nbr):
  if (nbr % 2 == 0):
    return True

def impair (nbr):
  if (nbr % 2 == 1):
    return True

nombre = int(input("Veuillez saisir un nombre : "))
if pair(nombre):
  print ("Le nombre est pair")
if impair(nombre):
  print ("Le nombre est impair")

def pair (nbr):
  if (nbr % 2 == 0):
    return True

nombre = int(input("Veuillez saisir un nombre : "))

if pair(nombre):
  print("Le nombre est pair")
else :
  print("Le nombre est impair")

"""**Exercice 6 (secondaire) :**"""

def compte_caracteres(ligne):
  counter = 0
  for cara in ligne :
    counter += 1
  return counter

ligne = str(input("Veuillez saisir une ligne : "))
print(compte_caracteres(ligne))

def compte_mots(ligne):
  counter = 0
  for cara in ligne :
    if cara == ' ':
      counter += 1
  counter += 1
  return counter

ligne = str(input("Veuillez saisir une ligne : "))
print(compte_mots(ligne))

"""**Exercice 7 (secondaire) :**

=> Question 1
"""

import random

def listGenerator(nbr):
  list_to_return = []

  while nbr >= 1:
    nbr_random = random.randint(1, nbr)
    print(nbr_random)
    list_to_return.append(nbr_random)
    nbr -= nbr_random
  return list_to_return

nbr = int(input("Veuillez saisir un nombre : "))
print("Voici une liste :", listGenerator(nbr))

"""=> Question 2"""

import random

def listGenerator(nbr):
  list_to_return = []

  while nbr > 1:
    nbr_random = random.randint(1, nbr)
    while nbr_random % 2 != 0:
      nbr_random = random.randint(1, nbr)
    list_to_return.append(nbr_random)
    nbr -= nbr_random
  return list_to_return

nbr = int(input("Veuillez saisir un nombre : "))
print("Voici une liste :", listGenerator(nbr))

"""**Exercice 8 (secondaire) :**"""

# -*- coding : utf8 -*-
"""Proportion d'une séquence dans une chaîne d'ADN."""

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def valide(seq) :
    """Retourne vrai si la séquence est valide, faux sinon."""
    ret = any(seq)
    for c in seq :
        ret = ret and c in "atgc"
    return ret

def proportion(a, s) :
    """Retourne la proportion de la séquence <s> dans la chaîne <a>."""
    return 100*a.count(s)/len(a)

def saisie(ch) :
    s = input("{:s} :".format(ch))
    while not valide(s) :
        print("'{:s}' ne peut contenir que les chaînons 'a', 't', 'g' et 'c'"
              " et ne doit pas être vide".format(ch))
        s = input("{:s} :".format(ch))
    return s

# Programme principal =========================================================
adn = saisie("chaîne")
seq = saisie("séquence")

print('Il y a {:.2f} % de"{:s}" dans votre chaîne.'
     .format(proportion(adn, seq), seq))
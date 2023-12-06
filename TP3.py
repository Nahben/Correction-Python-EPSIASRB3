"""
## Partie 3 : Les listes

**Exercice 1 (clé) :**
"""

week_days = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

print(week_days)
print(week_days[3])

week_days[5] = "dimanche"
print(week_days)

week_days[0], week_days[-1] = week_days[-1], week_days[0]

print(week_days)

day = week_days[0]
week_days[0] = week_days[6]
week_days[6] = day
print(week_days)

"""**Exercice 2 (clé) :**"""

list_nbr = [10, 20, 30, 40]

print(list_nbr)

list_nbr.append(1)
list_nbr.pop(0)
list_nbr.remove(40)
list_nbr.append(50)
print(list_nbr)

res_calcul = list_nbr[0] + list_nbr[1]
print(res_calcul)

if list_nbr[0] > list_nbr[-1] :
  print("Le premier élément de la liste est plus grand que le dernier élément de la liste")
elif list_nbr[0] == list_nbr[-1]:
  print("Le premier élément de la liste est égal au dernier élément de la liste")
else :
  print("Le premier élément de la liste est plus petit que le dernier élément de la liste")

"""**Exercice 3 (secondaire) :**"""

ligne = "Ceci est un test"

liste = ligne.split(" ")

print(liste)

"""**Exercice 4 (secondaire) :**"""

import random

students = ["Mathieu", "Max", "Jeanne", "Lola", "Victor", "Joris", "Emilie"]

random.shuffle(students)

print(students)

"""**Exercice 5 (secondaire) :**

=> Partie 1
"""

liste_nbr = []

nbr_ajouter = int(input("Veuillez saisir un nombre : "))
position_nbr = int(input("Veuillez saisir une position : "))
print(position_nbr)
print(len(liste_nbr))
if position_nbr <= len(liste_nbr):
  liste_nbr.insert(position_nbr, nbr_ajouter)
  print("Voici la liste : ", liste_nbr)
else :
  print("Position incorrect")

"""=> Partie 2"""

liste_nbr = [10, 20]
print(len(liste_nbr))

choix_utilisateur = input("Veuillez choisir entre le mode supprimer et ajouter :")

if choix_utilisateur == "ajouter" :
  if len(liste_nbr) == 0 :
    nbr_ajouter = int(input("Veuillez saisir un nombre : "))
    liste_nbr.append(nbr_ajouter)
    print("Voici la liste : ", liste_nbr)
  else :
    nbr_ajouter = int(input("Veuillez saisir un nombre : "))
    position_nbr = int(input("Veuillez saisir une position : "))
    print(position_nbr)
    print(len(liste_nbr))
    if position_nbr <= len(liste_nbr):
      liste_nbr.insert(position_nbr, nbr_ajouter)
      print("Voici la liste : ", liste_nbr)
    else :
      print("Position incorrect")
elif choix_utilisateur == "supprimer" and len(choix_utilisateur) > 0 :
 nbr_supprimer = int(input("Veuillez saisir un nombre : "))
 liste_nbr.remove(nbr_supprimer)
 print("Voici la liste : ", liste_nbr)
else :
  print("Erreur")
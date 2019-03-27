#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:55:23 2019

@author: telu
"""


# %% 1)
def liste_puissance(p, n):
    return [i**p for i in range(n)]


print('Question 1)')
print(liste_puissance(1, 5), liste_puissance(2, 10))


# %% 2)
def dernier_chiffre(i):
    i_str = str(i)     # Transformation de i en string
    c_str = i_str[-1]  # Dernier chiffre, sous format string
    c = int(c_str)     # Conversion du dernier chiffre en entier
    return c


print('Question 2)')
print(dernier_chiffre(50), dernier_chiffre(123),
      dernier_chiffre(12)+dernier_chiffre(53))


# %% 3)
def liste_magique(p, n):
    return [dernier_chiffre(i) for i in liste_puissance(p, n)]


print('Question 3)')
print(liste_magique(1, 5), liste_magique(2, 10))

# %% 4)
print('Question 4)')
print('- Affichage des listes magiques pour les premiers nombres pairs')
n = 10
for p in range(2, 13, 2):
    print(liste_magique(p, n))
print('=> une fois sur deux, les chiffres sont les memes')
print('- Affichage de la somme des listes magiques pour deux nombres pairs consecutifs')
for p in [2, 6]:
    liste1 = liste_magique(p, n)
    liste2 = liste_magique(p+2, n)
    liste = []
    for i in range(n):
        liste.append(liste1[i] + liste2[i])
    print(liste)
print('=> les sommes sont toujours les mêmes')

# %% 5)
print('Question 5)')
print('- Affichage des listes magiques pour les premiers nombres pairs')
n = 10
for p in range(1, 12, 2):
    print(liste_magique(p, n))
print('=> pour 1, 5, 9, ..., les chiffres sont les memes et vont de 1 a 9, dans le bon ordre')
print('=> pour 3, 7, 11, ..., les chiffres sont les memes et vont de 1 a 9, mais pas dans le bon ordre')

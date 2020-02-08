# coding: utf-8
# CC BY-NC-SA 4.0 - 2020 - Jean-Hugues Roy (https://creativecommons.org/licenses/by-nc-sa/4.0/)

### POUR APPRENTISSAGE DE:
### LECTURE DE CSV 

# PYTHON «VANILLE» NE FAIT PAS TOUT
# IL EST PARFOIS NÉCESSAIRE D'IMPORTER DES MODULES
# POUR Y AJOUTER DES FONCTIONNALITÉS
# ICI, ON IMPORTE LE MODULE PERMETTANT DE GÉRER LES FICHIERS CSV

import csv

# NE PAS NOMMER VOS SCRIPTS DU NOM DES MODULES
# --->>> ICI, NE PAS APPELER VOTRE SCRIPT csv.py
# PCQ LE SCRIPT VA TENTER DE S'IMPORTER LUI-MÊME ET ÇA CAUSE ERREUR FATALE TERRIBLE

# ON VA MAINTENANT LIRE UN FICHIER CSV
# SAQ ACCESSIBLE À CET URL -> http://bit.ly/edm5240saq
# CONTIENT PLUS D'UN DEMI-MILLION DE LIGNES (624 547)
# IL FAUT PLACER CE FICHIER
# DANS LE MÊME RÉPERTOIRE QUE CELUI DANS LEQUEL VOTRE SCRIPT EST SAUVEGARDÉ

# ENSUITE, ON PEUT PLACER LE NOM DU FICHIER CSV DANS UNE VARIABLE

fichier = "saq.csv"

# ON L'OUVRE ET ON LE PLACE DANS UN OBJET PYTHON TEMPORAIRE

f1 = open(fichier)

# LE TRAVAIL N'EST PAS FINI.
# IL FAUT TRAITER NOTRE OBJET DANS UNE MÉTHODE DU MODULE CSV APPELÉE READER
# QUI VA LIRE NOTRE OBJET ET TOUT PLACER
# DANS UNE VARIABLE QU'ON PEUT APPELLER «lignes»

lignes = csv.reader(f1)

# PETIT TRUC POUR ESCAMOTER LES ENTÊTES
next(lignes)

# CELA CRÉÉE UNE IMMENSE LISTE DE LISTES
# OÙ CHAQUE LIGNE DE NOTRE CSV EST L'UNE DE CES LISTES
# ON PEUT DONC EXAMINER CHACUNE DES LIGNES AVEC UNE BOUCLE

for ligne in lignes:
	print(ligne)

# CE QUI PERMET D'ALLER EN CHERCHER DES ÉLÉMENTS PRÉCIS
# LA COMMANDE CI-DESSOUS PERMET D'AFFICHER
# LA 4E COLONNE DE CHACUNE DES LIGNES DE NOTRE CSV
	print(ligne[3])

# ON PEUT COMPTER LE NOMBRE DE LIGNES QU'ON A AVEC UN COMPTEUR

total = 0

for ligne in lignes:
	total += 1
	print("On a {} produits".format(total))

# COMPTEUR PRATIQUE SI ON VEUT VOIR QUELLE EST
# LA PROPORTION D'UN ÉLÉMENT SUR LE TOTAL

##### EXERCICE 1

# PAR EXEMPLE, QUEL % DES PRODUITS VENDUS À LA SAQ
# VIENNENT DE FRANCE, DU CANADA OU DES USA?

fr = 0
ca = 0
us = 0

for ligne in lignes:
	total += 1
	if ligne[3] == "France":
		fr += 1
	elif ligne[3] == "Canada":
		ca += 1
	elif ligne[3] == "États-Unis":
		us += 1

# POUR AVOIR LE NOMBRE TOTAL

print("Sur {} produits à la SAQ, {} sont français {} sont canadiens et\
{} sont américains".format(total, fr, ca, us))

# MAIS LA PROPORTION?
# ON PEUT SE SERVIR DE LA FONCTION «round()» POUR ARRONDIR

print("Sur {} produits à la SAQ, {}% sont français {}% sont canadiens et \
{}% sont américains".format(
	total,
	round(fr/total*100,2),round(ca/total*100,2),
	round(us/total*100,2),
	))

##### EXERCICE 2

# SI ON VOULAIT CALCULER TOUT L'INVENTAIRE DE LA SAQ?

# ON CRÉÉ UNE VARIABLE QUI VA FAIRE LA SOMME AU FUR ET À MESURE
# QU'ON VA CHERCHER LA VALEUR DE CHAQUE PRODUIT
# ATTENTION -->> IL FAUT CONVERTIR NOTRE ligne-5 EN «float»
# 			POUR L'UTILISER DANS LE CALCUL QUI S'EN VIENT
# ATTENTION2 -->> IL FAUT CONVERTIR NOTRE ligne-6 EN «int»
# ET ATTENTION ENCORE > CONVERTIR EN «str» POUR AFFICHER LE TOUT

inventaire = 0
for ligne in lignes:
	print(float(ligne[5]))
	inventaire = inventaire + float(ligne[5]) * int(ligne[6])
	print(inventaire)

print("La valeur de l'inventaire de la SAQ est de " +
str(round(inventaire)) + ".00 $")

# coding utf-8
# License Creative Commons CC-BY-NC - 2020 - Jean-Hugues Roy
# https://creativecommons.org/licenses/by-nc/4.0/legalcode.fr

### Les données pour ce tutoriel sont accessibles ici:
### http://bit.ly/crtc_jhr
### Il s'agit de 493 des commentaires laissés en français sur le site du CRTC au sujet de la demande de renouvellement de licence de CBC/Radio-Canada

### MODULES À IMPORTER POUR SE SERVIR DE NLTK
import csv
from collections import Counter ### Pour compter les fréquences

import nltk
import string ### -> pour gérer la ponctuation
from nltk.tokenize import word_tokenize ### -> pour faire de la "tokenisation"
from nltk.stem import SnowballStemmer ### -> pour faire de la racinisation
from nltk.corpus import stopwords ### -> pour gérer les mots vides

### On place le fichier dans le même répertoire et on en place le nom dans une variable au nom pertinent
crtc = "crtc-francais.csv"

### Et on lit le fichier
f = open(crtc)
interventions = csv.reader(f)
next(interventions)

### Deux listes qu'on crée au besoin si on veut compter des fréquences de mots
# tousMots = []
# bigrams = []

### Notre boucle principale pour traiter chacun des lignes de notre CSV
for inter in interventions:

	### Vous pouvez "décommenter" chaque bloc qui suit pour faire le traitement que vous avez besoin de faire avec votre texte.
	
	### TOKENS

	### Pour utiliser NLTK, il faudra peut-être que vous téléchargiez un module supplémentaire
	### La procédure, ici, est d'aller dans le terminal et de taper "python" ou "python3"
	### Puis, devant les trois ">" vous entrez >>> import nltk
	### Puis vous entrez >>> nltk.download('punkt')
	### Et vous sortez de python avec "exit()"

	### Le texte qu'on veut traiter se trouve dans le 15 élément de la liste "inter"
	### C'est donc sur ce texte qu'on va appliquer la fonction "word_tokenize"

	# tokens = word_tokenize(inter[14])
	# print(tokens)

	### LEMMATISATION -> Trop imparfait avec NLTK, donc on oublie... On va plutôt faire de la :
	### RACINISATION

	# fr = SnowballStemmer('french')
	# racines = [fr.stem(mot) for mot in word_tokenize(inter[14])]
	# print(racines)

	### ÉTIQUETTAGE (TAGGING)
	### Compliqué, sous NLTK, et peu adapté au français -> nécessite l'installation d'autres outils extérieurs... donc ici aussi, on oublie ça...

	### MOTS VIDES AVEC NLTK

	### Pour utiliser NLTK, il faudra aussi que vous téléchargiez un module supplémentaire, comme ci-dessus
	### La procédure, ici, est d'aller dans le terminal et de taper "python" ou "python3"
	### Puis, devant les trois ">" vous entrez >>> import nltk
	### Puis vous entrez >>> nltk.download('stopwords')
	### Et vous sortez de python avec "exit()"

	# tokens = [mot for mot in word_tokenize(inter[14]) if mot not in stopwords.words('french')]
	# print(tokens)

	### RETRANCHER PONCTUATION (ET MOTS VIDES AUSSI)

	# tokens = [mot for mot in word_tokenize(inter[14]) if mot not in stopwords.words('french') and mot not in string.punctuation] ### -> Requiert l'ajout de "import string" en haut
	# print(tokens)

	### COMPTER FRÉQUENCES

	### On peut commencer par choisir selon quels critères on veut sélectionner nos mots
	# mots = [fr.stem(mot) for mot in word_tokenize(inter[14]) if mot not in stopwords.words('french') and mot not in string.punctuation]
	# print(mots)
	# print("#"*80) ### -> petit séparateur décoratif

	### MOTS SEULS

	### On place chaque "racine" (on aurait aussi pu choisi des "tokens") dans une grande liste qui est en quelque sorte un "sac de mots" de toutes les formes lexicales que nous estimons pertinentes pour notre analyse
	# for mot in mots:
	# 	tousMots.append(mot)

### IMPRESSION DES RÉSULTATS UNE FOIS LA BOUCLE COMPLÉTÉE
# freq = Counter(tousMots)
# print(freq.most_common(25))
# print(len(tousMots))

	### PAIRES DE MOTS (OU BIGRAMMES)

	### On crée des paires avec cette syntaxe
	# for x, y in enumerate(mots[:-1]): ### -> enumerate permet de faire des itérations sur l'index d'une liste; ici, les valeurs de x et de y seront respectivement le numéro d'index et l'élément (par exemple: 0, moi; 1, richard; 2, martineau; 3, je; 4, déclare; etc...)
		### Et on place chaque paire dans un autre "sac de mots", mais en fait, un "sac de paires de mots"
		# bigrams.append("{} {}".format(mots[x],mots[x+1]))
	# print(bigrams)

### IMPRESSION DES RÉSULTATS UNE FOIS LA BOUCLE COMPLÉTÉE
# freq = Counter(bigrams)
# print(freq.most_common(25))
# print(len(bigrams))





# coding utf-8
# License Creative Commons CC-BY-NC - 2020 - Jean-Hugues Roy
# https://creativecommons.org/licenses/by-nc/4.0/legalcode.fr

### Les données pour ce tutoriel sont accessibles ici:
### http://bit.ly/crtc_jhr
### Il s'agit de 493 des commentaires laissés en français sur le site du CRTC au sujet de la demande de renouvellement de licence de CBC/Radio-Canada

### IMPORTATION DES MODULES NÉCESSAIRES POUR UTILISER SPACY

import csv, spacy
from collections import Counter ### Pour compter les fréquences

### On place le fichier dans le même répertoire et on en place le nom dans une variable au nom pertinent
crtc = "crtc-francais.csv"

### Et on lit le fichier
f = open(crtc)
interventions = csv.reader(f)
next(interventions)

### On charge le réseau neuronal qui contient le modèle de petite taille que spaCy a mis au point pour analyser la langue française
tal = spacy.load("fr_core_news_md")
# tal = spacy.load("fr_core_news_sm") ### -> SpaCy dispose aussi d'un modèle de petite taille. Il est significativement plus rapide à charger, mais peut-être moins précis. Pour s'en servir, il faut bien sûr le télécharger en amont.

### Ajouter des mots vides, au besoin
# tal.Defaults.stop_words.add("y")

### Retrancher des mots vides, au besoin
# tal.Defaults.stop_words.remove("gens")

### Deux listes qu'on crée au besoin si on veut compter des fréquences de mots
# tousMots = []
# bigrams = []

### Notre boucle principale pour traiter chacun des lignes de notre CSV
for inter in interventions:

	### Le texte qu'on veut traiter se trouve dans le 15 élément de la liste "inter"
	### On utilise notre modèle pour traiter le texte et on place le résultat dans un variable qu'on peut appeler "doc"
	### La variable va être utile pour toutes les opérations qui suivront
	doc = tal(inter[14])

	### Vous pouvez "décommenter" chaque bloc qui suit pour faire le traitement que vous avez besoin de faire avec votre texte.

	### TOKENS

	# tokens = [token.text for token in doc] ### La liste "tokens" est ici créée à l'aide d'une "list comprehension", une façon plus complexe, mais qui tient en une seule ligne
	# print(tokens)
	# print(len(tokens))

	### LEMMATISATION

	# lemmes = [token.lemma_ for token in doc]
	# print(lemmes)
	# print(len(lemmes))

	### ÉTIQUETTAGE (TAGGING)

	# tags = [token.tag_ for token in doc]
	# print(tags)
	# print(len(tags))

	### ".pos_" donne un étiquettage plus simple
	# tags = [token.pos_ for token in doc]
	# print(tags)
	# print(len(tags))

	### Pour voir les mots et leur étiquette
	# for token in doc:
		# print("«{}», «{}» \t {} {}".format(token.text, token.lemma_, token.pos_, token.tag_))
		# print("."*10)

	### MOTS VIDES

	# tokens = [token.text for token in doc if token.is_stop == False]
	# print(tokens)
	# print(len(tokens))

	### RETRANCHER PONCTUATION (ET MOTS VIDES AUSSI)

	# # mots = [token.text for token in doc if token.is_stop == False and token.is_punct == False]
	# mots = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False] ### Même syntaxe mais avec mots lemmatisés
	# print(mots)
	# print(len(mots))

	### COMPTER FRÉQUENCES

	### On peut commencer par choisir selon quels critères on veut sélectionner nos mots
	# mots = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False] ### Même syntaxe mais avec mots lemmatisés
	# print(mots)
	# print("#"*80) ### -> petit séparateur décoratif

	### MOTS SEULS

	### On place chaque "token" ou "lemme" dans une grande liste qui est en quelque sorte un "sac de mots" de toutes les formes lexicales que nous estimons pertinentes pour notre analyse
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





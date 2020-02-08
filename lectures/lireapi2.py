# coding: utf-8
# CC BY-NC-SA 4.0 - 2020 - Jean-Hugues Roy (https://creativecommons.org/licenses/by-nc-sa/4.0/)

### POUR LIRE DES API EN DIRECT SUR LE WEB
### ET ENSUITE CRÉER DES CSV

### MAIS D'ABORD -> QU'EST-CE QU'UN API?
# C'EST UNE INTERFACE DE PROGRAMMATON (APPLICATION PROGRAMMING INTERFACE EN ANGLAIS)
# LA PLUPART DES OUTILS QUE VOUS UTILISEZ QUOTIDIENNEMENT (FACEBOOK, INSTA, TWITCH, ETC.)
# SONT EN FAIT D'IMMENSES BASES DE DONNÉES
# LEUR PAGE WEB OU APPLICATIONS MOBILES SONT DES INTERFACES POUR LES HUMAINS
# PLUSIEURS DE CES SERVICES ONT AUSSI UNE INTERFACE POUR LES ORDINATEURS: C'EST LEUR API

### >>> EXEMPLE AVEC SPOTIFY
### ALLER À https://developer.spotify.com/ > CONSOLE
### SEARCH
### BROWSE > RECOMMENDATIONS

# IL FAUT D'ABORD IMPORTER DES MODULES COMPLÉMENTAIRES

# JSON POUR TRAITER DES FICHIERS DE DONNÉES «.json», LE FORMAT LE PLUS COURAMMENT UTILISÉ PAR LES API
# JSON COMPREND À LA FOIS DES DICTIONNAIRES ET DES LISTES

import json

# ON IMPORTE AUSSI CSV CAR ON VA, AU FINAL, CRÉER UN FICHIER CSV

import csv

# ON IMPORTE UN MODULE POUR INTERAGIR AVEC UN SERVEUR WEB
# COMME ON FAIT DES REQUÊTES SUR LE WEB, CE MODULE S'APPELLE «requests»

import requests

# ON DÉTERMINE TOUT DE SUITE LE NOM QU'AURA NOTRE FICHIER CSV ET ON PLACE CE NOM DANS UNE VARIABLE

fichier = "chansons.csv"

# VOICI L'URL QU'ON VA CONSULTER
# VOUS POUVEZ LA COPIER-COLLER DANS UN NAVIGATEUR (FIREFOX, CHROME, ETC)
# C'EST UN FICHIER JSON DES MÉTADONNÉES D'UNE CHANSON ARCHIVÉE À BANQ:
# ALLEZ À http://bit.ly/jhrbanq

url = "http://collections.banq.qc.ca/api/service-notice?handle=52327/524"

# MONTRER QUE LE CHARABIA QUI EST LÀ EST COMPRÉHENSIBLE
# C'EST DU BON VIEUX JSON

# ÉTHIQUE APPLIQUÉE AU MOISSONNAGE DE DONNÉES
# ON FAIT DU JOURNALISME À VISIÈRE LEVÉE
# IL EST DONC SOUHAITABLE DE S'IDENTIFIER QUAND ON COGNE À LA PORTE D'UN SERVEUR

entete = {
	"User-Agent":"Jean-Hugues Roy - 514/778-6102",
	"From":"roy.jean-hugues@uqam.ca"
}

# ON UTILISE LA MÉTHODE «.get» DU MODULE REQUESTS AVEC DEUX PARAMÈTRES:
# L'URL DONT ON FAIT LA REQUÊTE
# ET LES ENTÊTES QUI ACCOMPAGNENT NOTRE REQUÊTE
# ON PLACE LE RÉSULTAT DANS UNE VARIABLE TEMPORAIRE QU'ON PEUT APPELER «req»

req = requests.get(url,headers=entete)

# ON PEUT VÉRIFIER CE QU'ELLE CONTIENT

print(req)

# ON VOIT LE STATUT DE NOTRE REQUÊTE
# 200 SIGNIFIE QUE ÇA FONCTIONNE
# 404 SIGNIFIE QUE LE CONTENU N'EST PAS DISPONIBLE (ESSAYEZ DE CHANGER LE 524 PAR 514)
# 500 SIGNIFIE UNE ERREUR DU SERVEUR (CHANGEZ LE 524 PAR 523)

# ON PEUT DONC FAIRE UN TEST POUR VOIR SI NOTRE REQUÊTE FONTIONNE
# SI LE STATUT N'EST PAS 200, C'EST QUE ÇA NE MARCHE PAS

if req.status_code != 200:
	print("Ça marche pas")

# SINON, C'EST QUE LE STATUT EST 200, ALORS ON PEUT EXTRAIRE LES DONNÉES DE L'API

else:

	# ON COMMENCE PAR TRAITER LE CONTENU DE NOTRE VARIABLE «REQ» AVEC LE MODULE JSON
	# ET ON LE PLACE DANS UNE VARIABLE

	toune = req.json()

	# ON PEUT VÉRIFIER CE QUE NOTRE VARIABLE CONTIENT. C'EST DU CHARABIA.

	print(toune)

	# EN FAIT, CET API NOUS RETOURNE DU JSON QUI COMPREND DES DICTIONNAIRES ET DES LISTES.
	# VOICI UN EXEMPLE DE DICTIONNAIRE QUI CONTIENT LE TITRE DE LA CHANSON

	# {
	# 	"titre":"À demain Une blague / [enregistrement sonore] ; [interprété par] Hector Pellerin de Montréal"
	# }

	# SI, DANS LES LISTES OU LES LISTES, L'INDEX EST UN NOMBRE (DE 0 À ...), DANS LES DICTIONNAIRES, L'INDEX EST COMPOSÉ PAR LA CLÉ.
	# POUR L'AFFICHER, ON PEUT AINSI ÉCRIRE:

	print(toune["titre"])

	# LES DICTIONNAIRES PEUVENT ÊTRE COMPLEXES:

	# "bitstreams":{"racine":{"fils":[{"type":"f","designation":"Face A  À demain","pbsid":"xALrTlJSGZep3nKvgYFJ5g","formats":[{"id":"xALrTlJSGZep3nKvgYFJ5g","format":"m4a","url":"http://collections.banq.qc.ca/bitstream/52327/524/1/494377a.m4a","diffusable":true,"masque":false,"principale":true,"mimeType":"audio/m4a","restriction":{"masque":false,"op":false,"accesException":true,"accesRestriction":false,"msgCode":""}}]},{"type":"f","designation":"Face B  Une blague","pbsid":"0Ed_Zb7x3P22ejyhw2Fqjg","formats":[{"id":"0Ed_Zb7x3P22ejyhw2Fqjg","format":"m4a","url":"http://collections.banq.qc.ca/bitstream/52327/524/2/494377b.m4a","diffusable":true,"masque":false,"principale":true,"mimeType":"audio/m4a","restriction":{"masque":false,"op":false,"accesException":true,"accesRestriction":false,"msgCode":""}}]}]},"restriction":{"masque":true}},

	# ON PEUT AMÉLIORER L'AFFICHAGE ("BEAUTIFY") :

	# "bitstreams": {
    #     "racine": {
    #         "fils": [
    #             {
    #                 "type": "f",
    #                 "designation": "Face A  À demain",
    #                 "pbsid": "xALrTlJSGZep3nKvgYFJ5g",
    #                 "formats": [
    #                     {
    #                         "id": "xALrTlJSGZep3nKvgYFJ5g",
    #                         "format": "m4a",
    #                         "url": "http://collections.banq.qc.ca/bitstream/52327/524/1/494377a.m4a",
    #                         "diffusable": true,
    #                         "masque": false,
    #                         "principale": true,
    #                         "mimeType": "audio/m4a",
    #                         "restriction": {
    #                             "masque": false,
    #                             "op": false,
    #                             "accesException": true,
    #                             "accesRestriction": false,
    #                             "msgCode": ""
    #                         }
    #                     }
    #                 ]
    #             },
    #             {
    #                 "type": "f",
    #                 "designation": "Face B  Une blague",
    #                 "pbsid": "0Ed_Zb7x3P22ejyhw2Fqjg",
    #                 "formats": [
    #                     {
    #                         "id": "0Ed_Zb7x3P22ejyhw2Fqjg",
    #                         "format": "m4a",
    #                         "url": "http://collections.banq.qc.ca/bitstream/52327/524/2/494377b.m4a",
    #                         "diffusable": true,
    #                         "masque": false,
    #                         "principale": true,
    #                         "mimeType": "audio/m4a",
    #                         "restriction": {
    #                             "masque": false,
    #                             "op": false,
    #                             "accesException": true,
    #                             "accesRestriction": false,
    #                             "msgCode": ""
    #                         }
    #                     }
    #                 ]
    #             }
    #         ]
    #     },
	#         "restriction": {
    #         "masque": true
    #     }
    # },

	# IL Y A DEUX URL ENFOUIS PROFONDÉMENTS, MAIS QUI NOUS INTÉRESSENT. ESSAYONS PROGRESSIVEMENT DE S'EN RAPPROCHER.

	print(toune["bitstreams"])
	print(toune["bitstreams"]["racine"])
	print(toune["bitstreams"]["racine"]["fils"])
	print(len(toune["bitstreams"]["racine"]["fils"]))
	print(toune["bitstreams"]["racine"]["fils"][0]) # FACE A
	print(toune["bitstreams"]["racine"]["fils"][1]) # FACE B

	# DANS UN API, ON RETROUVE EN GÉNÉRAL TOUJOURS LA MÊME STRUCTURE
	# LES DICTIONNAIRES SONT GÉNÉRALEMENT TOUJOURS À LA MÊME PLACE ET ONT UN CONTENU QUI A LA MÊME STRUCTURE
	# LES LISTES AUSSI, MAIS LE NOMBRE D'ÉLÉMENTS QU'ELLES CONTIENNENT PEUT CHANGER

	for fil in toune["bitstreams"]["racine"]["fils"]:
		# print(fil)
		print(fil["formats"][0]["url"])

# MAINTENANT, SI ON SOUHAITAIT ALLER CONSIGNER LES INFORMATIONS CONTENUES PAR CET API SUR TOUTES LES CHANSONS, QUE POURRAIT-ON FAIRE?

# UNE BOUCLE, UN PEU COMME ON L'A FAIT AVEC LE MONTRÉAL CAMPUS, DANS LAQUELLE LE DERNIER ÉLÉMENT VARIERAIT DE 524 À 1700, HISTOIRE DE TESTER TOUS LES NUMÉROS POSSIBLES.

# ON VA LE FAIRE AVEC UN PLUS PETIT NOMBRE -> DE 524 À 550:

nombres = list(range(524,551))

# ON VA PRENDRE LA PARTIE QUI NE CHANGE PAS DE L'URL DE L'API:

urlDebut = "http://collections.banq.qc.ca/api/service-notice?handle=52327/"

# ON VA AUSSI SE CRÉER AUSSI UN PETIT COMPTEUR

n = 0

# PUIS ON VA CRÉER UNE BOUCLE:

for nb in nombres:
	url = urlDebut + str(nb)
	print(url)

	# CHAQUE URL CONTENANT DES INFOS SUR UNE CHANSON, ON VA CONSIGNER CES INFOS DANS UNE LISTE QU'ON POURRAIT APPELER "INFOS" OU "CHANSON", LISTE VIDE POUR LE MOMENT...

	chanson = []

	# ON FAIT LA MÊME REQUÊTE QUE TOUT À L'HEURE (NOS ENTÊTES SONT TOUJOURS LÀ):

	req = requests.get(url,headers=entete)

	# ON FAIT LA MÊME VÉRIFICATION QUE TOUT À L'HEURE POUR VOIR SI L'URL AUQUEL ON TENTE DE SE CONNECTER EST BON:

	if req.status_code != 200:
		print("Ça marche pas avec le #{}".format(nb))

	else:

		# ON ANALYSE ("PARSE") LE JSON QUI NOUS EST RETOURNÉ PAR L'API ET ON LE MET DANS UNE VARIABLE AU NOM RECONNAISSABLE:

		toune = req.json()

		# ON VA AJOUTER 1 À NOTRE COMPTEUR, PUIS, ON VA AJOUTER CE NOMBRE À NOTRE LISTE "chanson", AINSI QUE NOTRE VARIABLE "nb", HISTOIRE DE FACILITER LE SUIVI EN CAS DE PÉPIN.

		n += 1
		chanson.append(n)
		chanson.append(nb)

		# C'EST ICI QU'ON VA RAMASSER DIFFÉRENTES INFORMATIONS POUR CHAQUE CHANSON
		# SON TITRE (QU'ON VA AUSSI AJOUTER À LA LISTE "chanson")

		titre = toune["titre"]
		chanson.append(titre)

		# SA DATE

		date = toune["dateCreation"]
		chanson.append(date)

		# SON AUTEUR/INTERPRÈTE

		auteur = toune["createurs"][0]
		chanson.append(auteur)

		# UNE DESCRIPTION DU SUPPORT SUR LEQUEL SE TROUVE LA CHANSON

		support = toune["descriptionMat"]
		chanson.append(support)

		# ENFIN, ON VA AJOUTER LES DEUX URLS DES CHANSONS DE CE QUI EST EST FAIT UN API QUI DÉCRIT DES DISQUES

		if len(toune["bitstreams"]["racine"]["fils"]) > 1:
			faceA = toune["bitstreams"]["racine"]["fils"][0]["formats"][0]["url"]
			faceB = toune["bitstreams"]["racine"]["fils"][1]["formats"][0]["url"]
			chanson.append(faceA)
			chanson.append(faceB)
		else:
			faceA = toune["bitstreams"]["racine"]["fils"][0]["formats"][0]["url"]
			chanson.append(faceA)
			chanson.append("")
		
		print(chanson)
		print("~"*33) # LIGNE POUR SÉPARER LES CHANSONS

		# TOUT VA BIEN. ON PEUT AJOUTER LE CONTENU DE CETTE LISTE AU CSV DONT ON A DÉFINI LE NOM AU DÉBUT DU SCRIPT
		# ON COMMENCE PAR SE CRÉER UNE 1RE VARIABLE TEMPORAIRE QUI OUVRE NOTRE FICHIER AVEC LA FONCTION «OPEN»
		# IL Y A 2 PARAMÈTRES DANS CETTE FONCTION: LE NOM DU FICHIER, D'ABORD, PUIS LE MODE.
		# ICI, «a», SIGNIFIE QU'ON ÉCRIT DANS NOTRE FICHIER EN MODE «APPEND»
		# C'EST-À-DIRE QUE LA LIGNE QU'ON AJOUTE VA S'ADJOINDRE AU CONTENU DÉJÀ EXISTANT
		# PAR DÉFAUT, LE MODE EST «w» ET CELA EFFACE TOUT LE CONTENU QUI EST DÉJÀ DANS NOTRE FICHIER. ON NE VEUT PAS CELA.
	
		dead = open(fichier,"a")

		# ON UTILISE ENSUITE LA MÉTHODE «.writer()» DU MODULE CSV POUR SE CRÉER UNE 2E VARIABLE TEMPORAIRE À PARTIR DE NOTRE PREMIÈRE.
		# LE POURQUOI 
		obies = csv.writer(dead)
		obies.writerow(chanson)

		# DEUX CHOSES IMPORTANTES À RETENIR:
		# -> LA FONCTION OPEN DOIT PRENDRE LE PARAMÈTRE «a»
		# ÇA, C'EST LE MODE D'ÉCRITURE QUE VOUS DÉFINISSEZ
		# «A» SIGNIFIE «APPEND», CE QUI VEUT DIRE QUE QUE LA LIGNE QU'ON AJOUTE VA S'ADJOINDRE AU CONTENU DÉJÀ EXISTANT
		# PAR DÉFAUT, LE MODE EST «w» ET CELA EFFACE TOUT LE CONTENU QUI EST DÉJÀ DANS NOTRE FICHIER. ON NE VEUT PAS CELA.
		# -> 2E CHOSE, À LA DERNIÈRE LIGNE, LE PARAMÈTRE DE LA MÉTHODE «writerow» EST LE NOM DE LA LISTE QUI CONTIENT LES INFORMATIONS/DONNÉES QU'ON A UTILISÉE PLUS HAUT

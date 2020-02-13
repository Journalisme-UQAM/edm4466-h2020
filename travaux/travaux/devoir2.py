# coding : utf-8

# On importe tout ce dont on a besoin
import requests, json, csv

# On crée une variable dans laquelle on va mettre l'adresse du site auquel on va se connecter.
api = "http://jhroy.ca/uqam/lobby.json"

# On crée aussi une variable qui va contenir le fichier CSV de nos résultats à la fin:
lobbyClimatique = "lobbyclimatique.csv"

# Il est toujours éthique de faire du journalisme à visière levée et, donc, on va se présenter.

entetes = {
    "User-Agent":"JH Roy, bourreau d'étudiants en journalisme",
    "From": "514/778-6102 pour les plaintes"
    }

# On utilise requests pour "get" le contenu de l'URL contenu dans la variable "api"
req = requests.get(api, headers=entetes)

# Petit test pour voir si ça fonctionne
print(req.status_code)

# On "parse", ou traite, le contenu du site web auquel on se connecte avec le module "json", parce qu'on sait qu'il s'agit de données dans ce format et on le place dans une autre variable
tout = req.json()

# Dans la description du devoir2, je vous disais comment mon api maison était structuré:
# Il est d'abord fait d'une clé, "registre", dont la valeur est une liste.
# Pour vérifier combien d'éléments contient cette liste, voici ce qu'on pouvait faire:
print(len(tout["registre"]))

# Comme on a affaire à une liste, on peut y faire une boucle
for element in tout["registre"]:
    # print(element) # après une première impression aux fins de vérification, j'ai mis cet affichage en commentaire

# Je vous disais que chacun de ces 71 997 éléments était une autre liste, elle-même composée de trois éléments.

# Le premier élément (l'élément 0) de chacune de ces listes contient un dictionnaire donnant des informations sur la compagnie ou le groupe qui fait du lobbying
    # print(element[0]) # ici aussi, après une première impression aux fins de vérification, j'ai mis cet affichage en commentaire

# Le deuxième élément (l'élément 1) de chacune de ces listes contient une autre liste donnant, cette fois, des informations sur sur l'objet du lobbying
# On peut donc faire une petite boucle dans ce deuxième élément:
    for sujet in element[1]:
        # print(sujet) # affichage aux fins de vérification en cours de rédaction du script ;)

        # C'est ici qu'on peut vérifier si le lobbying concerne le climat
        # On fait cette vérification au moyen d'une condition
        if "limat" in sujet["objet"] or "limat" in sujet["objet_autre"]:

            # Si la condition est vraie (et que le lobbying concerne le climat), eh bien on ramasse l'info dont on a besoin:
            nomFr = element[0]["fr_client_org_corp_nm"] # le nom de l'entreprise ou du groupe en français se trouve dans l'élément 0, sous la clé "fr_client_org_corp_nm"
            nomAn = element[0]["en_client_org_corp_nm"] # le nom de l'entreprise ou du groupe en anglais se trouve dans l'élément 0, sous la clé "en_client_org_corp_nm"
            codeClient = element[0]["client_org_corp_num"] # etc
            date = element[0]["date_comm"]

            objet = sujet["objet"]
            objetAutre = sujet["objet_autre"]

            # C'était optionnel, mais vous pouviez aussi recueillir le nom du ministère ou de l'agence qui était la cible du lobbying en allant la chercher dans le troisième élément (l'élément 2)
            # Et comme ce 3e élément est lui aussi une liste, on peut ne prendre que le premier élément, parce qu'on sait que dans chacun de ces sous-éléments, le nom de l'institution sera le même
            # Et on peut donc aller chercher le nom du ministère ou de l'agence sous la clé "institution"
            institution = element[2][0]["institution"]

            # On met toutes ces infos dans une liste
            infos = [
                codeClient,
                nomFr,
                nomAn,
                date,
                objet,
                objetAutre,
                institution
            ]

            print(infos) # affichage dans le terminal aux fins de vérification
            print("~"*12) # affichage d'une petite séparation décorative faite de 12 tildes

            # Écriture de notre liste infos dans une ligne de notre fichier CSV
            magda = open(lobbyClimatique, "a")
            fusaro = csv.writer(magda)
            fusaro.writerow(infos)

# Vous devriez avoir un fichier CSV contenant 2564 lignes
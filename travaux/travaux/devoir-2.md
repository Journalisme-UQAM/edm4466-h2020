# Devoir 2

![](../../.gitbook/assets/nbelanger.jpg)

Je vous présente Nancy Bélanger,  [Commissaire au lobbying du Canada](https://lobbycanada.gc.ca/eic/site/012.nsf/fra/h_00000.html). Elle est notamment responsable du [Registre fédéral des lobbyistes](https://lobbycanada.gc.ca/app/secure/ocl/lrs/do/advSrch?lang=fra).

Le **lobbying**, [nous dit l'Encyclopédie canadienne](https://thecanadianencyclopedia.ca/fr/article/lobbying), consiste à rencontrer des élu\(e\)s ou des fonctionnaires dans le but d’influencer les lois, les politiques ou les décisions des gouvernements.

C'est une activité à laquelle, traditionnellement, des entreprises et des groupes d'intérêt se livraient dans le plus grand secret. L'influence politique ne se faisait pas dans la transparence... Jusqu'à l'adoption, en 1989, d'une loi sur l'enregistrement des lobbyistes, rebaptisée Loi sur le lobbying en 2006.

### Le Registre

Depuis 2008, le Registre des lobbyistes enregistre **trois dimensions du lobbying** :

* Qui est à la **source** du lobbying \(quelles entreprises ou organismes\)?
* Qui est la **cible** du lobbying \(quels ministères ou élu\(e\) cherche-t-on à influencer\)?
* Quels **sujets** sont abordés?

Inutile de vous dire combien ce Registre peut être d'intérêt public. Il vous permet de connaître qui cherche à influencer qui et pourquoi.

J'ai créé pour vous un API de toutes les inscriptions au registre entre le 1er janvier 2015 et le 31 octobre 2018 \(bon, en fait, ce n'est pas un véritable API, mais plutôt ce qu'on pourrait appeler un «pseudo-API» qui convient aux besoins de ce cours\).

### Mon API maison

Il se trouve à cet URL:

> [http://jhroy.ca/uqam/lobby.json](http://jhroy.ca/uqam/lobby.json)

C'est un immense fichier JSON structuré ainsi:

* Une première clé appelée «registre» dont la valeur est une liste de près de 72000 éléments.
* Chacun de ces éléments est une inscription au registre, elle-même sous forme d'une autre liste comptant trois éléments \(cliquez sur les onglets ci-dessous pour en voir les détails\):

{% tabs %}
{% tab title="0" %}
Un **dictionnaire** \(`dict`\) décrivant quel organisme ou quelle entreprise a fait du lobbying.
{% endtab %}

{% tab title="1" %}
Une **liste** \(`list`\) de tous les sujets abordés dans cette inscription \(souvent la liste ne compte qu'un élément, parce qu'un seul sujet a été abordé, mais parfois, il y a plusieurs sujets\). Chacun des éléments de la liste est un dictionnaire.
{% endtab %}

{% tab title="2" %}
Une **liste** \(`list`\) de tous les fonctionnaires ou élu\(e\)s rencontré\(e\)s à cette occasion \(souvent la liste ne compte qu'un seul élément, mais parfois plusieurs responsables ont été rencontrés\). Ici aussi, chacun des éléments de la liste est un dictionnaire.
{% endtab %}
{% endtabs %}

### Structure

Voici un exemple de ce fichier avec deux inscriptions. Je les décortique ci-dessous:

```javascript
{"registre":
	[

		[
			{"comlog_id": "344458", "client_org_corp_num": "13608", "en_client_org_corp_nm": "Canadian Steel Producers Association", "fr_client_org_corp_nm": "L'Association canadienne des producteurs d'acier", "declarant_num": "781164", "declarant_nom": "Watkins", "declarant_prenom": "Ron", "date_comm": "2015-01-20", "type_enr": "3", "date_soumission": "2015-01-26", "date_publication": "2015-02-16", "comlog_id_precedent": "null"},
			[
				{"comlog_id": "344458", "objet": "Government Procurement", "objet_autre": "Government Procurement"},
				{"comlog_id": "344458", "objet": "Infrastructure", "objet_autre": "Infrastructure"},
				{"comlog_id": "344458", "objet": "International Trade", "objet_autre": "International Trade"}
			],
			[
				{"comlog_id": "344458", "tcpd_nom": "Bottriell", "tcpd_prenom": "Kyla", "tcpd_titre": "Manager of Policy", "direction_service": "Minister's Office", "institution_autre": "null", "institution": "Foreign Affairs, Trade and Development Canada"}
			]
		],
		
		[
			{"comlog_id": "398177", "client_org_corp_num": "348827", "en_client_org_corp_nm": "Netflix", "fr_client_org_corp_nm": "Netflix", "declarant_num": "908202", "declarant_nom": "Roy", "declarant_prenom": "Louis-Charles", "date_comm": "2017-04-05", "type_enr": "1", "date_soumission": "2017-04-10", "date_publication": "2017-05-15", "comlog_id_precedent": "null"},
			[
				{"comlog_id": "398177", "objet": "Consumer Issues", "objet_autre": "Consumer Issues"},
				{"comlog_id": "398177", "objet": "Arts and Culture", "objet_autre": "Arts and Culture"}
			],
			[
				{"comlog_id": "398177", "tcpd_nom": "Séguin", "tcpd_prenom": "Caroline", "tcpd_titre": "Directrice des politiques", "direction_service": "null", "institution_autre": "null", "institution": "Canadian Heritage (PCH)"},
				{"comlog_id": "398177", "tcpd_nom": "Wilhelm", "tcpd_prenom": "Kelly", "tcpd_titre": "Conseillère, politique", "direction_service": "null", "institution_autre": "null", "institution": "Canadian Heritage (PCH)"},
				{"comlog_id": "398177", "tcpd_nom": "Joly", "tcpd_prenom": "Mélanie", "tcpd_titre": "Ministre du Patrimoine canadien", "direction_service": "null", "institution_autre": "null", "institution": "Canadian Heritage (PCH)"},
				{"comlog_id": "398177", "tcpd_nom": "Church", "tcpd_prenom": "Leslie", "tcpd_titre": "Directrice de cabinet", "direction_service": "null", "institution_autre": "null", "institution": "Canadian Heritage (PCH)"},
				{"comlog_id": "398177", "tcpd_nom": "Martinez", "tcpd_prenom": "Soraya", "tcpd_titre": "Senior Advisor", "direction_service": "null", "institution_autre": "null", "institution": "Canadian Heritage (PCH)"}
			]
		], 

		...
		
	]
}
```

La première inscription \(dont le `comlog_id` est 344458\) montre que l'Association canadienne des producteurs d'acier a rencontré, le 20 janvier 2015, **une** seule personne, la responsable des politiques du bureau du ministre des Affaires étrangères, du Commerce et du Développement, pour discuter de **trois** sujets \(les approvisionnements \[les contrats publics\], les infrastructures et le commerce international\). Je sais, moi aussi je bâille! 😴

La seconde inscription \(`comlog_id` 398177\) est plus intéressante:

* L'entreprise qui a fait du lobbying est Netflix.
* Il a été question de **deux** sujets: les consommateurs, d'une part, et les arts et la culture d'autre part.
* Et, grosse réunion, Netflix cherchait à influencer **cinq** fonctionnaires ou élu\(e\)s de Patrimoine canadien, dont la ministre de l'époque, Mélanie Joly.

### Infos importantes

Pour faire ce devoir, vous aurez à repérer, dans cet immense fichier, les clés suivantes:

* Dans l'élément `0` de la liste contenant l'enregistrement:
  * `fr_client_org_corp_nm` -&gt; c'est le nom de l'organisme ou de l'entreprise lobbyiste en français
  * `en_client_org_corp_nm` -&gt; lobbyiste en anglais
  * `client_org_corp_num` -&gt; code unique de l'entreprise ou de l'organisme cherchant à influencer le gouvernement
  * `date_comm` -&gt; date à laquelle a eu lieu la communication de lobbying
* Dans l'élément `1` de la liste:
  * `objet` -&gt; le sujet principal à propos duquel on cherche à influencer le gouvernement
  * `objet_autre` -&gt; sujet secondaire \(souvent on dédouble le sujet principal\)
* Dans l'élément `2` \(mais c'est _optionnel_\):
  * `institution` -&gt; c'est le nom du ministère ou de l'agence qui a fait l'objet de la tentative d'influence.

### Script attendu

Pardonnez ce long préambule, mais il fallait mettre la table pour votre mission. Celle-ci consiste à rédiger un script python qui va **produire un fichier csv** \(baptisez-le comme vous voulez\) contenant les colonnes suivantes:

* code de l'organisation lobbyiste
* nom de l'organisation lobbyiste en français
* nom de l'organisation lobbyiste en anglais
* date à laquelle la communication a eu lieu
* sujet principal \(n'en indiquez qu'un seul \[voir paragraphe suivant\]\)
* sujet autre \(n'en indiquez qu'un seul \[voir paragraphe suivant\]\)
* l'institution visée \(_optionnel_\)

Mais attention, le fichier ne devra contenir ces informations uniquement lorsqu'il a été question de **climat**. Ne considérez donc que les inscriptions dont le sujet principal ou le sujet autre contiennent la chaîne de caractères «_**limat**_», afin de trouver «climat», «Climat», «climatique», etc. Et à ce moment-là, n'inscrivez dans votre fichier qu'un seul «sujet principal» \(celui qui contient l'expression «limat»\) et qu'un seul «autre sujet» \(celui qui, ici aussi, contient l'expression «limat»\).

Plus de détails sur les paramètres de remise [dans la section travaux.](./#devoir-2) 


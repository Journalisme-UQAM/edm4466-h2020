# Devoir 1

![](../../.gitbook/assets/logomtlcampus%20%281%29.png)

Vous avez remarqué que lorsque vous entrez l’url suivant:

[https://montrealcampus.ca?p=30145](https://montrealcampus.ca?p=30145)

Vous êtes redirigé vers un article du plus meilleur journal étudiant au Québec. Le numéro **30145**, ici, est un numéro d’identification unique.

Vous êtes curieux de tester tous les numéros d’identification entre 20000 et 30150.

Écrivez un script python qui vous permettrait de générer rapidement les 10 151 URLs nécessaires, de les mettre dans une variable de type liste et d’afficher cette liste. Demandez aussi à votre script d’afficher la taille de cette liste pour vérifier que vous en avez bien 10 151.

Les détails pour savoir comment remettre votre devoir se trouvent [dans la page travaux](./#devoir-1).

Cela dit, pour faire ce que je vous demande, vous devrez utiliser une méthode que je n'ai pas eu le temps d'aborder avec vous en classe le 23 janvier. Il s'agit de la méthode `.append()`.

Elle permet d'ajouter des éléments à une liste. Admettons que vous ayez une liste de huit entreprises:

`gafa = ["Google","Apple","Facebook","Amazon","Netflix","Airbnb","Tesla","Uber"]`

Si vous souhaitez ajouter une entreprise à cette liste, vous pouvez le faire avec `.append()` :

`gafa.append("Microsoft")`

Si vous faites `print(gafa)`, votre liste compte désormais neuf éléments:

`print(gafa)`

`['Google', 'Apple', 'Facebook', 'Amazon', 'Netflix', 'Airbnb', 'Tesla', 'Uber', 'Microsoft']`


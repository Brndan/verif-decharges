# verif-decharges
Un script pour déterminer les limites de temps de décharge syndicale à la fédération SUD éducation

## Prérequis

Une installation de python 3.x

## Usage :

`verif-decharges.py [-h] [-y YEAR] [-v] fichier`

`fichier` est un fichier CSV à parser. Le fichier doit être formaté comme
avec une première ligne comme suit : Civilité Nom d'usage Prénom 2019-2018
2018-2017…

`-h, --help` : message d'aide

`-y YEAR, --year YEAR` : année de départ pour la vérification. Par défaut,
la première année rencontrée dans le fichier CSV.

`-v, --verbose` : affiche sur la sortie standard tous les noms suivis du
nombre d'ETP consommés et le nombre d'années de décharges.

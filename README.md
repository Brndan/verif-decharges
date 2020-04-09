# verif-decharges
Un script pour déterminer les limites de temps de décharge syndicale à la fédération SUD éducation.

## Prérequis

Une installation de python 3.x, et Gooey ainsi que wxgtk

Sous Ubuntu :
`sudo apt-get build-dep libwxgtk3.0-0v5`

`pip3 install Gooey`

## Créer un exécutable

`pip3 install PyInstaller`

`pyinstaller -F verif-decharge.spec`

## Installer le script

Pas d'installation requise.

Le script python se nomme `verif-decharge.py`. Il peut être lancé
directement par la commande `python3 verif-decharge.py`.

Dans le répertoire `bin` se trouvent des exécutables qui peuvent être
utilisés directement, pour Linux et Windows.


## Données en entrée

*Travaillez sur une copie de sauvegarde du tableau de décharges avant de commencer.*

Il faut fournir un fichier CSV à parser comprenant des nombres au format US, c'est-à-dire que le séparateur décimal doit être un point et non une virgule. Dans Libreoffice, il faut se rendre dans le menu Outils - Options.

Dans Libreoffice, exporter un tableur au format CSV et choisir
- `"` comme séparateur des chaînes de caractère ;
- `,` comme séparateur de champ.

Veiller à ce que le fichier ressemble à ceci :

| Civilité | Prénom | Nom d'usage | 2019-2020 | 2018-2019 |
| -------- | ------ | ----------- | --------- | --------- |
| M.       | Denis  | Orcel       | 0.5       | 0.5       |

## Données en sortie

Le programme produit un fichier `resultat.csv` dans le dossier où il est stocké (pas dans le dossier où le csv en entrée est stocké). Ce fichier fait la liste des camarades qui :

- ont atteint ou dépassé 3 ETP de décharge ;
- ont atteint 8 ans de décharge ;
- s’approchent de ces valeurs.




## Usage en ligne de commande :

`verif-decharges[.py|exe] [-h] [-y YEAR] [-v] fichier`

`fichier` est un fichier CSV à parser. Le fichier doit être formaté comme
avec une première ligne comme suit : Civilité Prénom Nom d'usage 2019-2018
2018-2017…

`-h, --help` : message d'aide

`-y YEAR, --year YEAR` : année de départ pour la vérification. Par défaut,
la première année rencontrée dans le fichier CSV.

`-v, --verbose` : affiche sur la sortie standard tous les noms suivis du
nombre d'ETP consommés et le nombre d'années de décharges.

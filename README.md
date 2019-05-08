# verif-decharges
Un script pour déterminer les limites de temps de décharge syndicale à la fédération SUD éducation

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

## Usage en ligne de commande :

`verif-decharges[.py|exe] [-h] [-y YEAR] [-v] fichier`

`fichier` est un fichier CSV à parser. Le fichier doit être formaté comme
avec une première ligne comme suit : Civilité Nom d'usage Prénom 2019-2018
2018-2017…

`-h, --help` : message d'aide

`-y YEAR, --year YEAR` : année de départ pour la vérification. Par défaut,
la première année rencontrée dans le fichier CSV.

`-v, --verbose` : affiche sur la sortie standard tous les noms suivis du
nombre d'ETP consommés et le nombre d'années de décharges.

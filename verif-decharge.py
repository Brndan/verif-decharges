#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gooey import Gooey,GooeyParser
import csv
import sys
#import argparse
import re



def year_constraint(infos_pers, years):
    """
    Retourne le nombre d'années effectué dans la période years
    Stoppe le parcour de years si il y a deux années consécutives sans décharge
    """
    count = 0
    # on parcourt la liste sur 2 années pour pouvoir stopper si
    # il y a 2 années nulles
    for y, next_y in zip(years, years[1:] + ['stop']):
        try:
            if infos_pers[y] != '0' and infos_pers[y] != '':
                count += 1
        except KeyError:
            # si la date n'est pas dans les infos de la personne
            # on considère qu'il n'y a plus de date après
            break
        try:
            if (infos_pers[y] == '0' or infos_pers[y] == "")\
                and (infos_pers[next_y] == '0' or infos_pers[next_y] == ""):
                break
        except KeyError:
                # Si le keyerror apparait, la date i+1 n'existe pas
                # pas besoin de s'en préoccuper
                pass
        if count == 8:
            break
    return count

def etp_constraint(infos_pers, years):
    """
    Retourne le nombre d'ETP effectués avec remise à zéro si
    il y a deux années consécutives sans décharge
    """
    etp = 0
    for y, next_y in zip(years, years[1:] + ['stop']):
        try:
            etp += float(infos_pers[y].replace(",", "."))
        except ValueError:
            # si on arrive pas à convertir le nombre, on considère que c'est 0
            pass
        except KeyError:
            # si la date n'est pas dans les infos de la personne
            # on considère qu'il n'y a plus de date après
            break
        try:
            if (infos_pers[y] == '0' or infos_pers[y] == "")\
                and (infos_pers[next_y] == '0' or infos_pers[next_y] == ""):
                break
        except KeyError:
            # Si le keyerror apparait, la date i+1 n'existe pas
            # pas besoin de s'en préoccuper
            pass
        if  etp >= 3:
            break
    return etp

def write_csv_file(rows):
    with open("resultat.csv", "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for r in rows:
            row = [r['Civilité'], r["Nom d'usage"], r['Prénom']]
            if r['year'] == 7:
                row += ['Attention bientôt 8 ans']
            elif r['year'] == 8:
                row += ["Limite des 8 ans atteinte"]
            else:
                row += ['RAS']
            if r['etp'] >= 3:
                row += ['Limite des 3 ETP atteinte']
            elif r['etp'] > 2.5:
                row += ['Bientôt 3 ETP atteints']
            else:
                row += ['RAS']
            writer.writerow(row)
    return

@Gooey(language='french')
def main():
    # gestion des arguments de la ligne de commande
# Version argparse pour ligne de commande à décommenter
#    parser = argparse.ArgumentParser(description="Vérification des décharges")

# Version Gooey pour GUI 
    parser = GooeyParser(description="Vérification des décharges")
    parser.add_argument("file", help="Fichier CSV\n\
                        Le fichier CSV doit contenir sur la première ligne (a minima):\n \
                        Civilité-Nom d'usage-Prénom suivi des colonnes de dates: 2018-2019 2017-2018 ...", widget='FileChooser')
    parser.add_argument("-y", "--year", help="Année de départ pour la vérification.\n \
Par défaut la première année rencontrée dans le fichier CSV.") 
#    parser.add_argument("-v", "--verbose", action="store_true", help="Affiche sur la ligne de commande tous les noms avec le nombre d'ETP et le nombre d'années")
    parser.add_argument("-v", "--verbose", action="store_true", help="Affiche sur la ligne de commande tous les noms avec le nombre d'ETP et le nombre d'années")
    args =parser.parse_args()

    with open(args.file, encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        # init de l'année de départ
        if args.year is None:
            for f in reader.fieldnames:
                if re.match("\d{4}-\d{4}", f):
                    date = f
                    break
        else:
            date = args.year
        if date not in reader.fieldnames:
            sys.exit("Impossible de trouver une année")

        # on se cale sur 16 années glissantes
        # à cause de l'année seule qui est suspensive
        # date contient un truc du style 2018-2019, on ne recupère que 2018 pour 
        # pouvoir facilement trouver les 16 autres années
        date = int(date.split("-")[0])
        # on prepare les 16 années

        years_list = ["%s-%s" % (i, i+1) for i in range(date, date - 16, -1)]
        resultat = list()
        for row in reader:
            row['year'] = year_constraint(row, years_list)
            row['etp'] = etp_constraint(row, years_list)
            # lorsque -v est donné on affiche sur la console les résultats
            if args.verbose:
                print(row["Nom d'usage"], row["Prénom"], row['etp'], row['year'])

            # On ne retient que les noms >=7 ou etp>2.5
            if row['year'] >= 7 or row['etp'] > 2.5:
                resultat.append(row)

    write_csv_file(resultat)
    return

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fonctions de base d'un jeu de Scrabble."""
# Imports ---------------------------------------------------------------------
import string
from random import *

# Variables globales ----------------------------------------------------------


# Fonctions -------------------------------------------------------------------
def initialiser_dictionnaire(nom_fichier):
    """Renvoie un dictionnaire d'ensembles contenant tous les mots d'un fichier
    de référence sans accents et en minuscules, où l'ensemble correspondant à
    la clé k contient tous les mots de longueur k."""
    dico_mots = dict()
    with open(nom_fichier,"r") as fichier:
        for mots in fichier.readlines():
            mots = mots.strip()
            longueur = len(mots)
            if longueur in dico_mots.keys():
                dico_mots[longueur].add(mots)
            else:
                dico_mots[longueur] = set()
                dico_mots[longueur].add(mots)
    return dico_mots
                
            
            



def initialiser_sac():
    """Renvoie la liste des lettres du Scrabble."""
    occu = [2,9,2,2,3,15,2,2,2,8,1,1,5,3,6,6,2,1,6,6,6,6,2,1,1,1,1]
    ltrs = '*abcdefghijklmnopqrstuvwxyz'
    lst = []
    for i in range(len(occu)):
        for _ in range(occu[i]):
            lst.append(ltrs[i])

    shuffle(lst)
    return lst



def piocher(sac, n):
    """Extrait n lettres au hasard du sac, et renvoie la liste qui les
    contient."""
    lst_mots = list()
    for _ in range(n):
        i_aleat = randint(0,len(sac)-1)

        #Deux lignes suivantes à commenter si on veut pouvoir piocher des lettres au hasard
        while  sac[i_aleat] == "*":
            i_aleat = randint(0,len(sac)-1)
        
        lst_mots.append(sac[i_aleat])

        #La lettre est prise donc on l'enlève du sac initial
        sac.pop(i_aleat)



    return lst_mots



'''Empecher les jockers de se faire tirer'''
def generer_points():
    points = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, 
         "g": 2, "h": 4, "i": 1, "j": 8, "k": 10, "l": 1, 
         "m": 2, "n": 1, "o": 1, "p": 3, "q": 8, "r": 1, 
         "s": 1, "t": 1, "u": 1, "v": 4, "w": 10, "x":10 , 
         "y": 10, "z": 10, "*":0}
         
    return points

def score(mot):
    """Renvoie la somme des points donnés par le mot.

    >>> score("ornes")
    5
    >>> score("cognat")
    9
    >>> score("contage")  # scrabble: on rajoute 50 points
    60
    """
    pts = generer_points()
    compteur = 0
    for lettres in mot:
        compteur += pts[lettres]
    if len(mot) >= 7:
        return compteur+50
    return compteur



def trouver_mot_de_longueur_fixe(lettres, longueur, dictionnaire):
    """Renvoie un mot de la longueur demandée formé des lettres passées en
    paramètre si le dictionnaire contient un tel mot, ou None dans le cas
    contraire."""
    return_mot = ''
    Joker = False


    ensemble = dictionnaire[longueur]

    for mots in ensemble:
        if '*' in lettres:
            Joker = True
        if return_mot != '':
            return return_mot
        for lttrs in mots:
            if lttrs in lettres and mots.count(lttrs) <= lettres.count(lttrs):
                return_mot = mots
                continue
            elif Joker:
                return_mot = mots
                Joker = False
                continue   
            else:
                return_mot = ''
                break
    return

def trouver_mot_de_longueur_maximale(lettres, dictionnaire):
    """Renvoie le plus long mot du dictionnaire que l'on peut construire sur
    l'ensemble de lettres donné, en respectant les occurrences."""
    liste_mot = []
    for i in range(1,len(lettres)+1):
        mot = trouver_mot_de_longueur_fixe(lettres,i,dictionnaire)
        if mot != None:
            liste_mot.append(mot)
    return max(liste_mot,key=len)


def trouver_mot_de_longueur_fixe_et_de_score_maximal(lettres, longueur, dictionnaire):
    """Renvoie le mot de plus haut score que l'on peut obtenir parmi tous les
    mots de la longueur demandée avec les lettres données, ou None si aucun mot
    de cette longueur n'existe."""
    liste_mots = []
    return_mot = ''
    ensemble = dictionnaire[longueur]
    for mots in ensemble:
        copy = lettres.copy()
        if return_mot != '':
            liste_mots.append(return_mot)
        return_mot = ''
        for lttrs in mots:
            if lttrs in lettres and mots.count(lttrs) <= lettres.count(lttrs):
                copy.remove(lttrs)
                return_mot = mots
                continue
            else:
                return_mot = ''
                break
    if len(liste_mots) != 0:
        return max(liste_mots,key=score)
    return 


def trouver_mot_de_score_maximal(lettres, dictionnaire):
    """Renvoie le mot du dictionnaire rapportant le plus de points, parmi tous
    ceux que l'on peut construire sur l'ensemble de lettres donné, en
    respectant les occurrences."""
    liste_mot = []
    for i in range(1,len(lettres)+1):
        mot = trouver_mot_de_longueur_fixe_et_de_score_maximal(lettres,i,dictionnaire)
        if mot != None:
            liste_mot.append(mot)
    return max(liste_mot,key=len)


def trouver_mot_de_longueur_maximale_avec_un_joker(lettres, dictionnaire):
    """Renvoie le plus long mot du dictionnaire que l'on peut construire sur
    l'ensemble de lettres donné, en respectant les occurrences, dans le cas où
    l'une des lettres est un joker."""
    return trouver_mot_de_longueur_maximale(lettres,dictionnaire)


if __name__ == "__main__":
    # à décommenter pour vérifier vos fonctions:
    import doctest
    doctest.testmod()


    dico_fr = initialiser_dictionnaire("./liste-mots-fr-utf8-sans-caracteres-speciaux.txt")
    sac = initialiser_sac()
    nombres_lettres = 7
    pioche = piocher(sac,nombres_lettres)
    '''
    dico=initialiser_dictionnaire("liste-mots-fr-utf8-sans-caracteres-speciaux.txt")
    for cle,ens in dico.items():
        print(cle,len(ens))

    print(dico[24])

    pioche = ["a","r","u","d","m","e","o"]
    '''

    # Ligne a mettre en commentaire pour tester avec d'autres lettres aléatoires
    pioche = ["a","r","u","d","m","e","o"]
    



    ''' ==================================== MOTS DE LONGUEUR FIXE ===================================='''
    print("\n=========== Recherche de mots de longueur fixe ===========")
    print(f'Je pioche {nombres_lettres} et j\'ai: {pioche} \n')
    for i in range(1,nombres_lettres+1):
        mot = trouver_mot_de_longueur_fixe(pioche,i,dico_fr)
        if mot == None:
            erreur = "Pas de mot trouvé..."
            print(f"Recherche d'un mot de longueur {i}... {erreur}: ")
            continue
        points = score(mot)
        print(f"Recherche d'un mot de longueur {i}... Trouvé: ",mot," "*(nombres_lettres-len(mot)),f" , qui rapporte {points} ", "points" if points > 1 else "point")



    ''' ==================================== MOTS DE LONGUEUR MAXIMALE===================================='''
    print("\n=========== Recherche de mots de longueur maximale ===========")
    print(f'Je pioche {nombres_lettres} et j\'ai: {pioche}\n')
    mot = trouver_mot_de_longueur_maximale(pioche,dico_fr)
    if mot == None:
        erreur = "Pas de mot trouvé..."
        print(f"Aucun mot n'a été trouvé pour la chaine {pioche}")
    points = score(mot)
    print(f"Voici le mot de longueur maximale pour la réglette: {pioche} : {mot} qui rapporte {points} ", "points" if points > 1 else "point")


    ''' ==================================== MOTS DE LONGUEUR FIXE ET SCORE MAXIMAL ===================================='''
    print("\n=========== Recherche de mots de longueur fixe et de score maximal ===========")
    print(f'Je pioche {nombres_lettres} et j\'ai: {pioche} \n')
    for i in range(1,nombres_lettres+1):
        mot = trouver_mot_de_longueur_fixe_et_de_score_maximal(pioche,i,dico_fr)
        if mot == None:
            erreur = "Pas de mot trouvé..."
            print(f"Recherche d'un mot de longueur {i}... {erreur}: ")
            continue
        points = score(mot)
        print(f"Recherche d'un mot de longueur {i}... Trouvé: ",mot," "*(nombres_lettres-len(mot)),f" , qui rapporte {points} ", "points" if points > 1 else "point")



    ''' ==================================== MOTS DE SCORE MAXIMAL ===================================='''
    print("\n=========== Recherche de mots de score maximal ===========")
    print(f'Je pioche {nombres_lettres} et j\'ai: {pioche}\n')
    mot = trouver_mot_de_score_maximal(pioche,dico_fr)
    if mot == None:
        erreur = "Pas de mot trouvé..."
        print(f"Aucun mot n'a été trouvé pour la chaine {pioche}")
    points = score(mot)
    print(f"Voici le mot de longueur maximale pour la réglette: {pioche} : {mot} qui rapporte {points} ", "points" if points > 1 else "point")



    ''' ==================================== MOTS DE LONGUEUR MAXIMALE AVEC JOKER===================================='''
    pioche = ['*', 'r', 'q', 'a', 'n', 's', 't']
    print("\n=========== Recherche de mots de longueur maximale avec un joker ===========")
    print(f'Je pioche {nombres_lettres} et j\'ai: {pioche}\n')
    mot = trouver_mot_de_longueur_maximale(pioche,dico_fr)
    if mot == None:
        erreur = "Pas de mot trouvé..."
        print(f"Aucun mot n'a été trouvé pour la chaine {pioche}")
    points = score(mot)
    print(f"Voici le mot de longueur maximale pour la réglette: {pioche} : {mot} qui rapporte {points} ", "points" if points > 1 else "point")
# Générateur de mots au SCRABBLE
Programme python permettant d'extraire les mots d'un fichier et de les trier selon des fonctions afin de jouer au scrabble.

Comment ça marche ?
1) Apporter ou utiliser son fichier texte contenant les mots du dictionnaire de la langue souhaitée (en UTF-8 )
2) Lancer le fichier scrabble_init.py en utilisant la commande python3 scrabble_init.py depuis un terminal ouvert dans le répertoire du fichier.
3) Le programme permet de choisir ses lettres et les utilise en afin de générer des mots selon les fonctions.

Les fonctions :
1) Mot de longueur fixe :
Retourne le premier mot trouvé de la longueur indiquée en utilisant les lettres disponibles.
2) Mot de longueur maximale:
Retourne le plus grand mot possible d'obtenir.
3) Mot de longueur fixe et de score maximale : 
Retourne le premier mot trouvé de la longueur indiquée permettant d'obtenir le meilleur score
4) Mot de score maximal:
Retourne le mot permettant d'obtenir le meilleur score avec les lettres indiquées
5) Mot de longueur maximale avec joker:
Retourne le mot le plus long tout en utilisant un joker s'il est dans les lettres indiquées ( joker représente par * (étoile) )


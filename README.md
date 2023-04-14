# Algo Puissance 4

## Comment démarrer

### Le Serveur Web

Pour lancer l’application, il suffit de faire

```bash
py ./src/app.py
```

#### Changer le port

Le fichier [`app.py`](/src/app.py) est le point d’entrée de l’application. Il contient le serveur web. Le serveur web se
lance par défaut sur le port **8000**, si on veut le lancer sur un port différent, on peut faire ceci pour le lancer sur
le port **3773** par exemple :

```bash
py ./src/app.py -p 3773
```

#### Changer le temps de réflexion

Il y a un autre argument disponible qui permet de changer le temps maximum de réflexion de l’algorithme. Par défaut, il
est à **une (1)** seconde. On peut le changer en faisant :

```bash
py ./src/app.py -t 0.25
```

**Attention** : le temps de réflexion doit être un nombre décimal positif.
Ce temps n’est pas vraiment representatif de la vitesse du serveur, donc si on met 0.25, il ne faut pas s’attendre à ce que le serveur réponde en 0.25 seconde, mais l’algo va prendre 0.25 seconde pour réfléchir et s’arrêter après a l’itération suivante par rapport à ce temps.


### Fichiers Utilisés

Il y a deux fichiers qui contiennent les vérifications du plateau envoyé :

- [`format.py`](/src/format.py) : contient les fonctions de vérifications du format du plateau (si le plateau est bien
  un tableau de 6 lignes et 7 colonnes, si les jetons sont bien soit h, m ou 0, etc.)
- [`verification.py`](/src/verification.py) : contient les fonctions de vérifications du jeu (s’il y a un puissance 4,
  si le plateau est plein)

Enfin, il y a le fichier qui gère l’algorithme pour trouver le meilleur coup :

- [`algo.py`](/src/algo.py) : contient l’algorithme minimax et la fonction d’évaluation du plateau

## Description

L’algorithme Minimax est une méthode de recherche d’arbres utilisée dans les jeux à deux joueurs à somme nulle et à
information parfaite, comme les échecs, le morpion et le puissance 4. L’algorithme est basé sur le principe que les deux
joueurs jouent de manière optimale pour maximiser leur propre score tout en minimisant le score de l’adversaire.

### Principe de l’algorithme minimax

1. L’algorithme vérifie si la profondeur de recherche est égale à zéro ou s'il n’y a plus de coups possibles. Si l’une
   de ces conditions est remplie, l’algorithme évalue le plateau de jeu en fonction du joueur maximisant et retourne
   cette valeur d’évaluation ainsi que None pour le meilleur coup (puisqu’il n’y a pas de meilleur coup dans ce cas).
2. Si le joueur actuel est le joueur maximisant, l’algorithme cherche le coup qui maximise la valeur d’évaluation du
   plateau de jeu. Pour chaque coup possible, il simule le coup, appelle récursivement la fonction Minimax sur le
   nouveau plateau de jeu avec une profondeur de recherche réduite de 1 et change le joueur actuel en joueur minimisant.
   L’algorithme récupère la valeur d'évaluation de chaque coup simulé et sélectionne le coup qui maximise cette valeur.
3. Si le joueur actuel est le joueur minimisant, l’algorithme cherche le coup qui minimise la valeur d'évaluation du
   plateau de jeu. Pour chaque coup possible, il simule le coup, appelle récursivement la fonction Minimax sur le
   nouveau plateau de jeu avec une profondeur de recherche réduite de 1 et change le joueur actuel en joueur maximisant.
   L’algorithme récupère la valeur d’évaluation de chaque coup simulé et sélectionne le coup qui minimise cette valeur.
4. L’algorithme utilise également l’élagage alpha-bêta pour réduire le nombre de branches de l’arbre de recherche
   explorées. L’élagage alpha-bêta permet de ne pas explorer certaines branches inutiles de l’arbre de recherche lorsque
   nous savons déjà qu’elles ne peuvent pas produire de meilleurs résultats que les branches déjà explorées.

En résumé, l’algorithme Minimax cherche le meilleur coup possible pour le joueur maximisant en explorant les coups
possibles jusqu’à une certaine profondeur et en évaluant les plateaux de jeu résultants. Il prend en compte les coups
optimaux de l’adversaire (le joueur minimisant) et utilise l’élagage alpha-bêta pour améliorer l’efficacité de la
recherche.

### Fonctionnement du calcul des scores

La fonction `eval_board` est utilisée pour évaluer le plateau de jeu actuel en attribuant un score basé sur la position
des jetons de chaque joueur. Le score final est la somme de toutes les évaluations individuelles pour chaque
configuration de jetons.

1. Pour chaque position sur le plateau, on attribue des points en fonction de la position heuristique. Les positions
   heuristiques sont définies par la matrice `position_heuristics` qui attribue des points pour chaque case du plateau
   en fonction de son importance stratégique. Les jetons "m" (machine) ajoutent des points au score, tandis que les
   jetons "h" (humain) en retirent.
2. Ensuite, on évalue les points pour chaque rangée, colonne, diagonale et anti-diagonale de quatre cases consécutives.
   Pour chaque configuration de jetons, on appelle la fonction `score_heuristique` avec le nombre de jetons consécutifs
   pour chaque joueur et le nombre total de jetons pour chaque joueur.
3. La fonction `score_heuristique` attribue des points en fonction du nombre de jetons consécutifs pour chaque joueur.
   Plus il y a de jetons consécutifs, plus les points attribués sont élevés. Les points sont également ajustés en
   fonction du nombre total de jetons pour chaque joueur. Par exemple, si un joueur a trois jetons consécutifs sans
   jetons de l’adversaire, il obtient plus de points que s’il y avait des jetons adverses dans la configuration.
4. Si le score atteint les valeurs -1000 ou 1000, cela signifie que l’un des joueurs a une position gagnante et la
   fonction `eval_board` retourne immédiatement le score.

La fonction `eval_board` estime ainsi la qualité du plateau de jeu pour le joueur maximisant (la machine) en attribuant
des points en fonction de la position des jetons et des configurations de jetons consécutifs. Un score plus élevé
indique une meilleure position pour la machine, tandis qu’un score plus faible indique une meilleure position pour
l’humain.
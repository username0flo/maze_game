# Presentation

## resumé
- jeu de labyrinthe (deébut -> arrivée)
- commandes / deplacements
- bombes
- on peut recommencer



main:

jeu

init:

constantes
pres vite fait les variables (~fonction)

maze:

algo 1:

- remplissage d'une grille avec que des murs (1) sans case vide (0)
- enlever la case du joueur en (0, 0) -> la mettre en case vide
- mettre dans une liste vide de murs les murs voisins (en croix)
- choisir un mur aléatoire de cette liste de murs
- si ce mur posséde strictement plus qu'une case vide dans ses cases voisines -> supprimer ce mur et choisir un autre mur de la liste 

algo 2:

- meme chose que pour algo 1: dans init grille
- utilise une pile: retient les cases vides (dans l'ordre)
- vide une case au hazard (voisin)
- ajoute la case a la pile
- si aucune case creusable: on enleve le dernier pile

gestion evenement:
tuple: 
- fleche
- clic
- touche




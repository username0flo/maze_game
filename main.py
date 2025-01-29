from graphics import *
import random as rd
from time import sleep
# definition des fonction du jeu:

def init_grille(joueur):
    return algo_prim(joueur)

def algo_prim(joueur):
    # initialise la grille: (0 = case_vide, 1 = mur)
    grille = []
    for i in range(NB_CASES):
        grille.append([1]*NB_CASES)
    murs = []
    i,j =joueur
    grille[i][j] = 0
    ajouter_murs(murs,grille,i,j)
    while(len(murs)):
        index = rd.randint(0,len(murs)-1)
        mur = murs[index]
        if(nb_voisins(mur,grille) == 1):
            i,j = mur
            grille[i][j] = 0
            ajouter_murs(murs,grille,i,j)
        murs.pop(index)

    return grille

def ajouter_murs(liste_mur,grille,x,y):
    for i in range(x-1,x+2):
        if(not(dans_intervalle(i,0,NB_CASES-1))):
            continue
        if(not(grille[i][y])):
            continue
        if(not((i,y) in liste_mur)):
            liste_mur.append((i,y))
    
    for j in range(y-1,y+2):
        if(not(dans_intervalle(j,0,NB_CASES-1))):
            continue
        if(not(grille[x][j])):
            continue
        if(not((x,j) in liste_mur)):
            liste_mur.append((x,j))

def nb_voisins(mur,grille):
    x,y = mur
    nbre_voisins = 0
    for i in range(x-1,x+2):
        if(not(dans_intervalle(i,0,NB_CASES-1))):
                continue
        if(not(grille[i][y])):
            nbre_voisins += 1
    
    for j in range(y-1,y+2):
        if(not(dans_intervalle(j,0,NB_CASES-1))):
                continue
        if(not(grille[x][j])):
            nbre_voisins += 1
    return nbre_voisins

def recuperer_voisins(grille,case):
    voisins = []
    x,y = case
    for i in range(x-1,x+2):
        if(not(dans_intervalle(i,0,NB_CASES-1))):
            continue
        voisins.append((i,y))
    
    for j in range(y-1,y+2):
        if(not(dans_intervalle(j,0,NB_CASES-1))):
                continue
        voisins.append((x,j))
    return voisins



def dans_intervalle(val,mini,maxi):
    if(val < mini or val > maxi):
        return False
    return True
''' grille :
[
                [0,1,1,1,1,0,1,1,1,1],
                [0,1,1,0,0,0,0,0,0,1],
                [0,0,0,0,1,0,1,1,0,1],
                [1,1,1,1,0,0,1,1,0,1],
                [0,0,0,0,0,1,1,1,0,0],
                [0,1,1,0,0,1,0,0,0,0],
                [0,1,1,0,1,1,0,1,1,0],
                [0,1,0,0,1,0,0,1,1,0],
                [0,1,1,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0,0,0]
            ]
'''
def jeu_fini(arrivee, joueur):
    arvee_i, arvee_j = arrivee
    joueur_i, joueur_j = joueur
    return (arvee_i == joueur_i) and (arvee_j == joueur_j)


def generer_item(grille,nb_item,arrivee):
    item_liste = []
    for _ in range(nb_item):
        i,j = rd.randint(0,NB_CASES-1),rd.randint(0,NB_CASES-1)
        while grille[i][j] or (i,j) in item_liste or ((i,j) == (0,0)) or ((i,j) == arrivee):
            i,j = rd.randint(0,NB_CASES-1),rd.randint(0,NB_CASES-1)
        item_liste.append((BOMBE,(i,j)))
    return item_liste


def gerer_evenements():
    fleches = get_fleches()
    clic = last_clic()
    touche  = ''
    if(touche_enfoncee('K_e')):
        touche = 'e'
    elif(touche_enfoncee('K_q')):
        touche = 'a'
    return (touche,fleches,clic)


def recuperer_case(joueur,evenements):
    touche,fleches,clic = evenements
    x,y = fleches
    if(abs(x) >1 or abs(y) >1):
        print("pblm")
    jou_i, jou_j = joueur
    return jou_i + x, jou_j + y

def gerer_items(grille,liste_item,inventaire,joueur,evenements):
    touche, fleches, clic = evenements
    if(touche == 'e'):
        if((1,joueur) in liste_item):
            print("bombe trouvee")
            index = index_valeur(liste_item,(1,joueur))
            liste_item.pop(index)
            inventaire[BOMBE-1] +=1
    elif (touche == 'a'):
        sleep(0.1)
        if inventaire[BOMBE-1]:
            print("bombe placee")
            poser_bombe(grille,joueur)
            inventaire[BOMBE-1] -=1

def poser_bombe(grille,joueur):
    voisins = recuperer_voisins(grille,joueur)
    for voisin in voisins:
        i,j = voisin
        grille[i][j] = 0

        
def index_valeur(liste,val):
    for i,valeur in enumerate(liste):
        if(val == valeur):
            return i
    return -1

def creer_joueur():
    return (0,0)

def bouger_joueur(grille,src_pos,dest_pos):
    isrc, jsrc = src_pos
    idest, jdest = dest_pos
    if not(dans_intervalle(idest,0,NB_CASES-1) and dans_intervalle(jdest,0,NB_CASES-1)):
        return src_pos
    if abs(idest - isrc) > 1 or abs(jdest - jsrc) >1: # pas necessaire
        return src_pos
    if grille[idest][jdest]:
        return src_pos
    return dest_pos




def affiche_jeu(grille,joueur,arrivee,jeu_termine,liste_item,bouton):
    remplir_fenetre(blanc)
    if(jeu_termine):
        texte, espacement, rect = bouton
        x, y, largeur, hauteur = rect
        affiche_texte_centre("gagné !!!",(TAILLE_FENETRE//2,TAILLE_FENETRE//2),noir,50)
        affiche_rectangle((x, y), (x + largeur, y + hauteur), noir)
        affiche_texte(texte, (x + espacement, y + espacement), noir)
    else:
        dessine_grille(grille)
        for item in liste_item:
            type_item,coord = item
            item_i,item_j = coord
            dessine_cercle_centre(item_i,item_j,noir)

        joueur_i, joueur_j = joueur
        dessine_cercle_centre(joueur_i,joueur_j,rouge)

        arrivee_i, arivee_j = arrivee
        dessine_cercle_centre(arrivee_i,arivee_j,vert)


    affiche_tout()

def dessine_grille(grille):
    for i in range(NB_CASES):
        for j in range(NB_CASES):
            if grille[i][j]:
                x,y = grille2fenetre(i,j)
                affiche_rectangle_plein((x,y),(x +TAILLE_CASE, y +TAILLE_CASE),noir)

def dessine_cercle_centre(i,j,couleur):
    x, y = grille2fenetre(i,j)
    x += TAILLE_DEMI_CASE
    y += TAILLE_DEMI_CASE
    affiche_cercle_plein((x,y),TAILLE_DEMI_CASE,couleur)

def grille2fenetre(i,j):
    return (i*TAILLE_CASE, j*TAILLE_CASE)

def gen_arrivee(grille):
    i, j = NB_CASES - 1, NB_CASES - 1
    while grille[i][j] == 1:
        j -= 1

    return (i, j)


def gen_bouton(text, espacement):
    hauteur, largeur = hauteur_texte(text, 20), largeur_texte(text, 20)
    return (text,espacement,(5, 5, largeur + (2*espacement), hauteur + (2*espacement)))



TAILLE_FENETRE = 600
NB_CASES = 20

TAILLE_CASE = TAILLE_FENETRE//NB_CASES
TAILLE_DEMI_CASE = TAILLE_CASE//2

# types items
BOMBE = 1


init_fenetre(TAILLE_FENETRE,TAILLE_FENETRE,"labyrinthe")
affiche_auto_off()
joueur = creer_joueur()
grille = init_grille(joueur)
arrivee = gen_arrivee(grille)
bouton = gen_bouton("Recommencer", 5)
liste_items = generer_item(grille,3,arrivee)
evenements = ('',(0,0),(0,0))
inventaire = [0]
JEU_TERMINE = False
affiche_jeu(grille,joueur,arrivee,JEU_TERMINE,liste_items,bouton)


while pas_echap():
    JEU_TERMINE = jeu_fini(arrivee, joueur)
    evenements = gerer_evenements()
    if not(JEU_TERMINE):
        case = recuperer_case(joueur,evenements)
        joueur = bouger_joueur(grille,joueur,case)
        gerer_items(grille,liste_items,inventaire,joueur,evenements)
    affiche_jeu(grille,joueur,arrivee,JEU_TERMINE,liste_items,bouton)

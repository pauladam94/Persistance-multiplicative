
# coding: utf8

# Ce programme dessine graphiquement
# la persisance multiplicative des nombres

#importation de librairies / module
import pygame, sys
from pygame.locals import *
import Module_PM as pm

##def variable

# afficher le graphe pour le nombres 1 à n
nombre=10**7
#taille à régler pour afficher plus ou moins grand la figure
taille=1
COTE_CARRE = taille

# réglage taille de la fenetre affiché (max windows L1500 H700)
LARGEUR    = 800
HAUTEUR    = 700

#Initialisation de pygame
pygame.init()
#Initialisation de la fenetre graphique
fenetre = pygame.display.set_mode((LARGEUR,HAUTEUR))
pygame.display.set_caption("Animation1")

#Creation du coin supérieur gauche qui repère le
#carré

ABSCISSE = 0
ORDONNEE = 0
compt=1
test=0
updateur=0

###COULEUR[pm_nb(i)]

# ------------------PROGRAMME PRINCIPAL---------------------------------
#boucle infinie
while True:
#réceptionnaire evenements
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

#    pygame.draw.rect(fenetre,(0,255,255),(0,0, COTE_CARRE, COTE_CARRE))
    if test==0:
        for i in range(nombre):
            # construction des carrées choix couleur(1-2-3)
            #taille des carées et choix entre les deux programmes
            #de calcul de couleur (pm_nb() et pm_fin())
            pygame.draw.rect(fenetre,pm.COULEUR1[pm.pm_fin(i)],(ABSCISSE,ORDONNEE, COTE_CARRE, COTE_CARRE))
            if ABSCISSE==0 and ORDONNEE==0:
                ABSCISSE+=taille
            elif ABSCISSE!=0 or ORDONNEE==0:
                ABSCISSE-=taille
                ORDONNEE+=taille
            elif ABSCISSE==0:
                compt+=1
                ORDONNEE=0
                ABSCISSE=compt*taille
            updateur+=1
            if updateur==int(nombre/100):
                updateur=0
                #pygame.display.update()
                pygame.display.flip()
        test=1
#mettre a jour la fenetre
#    pygame.display.update()
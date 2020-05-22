import pygame
from pygame.locals import *

icone=pygame.image.load("dk_droite.png")
menu=pygame.image.load("menu.png")
taille_sprite=30
nombre_sprite=15
fond=pygame.image.load("fond.jpg")
depart=pygame.image.load("depart.png")
mur=pygame.image.load("mur.png")
arrivee=pygame.image.load("arrivee.png")
fenetre=pygame.display.set_mode((nombre_sprite*taille_sprite,nombre_sprite*taille_sprite))
droite=pygame.image.load("dk_droite.png")
gauche=pygame.image.load("dk_gauche.png")
haut=pygame.image.load("dk_haut.png")
bas=pygame.image.load("dk_bas.png")

import pygame
from pygame.locals import *
from classes import *
from constantes import *

pygame.init()
pygame.mixer.music.load("music.wav")
pygame.mixer.music.play()

pygame.display.set_caption("DK Labyrinthe")

fenetre=pygame.display.set_mode((nombre_sprite*taille_sprite,nombre_sprite*taille_sprite))

pygame.display.set_icon(icone)





quitter=1
continuer_menu=1
continuer_jeu=0
choix=0
while quitter==1:
    
    """ pour le menu"""
    fenetre.blit(menu,(0,0))
    pygame.display.flip()
    

    while continuer_menu==1:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type==QUIT:
                continuer_jeu=0
                continuer_menu=0
                quitter=0
            elif event.type==KEYDOWN:
                if event.key==K_F1:
                    continuer_menu=0
                    continuer_jeu=1
                    choix='n1.txt'
                elif event.key==K_F2:
                    continuer_menu=0
                    continuer_jeu=1
                    choix='n2.txt'
    if quitter==0:
        pygame.quit()
    else:
        
        fenetre.blit(fond,(0,0))
        
        
        niv=niveau(choix)
        niv.generer()
        niv.afficher()

        
        pygame.display.flip()
        click=droite

        dk=Perso(click,niv)
    

               
                    
    
                    
    while continuer_jeu==1:
        pygame.time.Clock().tick(30)
        




        for event in pygame.event.get():
            if event.type==QUIT:
                quitter=0
                continuer_jeu=0
                
            elif event.type==KEYDOWN:
                if event.key==K_RIGHT:
                    click=droite
                    
                    dk.deplacer("droite")
                if event.key==K_LEFT:
                    click=gauche
                    dk.deplacer("gauche")
                if event.key==K_UP:
                    click=haut
                    dk.deplacer("haut")
                if event.key==K_DOWN:
                    click=bas
                    dk.deplacer("bas")
        if quitter==0:
            pygame.quit()
        else:

            fenetre.blit(fond,(0,0))
            niv.afficher()
            fenetre.blit(click,(dk.x,dk.y))
            pygame.display.flip()
        
            if niv.structure[dk.ligne][dk.case]=='a':
                continuer_jeu=0
                continuer_menu=1
            








    
        












                    

import pygame
from pygame.locals import *
from constantes import *

class niveau:
    def __init__(self,choix):
        self.choix=choix
        self.structure=0


    def generer(self):

        with open(self.choix, 'r') as fichier:
            liste=[]
            for ligne in fichier:
                l=[]
                for sprite in ligne:
                    if sprite!='\n':
                        l.append(sprite)
                liste.append(l)
            self.structure=liste


    def afficher(self):
        
        x=0
        y=0

        for ligne in self.structure:
            for sprite in ligne:

                if sprite=="d":
                    fenetre.blit(depart,(x,y))
                    
                    x+=taille_sprite
                elif sprite=="0":
                    x+=taille_sprite
                elif sprite=="m":
                    fenetre.blit(mur,(x,y))
                    
                    x+=taille_sprite
                elif sprite=="a":
                    fenetre.blit(arrivee,(x,y))
                  

            y+=taille_sprite
            x=0



class Perso:
    
    def __init__(self,click,niveau):
        

        self.x=0
        self.y=0
        self.case=0
        self.ligne=0
        self.nivvv=niveau
        
        







    def deplacer(self,click):
        self.nivvv.generer()
        
        
        if click=="droite":
            
            if self.case < nombre_sprite-1:
                
                if self.nivvv.structure[self.ligne][self.case+1]!="m":
                    self.x+=taille_sprite
                    self.case+=1
                           
            
            
        elif click=="gauche":
            if self.case >0:
                if self.nivvv.structure[self.ligne][self.case-1]!="m":
                    self.x-=taille_sprite
                    self.case-=1
                        
            
         



        elif click=="haut":
            if self.ligne >0:
                
                if self.nivvv.structure[self.ligne-1][self.case]!="m":
                    self.y-=taille_sprite
                    self.ligne-=1
                         
      


        elif click=="bas":
            if self.ligne <nombre_sprite-1:
                
                if self.nivvv.structure[self.ligne+1][self.case]!="m":
                    self.y+=taille_sprite
                    self.ligne+=1
                
            
       



            
        


















    
        
                
                

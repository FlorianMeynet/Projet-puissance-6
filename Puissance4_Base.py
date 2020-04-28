#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 01:41:59 2020

@author: chendeb
"""

import http.client
import time
import numpy as np

CRED = '\33[31m'
CEND = '\033[0m'
CBLUE   = '\33[34m'

servergame="chendeb.free.fr"


def jouerWEB(idjeu,monid,tour,jeu,server=servergame):
    conn = http.client.HTTPConnection(server)
    req=conn.request("GET", "/Puissance6?status=JeJoue&idjeu="+idjeu+"&idjoueur="+monid+"&tour="+str(tour)+"&jeu="+str(jeu))
    r1 = conn.getresponse()
    return (r1.status, r1.reason)  

def getJeuAdv(idjeu,idAdv,tour,server=servergame):
    conn = http.client.HTTPConnection(server)
    req=conn.request("GET", "/Puissance6?status=GetJeuAdv&idjeu="+idjeu+"&idjoueur="+idAdv+"&tour="+str(tour))
    r1 = conn.getresponse()
    advJeu=None
    if(r1.status==200):
        temp=r1.read()
        print(temp)
        if(temp.decode('UTF-8')!='PASENCOREJOUE'):
            advJeu=int(temp)
    return advJeu  

def loopToGetJeuAdv( inetvalle,idjeu,idAdv,tour,server=servergame):
    advJeu=getJeuAdv(idjeu,idAdv,tour,server)
    while(advJeu==None):
        time.sleep(inetvalle)
        advJeu=getJeuAdv(idjeu,idAdv,tour,server)
    return advJeu

def remplirGrille(joueur, jeu):
    for i in range(grilleDim-1,-1):
        if(grille[i][jeu]==0):
            grille[i][jeu]=joueur
            break
            
def printGrille():
    for i in range(grilleDim):
        print("|",end=' ')
        for j in range(grilleDim):
            if(grille[i][j]==1):
                print(CBLUE+'0'+CEND,end=' ')
            elif grille[i][j]==2:
                print(CRED+'0'+CEND,end=' ')
            else:
                print(" ",end=' ')
            print("|",end=' ')
        print()
    print("|",end=' ')
    for i in range(grilleDim):
        print("_",end=" ")
        print("|",end=' ')
    print()
    print("|",end=' ')
    for i in range(grilleDim):
        print(i%10,end=" ")
        print("|",end=' ')
    print()
    







#############################################################
#                                                           #
#  Vous n'avez qu'a remplacer les deux methodes monjeu et   #
#      appliqueJeuAdv  selon votre IA                       #
#                                                           #
#  Bien definir un idjeu pour l'id de la partie de jeu      #
#  votre nom et celui du joueur distant                     #
#  puis bien préciser si vous commencer le jeu True,        #
#  False signifie que le joueurDistant qui commence.        #
#                                                           #
#                                                           #
#############################################################



grilleDim=12
grille=np.zeros((grilleDim,grilleDim),dtype=np.byte)



#idjeu est un id unique, si vous abondonnez une partie, pensez à créer un nouveau idjeu
idjeu="ID1504_001_2"
idjoueurLocal="Safwan"
idjoueurDistant="Christophe"

# bien préviser si vous commencer le jeu ou c'est l'adversaire qui commence
joueurLocalquiCommence=True



#cette methode est à remplacer par votre une fonction IA qui propose le jeu
def monjeu():
    a=Simulation(grille)
    print(" JE VEUX JOUER SUR LA CASE SUIVANTE SVPPPP : ", a)
    return a

def Jeufaitparminimax(grille) :
    score=Minimax_Decision(grille) #Jeu du minimax
    mouv=ValeurPossible(grille)
    meilleur=None
    for a in mouv :
        Grilleb=grille[:]
        Input(a,grille)
        if Minimax_Decision(Grilleb)>score:
            meilleur=a
    return meilleur

def Input(i,grille) :
    for j in range(6) :
        if grille[i][5-j]!=0 :
            grille[i][5-j]=1
            break
    
        
def estVictorieux(self) :
     for k in range(0,12) :
         for i in range(0,2) :
             if self[k][i]==self[k][(i+1)]==self[k][(i+2)]==self[k][(i+3)] :
                 return self[k][i]
     for i in range(0,6) :
         for k in range(0,8) :
             if self[k][i]==self[(k+1)][i]==self[(k+2)][i]==self[(k+3)][i] :
                 return self[k][i]
                
     for i in range(0,2) :
         for k in range(0,8) :
             if self[k][i]==self[(k+1)][(i+1)]==self[(i+2)][(k+2)]==self[(i+3)][(k+3)] :
                 return self[k][i]
             if self[(11-k)][(5-k)]==self[(10-k)][(4-k)]==self[(9-k)][(3-k)]==self[(8-k)][(2-k)] :
                 return self[(11-k)][(5-k)]
            
     return 0
 
def ValeurPossible(grille) :
    t=[]
    for i in range(grilleDim) :
        if grille[i][0]==0 :
            t.append(i)
    return t

def Utility(grille) :
        a=estVictorieux(grille)
        if a==joueurLocal : return 1
        if a==joueurDistant : return -1
        else : return 0
        
def Simulation(grille):
    tab = []
    liste = [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2]
    #print(ValeurPossible(grille))
    for i in ValeurPossible(grille):
        tab = grille[:]
        #print(tab)
        Input(i,tab)
        liste.append(Utility(tab))
        #print(liste)

    a = max(liste)

    for i in range (len(liste)):
        if a == liste[i]:
          return i

    

    
def Max_value(tab):
    ke=Utility(tab)
    if ke!=0 : return ke
    else :
        v=-1000
        for a in ValeurPossible(tab) :
             grilleb=tab[:]
             Input(a,grilleb)
             v=max(v,grilleb.Min_value(grilleb))
        return v
               
def Min_value(tab) :
   ke=Utility(tab)
   if ke!=0 : return ke
   else :
        v=+1000
        for a in ValeurPossible(tab) :
             grilleb=tab[:]
             Input(a,grilleb)
             v=min(v,Max_value(grilleb))
        return v
        
def Minimax_Decision(tab) :
    w=-1000
    for a in ValeurPossible(tab) :
        grilleb=tab[:]
        Input(a,grilleb)
        w=max(w,Min_value(grilleb))
    return w
    
    
# cette fonction est à remplacer une qui saisie le jeu de l'adversaire à votre IA
def appliqueJeuAdv(jeu):
    print("jeu de l'adversair est ", jeu)




if(joueurLocalquiCommence):
    joueurLocal=2
    joueurDistant=1
else:
    joueurLocal=1
    joueurDistant=2
    
    
tour=0
while(True):
    
    
    if(joueurLocalquiCommence):
        jeu=monjeu()
        jouerWEB(idjeu,idjoueurLocal,tour,jeu)
        remplirGrille(joueurLocal,jeu)
        printGrille()
        jeuAdv=loopToGetJeuAdv( 10,idjeu,idjoueurDistant,tour)
        #c'est ce jeu qu'on doit transmettre à notre IA
        appliqueJeuAdv(jeuAdv)
        remplirGrille(joueurDistant,jeuAdv)
        printGrille()
    else:
        jeuAdv=loopToGetJeuAdv( 10,idjeu,idjoueurDistant,tour)
        #c'est ce jeu qu'on doit transmettre à notre IA
        appliqueJeuAdv(jeuAdv)
        remplirGrille(joueurDistant,jeuAdv)
        printGrille()
        jeu=monjeu()
        jouerWEB(idjeu,idjoueurLocal,tour,jeu)
        remplirGrille(joueurLocal,jeu)
        printGrille()
        
    tour+=1        
    


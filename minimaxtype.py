import numpy as np

class Morpion :
    def __init__(self,grille=None) :
        if grille==None:
            self.grille=np.array([['0','0','0'],['0','0','0'],['0','0','0']])
        else:
            self.grille=grille
        
    def ajout(self,i,j,carac) :
        if carac=='+' or carac=='o'   :
            if self.grille[int(i)][int(j)]=='0' :
                self.grille[int(i)][int(j)]=str(carac)
            else :
                print("Deja prit")
        else :
            print("Erreur")
        
    def ActionsPossibles(self) : 
        L=[]
        for i in range (3) :
            for j in range (3) :
                if self.grille[i][j]!='+' or self.grille[i][j]!='o' :
                    L.append([i,j])     
        return L
    
    
    def __str__(self) :
        tect=""
        for i in range (len(self.grille)) :
            for j in range (len(self.grille[0])) :
                if self.grille[i][j]!='0' :
                    tect+= self.grille[i][j]+" | "
                else :
                    tect+=" "+" | "
            tect+="\n"
        return tect
            
    def Terminal_Test(self) :

        for i in range (0,3) :
            
            if self.grille[0][i]==self.grille[1][i] and self.grille[1][i]==self.grille[2][i] and self.grille[2][i]!='0':
                #print (self.grille[0][i] + " Vainqueur")
                return [True,self.grille[0][i]]
            
            if self.grille[i][0]==self.grille[i][1] and self.grille[i][1]==self.grille[i][2] and self.grille[i][2]!='0':
                #print (self.grille[i][0] + "Vainqueur")
                return [True,self.grille[i][0]]
            
        if self.grille[0][0]==self.grille[1][1] and self.grille[1][1]==self.grille[2][2] and self.grille[2][2]!='0':
            #print(self.grille[0][0] +" Vainqueur")
            return [True,self.grille[0][0] ]
        
        if self.grille[0][2]==self.grille[1][1] and self.grille[1][1]== self.grille[2][0]  and self.grille[2][0] !='0':
            #print(self.grille[0][2]+" Vainqueur")
            return [True, self.grille[0][2]]
        
        for i in range (0,3) :
            for j in range(0,3) :
                if self.grille[i][j]!='o' and self.grille[i][j]!='+' :
                    return [False,""]
                break
            break
                
        print("Pas de vainqueur")
        return [True,None]
        
    def Utility(self,carac) :
        if self.Terminal_Test()[0] :
            if self.Terminal_Test()[1]==carac : return 1
            if self.Terminal_Test()[1]=="" : return 0
            else : return -1

    def Max_value(self,carac) :
        if self.Terminal_Test()[0] : return self.Utility(carac)
        else :
            v=-100
            for a in self.ActionsPossibles() :
                grilleb=Morpion(self.grille[:])
                grilleb.ajout(a[0],a[1],carac)
                v=max(v,grilleb.Min_value(carac))
            return v
                
    def Min_value(self,carac) :
        if self.Terminal_Test()[0] : return self.Utility(carac)
        else :
            v=+100
            for a in self.ActionsPossibles() :
                grilleb=Morpion(self.grille[:])
                grilleb.ajout(a[0],a[1],carac)
                v=min(v,grilleb.Max_value(carac))
            return v
        
    def Minimax_Decision(self,carac) :
        w=-100
        for a in self.ActionsPossibles() :
            grilleb=Morpion(self.grille[:])
            grilleb.ajout(a[0],a[1],carac)
            w=max(w,(grilleb.Min_value(carac)))
        return w



def Jeufaitparminimax(Grillea,carac) :
    score=Grillea.Minimax_Decision(carac) #Jeu du minimax
    mouv=Grillea.ActionsPossibles()
    meilleur=None
    for a in mouv :
        Grilleb=Morpion(Grillea.grille[:])
        Grilleb.ajout(a[0],a[1],carac)
        if Grilleb.Minimax_Decision(carac)==score:
            meilleur=a
    return meilleur
   
def JEUAJOUER() :
    Grille=Morpion()
    print(Grille)
    while Grille.Terminal_Test()[0]==False :
        
        #Notre jeu
        i=input("Veuillez saisir la valeur i puis j :")
        j=input()
        print("Merci")
        Grille.ajout(i,j,'+')
        print(Grille)
        
        #jeu IA
        mouvIA=Jeufaitparminimax(Grille,'o')
        Grille.ajout(mouvIA[0],mouvIA[1],'o')
        print(Grille)
        print("A votre tour")
    
    a=Grille.Terminal_Test()[1]
    
    print(str(a) + " est notre heureux gagnant et va gagner un iphone X")
            
       
        
            
    
            
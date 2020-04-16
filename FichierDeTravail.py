import numpy as np
class Morpion : #12 colonne et 6 lignes
    def __init__(self) :
        a=np.zeros((12,6)) #0 c'est vide, 1 c'est completé par premier joueur, 2 par deuxième joueur
        self.matrice=a
    def __str__(self) :
        val=""
        for j in range(6):
            for i in range(12) :
            
                val+="  "+str(int(self.matrice[i,j]))+"  "
            val+='\n'
        val+='\n'
        for j in range(12) :
            val+=" "+str(j+1)+"   "
        
        return val
    def ajoutDunJeton(self,i,joueur1ou2) :
        for k in range(0,6) :
            if (self.matrice[i,(5-k)]==0) : 
                self.matrice[i,(5-k)]=joueur1ou2
                print("Bien joué")
                return
        print("Erreur, ligne déjà complétée")
        
    def estVictorieux(self) :
        for k in range(0,12) :
            for i in range(0,2) :
                if self.matrice[k,i]==self.matrice[k,(i+1)]==self.matrice[k,(i+2)]==self.matrice[k,(i+3)] :
                    return self.matrice[k,i]
        for i in range(0,6) :
            for k in range(0,8) :
                if self.matrice[k,i]==self.matrice[(k+1),i]==self.matrice[(k+2),i]==self.matrice[(k+3),i] :
                    return self.matrice[k,i]
                
        for i in range(0,2) :
            for k in range(0,8) :
                if self.matrice[k,i]==self.matrice[(k+1),(i+1)]==self.matrice[(i+2),(k+2)]==self.matrice[(i+3),(k+3)] :
                    return self.matrice[k,i]
                if self.matrice[(11-k),(5-k)]==self.matrice[(10-k),(4-k)]==self.matrice[(9-k),(3-k)]==self.matrice[(8-k),(2-k)] :
                    return self.matrice[(11-k),(5-k)]
            
    
                
        
a=Morpion()
print(a)
while a.estVictorieux()==0 :
    b=input("Joueur1 : Rentrer un indice de colonne")
    a.ajoutDunJeton(b,1)
    print(a)
    val=a.estVictorieux()
    if val!=0 :
        print("Lejoueur "+str(val)+" a gagné cette partie")
        break
    
    
    b=input("Joueur1 : Rentrer un indice de colonne")
    a.ajoutDunJeton(b,2)
    print(a)
    val=a.estVictorieux()
    if val!=0 :
        print("Lejoueur "+str(val)+" a gagné cette partie")
        break
    
    
                
                
        
    
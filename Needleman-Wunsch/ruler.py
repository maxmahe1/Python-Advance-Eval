import numpy as np 
from colorama import Fore, Style

class Ruler():

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.distance = int(Ruler.compute(self)[3])
    
    def red_text(text):
        return f"{Fore.RED}{text}{Style.RESET_ALL}"

    def compute(self):
        s1 = self.s1
        s2 = self.s2
        l1, l2 = len(s1), len(s2)
        M = np.zeros((l1+1, l2+1)) #On crée une matrice M et P, 2 tableaux doubles entrées avec le mot 1 en haut et le mot 2 sur le côté
        P = np.zeros((l1+1, l2+1), object)#La matrice P va servir à répertorier chaque chemin choisi (up, diag, left) afin de pouvoir décoder la séquence


#Pour gagner en généralité avec une matrice quelconque, il faut utiliser la fonction qui ramène le code ASCII des lettres en 0 et 25 (vue au début d'année on l'appelera lower)
#Il suffi ensuite d'accéder au coefficient en faisant Sij(lower(s1[i]),lower(s2[j]))

        for i in range(1, l1 + 1):
            M[i][0] = i*1 #Le 1 correspond au cout, mais il peut varier!
            P[i][0] = 'up'
            
        for i in range(1, l2 + 1):
            M[0][i] = i*1
            P[0][i] = 'left'
            
        for i in range(1, l1 + 1):
            
            for j in range(1, l2 + 1):
                if s1[i-1] == s2[j-1]:
                    new = 0 #Ici, si on avait la matrice S on devrait mettre à la place de new. S(lower(s1[i-1],lower(s2[j-1])))
                    
                elif s1[i-1] != s2[j-1]:
                    new = 1 #Idem pour ici 
                d, u, l = M[i-1][j-1] + new,  1 + M[i-1][j], 1 + M[i][j-1] 
                M[i, j] = min(d, u, l)#On applique la règle pour passer à une nouvelle case, règle obtenue sur wikipédia.
                
                if min(d, u, l) == u:
                    P[i][j] = 'up' #On complète la matrice P en conséquence
                if min(d, u, l) == d:
                    P[i][j] = 'diag'
                if min(d, u, l) == l:
                    P[i][j] = 'left'
        distance = M[l1][l2] #On accède à la distance entre 2 séquence
        
        A = [P[l1][l2]] #A est la matrice mirroire de P
        x, y = l1, l2
        a = P[x][y]

        while a != P[0][0]:#Ici on complète le reste de la matrice P, plus facile à faire car le choix de chemin est unique.
        
            if a == 'diag': 
                x, y = x-1, y-1
            if a == 'left':
                x, y = x, y-1
            if a == 'up':
                x, y = x-1, y
            a = P[x][y]
            A.insert(0, a)
        return P, M, A, distance

    def prep(self):
        def red_text(text):
            return f"{Fore.RED}{text}{Style.RESET_ALL}"
        
        s1 = self.s1
        s2 = self.s2
        A = Ruler.compute(self)[2]  # On fait machine arrière grâce à la matrice A
        l = len(A)
        L1 = []
        L2 = []
        c1, c2 = 0, 0
        for i in range(1, l): #Dans cette boucle, on reconstruit chaque séquence à partir du chemin suivi précedemment établi. Si on va en haut ou à gauche, le mot dont la lettre ne change pas se voit attribuer un '-' rouge
        
            if A[i] == 'diag':
                if s1[i-1-c1] == s2[i-1-c2]:
                    L1.append(s1[i-1-c1])
                    L2.append(s2[i-1-c2])
                if s1[i-1-c1] != s2[i-1-c2]:
                    L1.append(red_text(s1[i-1-c1]))
                    L2.append(red_text(s2[i-1-c2]))
                
            if A[i] == 'up':
                L1.append(s1[i-1-c1])
                L2.append(red_text("-"))
                c2 += 1
            if A[i] == 'left':
                L1.append(red_text("-"))
                L2.append(s2[i-1-c2])
                c1 += 1

        return (''.join(L1), ''.join(L2))

#Il ne reste plus qu'à créer la fonction qui va afficher les éléments nécessaires
    
    def report(self):
        return(Ruler.prep(self))


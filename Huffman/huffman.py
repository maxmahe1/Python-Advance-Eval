# La classe Node va servir pour initialiser les choses. Le but de l'algorithme est de construire l'arbre 
# et d'ensuite le remonter, finalement un petit peu comme le programme précèdent. 
# Les notations dg et dd correspondent à feuille droite et feuille gauche. 

class Node:
    def __init__(self,valeur, dg, dd=None):
        self.valeur = valeur
        if dd == None:
            self.name = dg
            self.dg = None
            self.dd = None

        else:
            self.name = dg.name+dd.name
            self.dg = dg
            self.dd = dd
            
    def __repr__(self):
        return f"{self.valeur}, {self.name}"

# Rentrons maintenant dans le dur en créant la classe qui crée l'arbre.
# On stock d'abord les lettre en fonction de leur fréquence d'apparition que l'on compte avec la fonction occur.
# Le programme tree lui utilise la méthode de construction vue sur l'article Wikipédia: 
# On associe les 2 noeuds de plus faible poids pour en créer un nouveau de poids égale à la somme des 2.

class TreeBuilder:
    def __init__(self, text):
        self.text = text
        self.lst = list(self.text)
        self.l_feuille = []
        
    def occur(self):
        occur = {} 
        for i in self.lst:
            if i not in occur: 
                occur[i] = 1
            else:
                occur[i] += 1 
        letters = sorted(occur.items(), key=lambda t: t[1]) 
        return letters


    def tree(self):
        Letters = self.occur()
        Tot_feuilles = []
        for i in Letters:
            Tot_feuilles.append(Node(i[1], i[0]))
        while len(Tot_feuilles) > 1:
            f1 = Tot_feuilles[0]
            f2 = Tot_feuilles[1]
            v = f1.valeur + f2.valeur 
            
            new_feuilles = Node(v, f1, f2)
            del Tot_feuilles[1]
            del Tot_feuilles[0]
            j = 0
            while j<len(Tot_feuilles) and Tot_feuilles[j].valeur <= new_feuilles.valeur:
                    j += 1
            if j == 0:
                Tot_feuilles.append(new_feuilles)
            else:
                Tot_feuilles.insert(j, new_feuilles)
        return Tot_feuilles[0]

# Quant à la classe Codec, celle-ci a pour but d'encoder et décoder la chaine. La fonction create crée la chaine.
# La fonction encode crée la chaine binaire 
# La fonction decode écrit la phrase grâce à la chaine binaire en regardant si c'est 0 ou 1 ce qui permet 
# de savoir si on va à droite ou à gauche


class Codec:
    def __init__(self, racine):
        self.racine = racine
        self.dic = {}

        
    def create(self, noeud = None, code = ""):
        if noeud == None:
            noeud = self.racine

        if len(noeud.name) == 1:
            self.dic[noeud.name] = code
        else:
            code1 = code + "0"
            code2 = code + "1"
            return self.create(noeud.dg, code1), self.create(noeud.dd, code2)

    def encode(self, text):
        codage = str()
        for i in text:
            codage += self.dic[i]
        return codage

    def decode(self, code):
        decodage = str()
        i = 0
        while i < len(code):
            noeud = self.racine
            while len(noeud.name) > 1:
                if code[i] == "0":
                    noeud = noeud.dg
                else:
                    noeud = noeud.dd
                i+=1
            decodage += noeud.name
        return decodage

text = "a dead dad ceded a bad babe a beaded abaca bed"

builder = TreeBuilder(text)
binary_tree = builder.tree()
codec = Codec(binary_tree)
codec.create()     
encoded = codec.encode(text)
decoded=codec.decode(encoded)
print(f"{text}\n{encoded}")

if decoded != text:
    print("OOPS")
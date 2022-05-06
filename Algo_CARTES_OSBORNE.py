class Carte :
    def __init__(self,mana,nom,descrip):
        self.__mana = mana
        self.__name = nom
        self.__descrip = descrip
        
    def getName(self):
        return self.__name

    def getMana(self):
        return self.__mana

    def getDescrip(self):
        return self.__descrip

class Abstraite_Carte :
    def __init__(self,attributs,fonctions):
        self.__attributs = attributs
        self.__fonctions = fonctions

    def getAttributs(self):
        return self.__attributs

    def getFonctions(self):
        return self.__fonctions    


class Mage :
    def __init__(self,pv,total,valeur_mana,main,defausse,zone,action,recupere_mana,attaque,degats):
            self.__pv = pv
            self.__total = total
            self.__vm = valeur_mana

            self.__main = main
            self.__defausse = defausse
            self.__zone = zone

            self.__action = action
            self.__rm = recupere_mana
            self.__attaque = attaque

            self.__degats = 1

# e-Mage 

    def __e_Mage__(self,nom):
        self._vm = 0
        self._action = False
    def rm(self,nombre):
        self.__rm -= nombre
        if(self.__rm<=0):
            self.__rm=0
        return self.__rm
    def attaque(self,nombre):
        self.__attaque += nombre
        return self.__attaque
   


    def getPoints_De_Vie(self):
        return self.__pv

    def getTotal(self):
        return self.__total

    def getValeur_Actuelle_Mana(self):
        return self.__vm

    
    def getMain(self):
        return self.__main

    def getDefausse(self):
        return self.__defausse

    def getZone_Jeu(self):
        return self.__zone

    
    def getAction(self):
        return self.__action

    def getRecupereMana(self):
        return self.__rm

    def getAttaque(self):
        return self.__attaque

    
    def getDegats(self):
        return self.__degats



class Cristal(Carte):
    def __init__(self,name,valeur):
        Carte.__init__(self,name)
        self.__valeur = valeur
    def affiche(self):
        print ("vous avez " + str(self.mana) + " " + self.name)

#programme principal
    def action(self):
        if(self.valeur==0):
            self.mana = self.mana - 1
            print("Vous utilisez " + self.name + "cela vous coûte " + str(self.mana))
        if(self.e_mage):
            self.mana = self.mana + valeur
            print("Vous utilisez " + self.name + "Vous restez dans votre zone de jeu rt votre mana maximum augmente de sa valeur")



class Creature(Carte):
    def __init__(self,name,pv_creature,score_attaque):
        Carte.__init__(self,name)
        self.__pv_creature = pv_creature
        self.__score_attaque = score_attaque
        
    def getPVMonstre(self):
        return self.__pv_creature

    def getScoreAttaque(self):
        return self.__score_attaque

#programme principal
    def action(self):
        if(self.valeur==0):
            self.mana = self.mana - 1
            print("Vous utilisez " + self.name + "cela vous coûte " + str(self.mana))
        if(self.attaque):
            self.pv = self.pv - degats
            print("Vous avez attaqué " + self.name + "Vous perdez des points de vies")
        if(self.attaque):
            self.pv = self.pv <= degats
            print("Vous avez attaqué " + self.name + "Vous avez perdu toutes vos points de vies, votre creature va donc à la défausse")
    

class Blast(Carte):
    def __init__(self,name,valeur_blast):
        Carte.__init__(self,name)
        self.__valeur_blast = valeur_blast
        
#main

      




    



    

    



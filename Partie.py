class Partie:
    def __init__(self):
        super().__init__()
        self.tab = None 

    def taille(self):
        test_taille = 0

        while test_taille == 0:
            user_taille = input('Quel taille de plateau souhaitez vous ? (entrez la taille de la forme longeur*largeur, avec un max de 20 et un min de 8)').split("*",)

            if int(user_taille[0]) > 20 or int(user_taille[1]) > 20 or int(user_taille[0]) < 8 or int(user_taille[1]) < 8:
                test_taille = 0
            else:
                test_taille = 1

        return user_taille


    def coup(self):
        coord = input("Ou souhaitez vous jouer ? (Saisir les coordonnées séparer pas un \';\') ").split(";",)
        return coord
    
    
    def validite(self,coup, tableau):
        #récupération des coordonées ou le joueur souhaite poser son pion 
        cl = int(coup[0])
        lg = int(coup[1])

        #vérification si la case est déjà prise par un autre pion
        if tableau[lg][cl] == " X " or tableau[lg][cl] == " 0 ":
            return 1
        else:
            return 0

        

    def ajout_pion(self, coup, tableau, pion):
        if pion == 1:
            tableau[int(coup[1])][int(coup[0])] = " X "
            self.tab = tableau

        if pion == 0:
            tableau[int(coup[1])][int(coup[0])] = " 0 "
            self.tab = tableau



    def inversement(self, tableau, coup, pion):
        cl = int(coup[0])
        lg = int(coup[1])

        if pion == 1:
            a = " X "
            b = " 0 "

        elif pion == 0:
            a = " 0 "
            b = " X "


        if tableau[lg][cl] == a:                          #droite du pion joué
            if tableau[lg][cl + 1] == b:
                ncl = cl + 1
                
                while tableau[lg][ncl] == b:
                    ncl += 1
                    if tableau[lg][ncl] == a:
                        ncl = cl + 1
                        while tableau[lg][ncl] == b:
                            tableau[lg][ncl] = a
                            ncl += 1

            
            if tableau[lg][cl - 1] == b:                     #gauche du pion joué            
                ncl = cl - 1
                
                while tableau[lg][ncl] == b:
                    ncl -= 1
                    if tableau[lg][ncl] == a:
                        ncl = cl - 1
                        while tableau[lg][ncl] == b:
                            tableau[lg][ncl] = a
                            ncl -= 1
            

            if tableau[lg + 1][cl] == b:        #En bas du pion joué 
                nlg = lg + 1
                
                while tableau[nlg][cl] == b:
                    nlg += 1
                    if tableau[nlg][cl] == a:
                        nlg = lg + 1
                        while tableau[nlg][cl] == b:
                            tableau[nlg][cl] = a
                            nlg += 1

            if tableau[lg - 1][cl] == b:            #En haut du pion joué 
                nlg = lg - 1
                print("TEST")
                while tableau[nlg][cl] == b:
                    nlg -= 1
                    if tableau[nlg][cl] == a:
                        nlg = lg - 1
                        while tableau[nlg][cl] == b:
                            tableau[nlg][cl] = a
                            nlg -= 1

            if tableau[lg + 1][cl + 1] == b:            #En bas à droite du pion joué 
                nlg = lg + 1
                ncl = cl + 1
                while tableau[nlg][ncl] == b:
                    nlg += 1
                    ncl += 1
                    if tableau[nlg][ncl] == a:
                        nlg = lg + 1
                        ncl = cl + 1
                        while tableau[nlg][ncl] == b:
                            tableau[nlg][ncl] = a
                            nlg += 1
                            ncl += 1

            if tableau[lg - 1][cl - 1] == b:            #En haut à gauche du pion joué 
                nlg = lg - 1
                ncl = cl - 1
                while tableau[nlg][ncl] == b:
                    nlg -= 1
                    ncl -= 1
                    if tableau[nlg][ncl] == a:
                        nlg = lg - 1
                        ncl = cl - 1
                        while tableau[nlg][ncl] == b:
                            tableau[nlg][ncl] = a
                            nlg -= 1
                            ncl -= 1

            if tableau[lg - 1][cl + 1] == b:            #En haut à droite auche du pion joué 
                nlg = lg - 1
                ncl = cl + 1
                while tableau[nlg][ncl] == b:
                    nlg -= 1
                    ncl += 1
                    if tableau[nlg][ncl] == a:
                        nlg = lg - 1
                        ncl = cl + 1
                        while tableau[nlg][ncl] == b:
                            tableau[nlg][ncl] = a
                            nlg -= 1
                            ncl += 1
            
            if tableau[lg + 1][cl - 1] == b:            #En bas à gauche auche du pion joué 
                nlg = lg + 1
                ncl = cl - 1
                while tableau[nlg][ncl] == b:
                    nlg += 1
                    ncl -= 1
                    if tableau[nlg][ncl] == a:
                        nlg = lg + 1
                        ncl = cl - 1
                        while tableau[nlg][ncl] == b:
                            tableau[nlg][ncl] = a
                            nlg += 1
                            ncl -= 1
                

    
        
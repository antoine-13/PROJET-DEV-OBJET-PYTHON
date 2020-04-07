class Partie:
    def __init__(self):
        super().__init__()
        self.tab = None 

    
    def initialisation(self):
        #création du tableau
        cases = [] 
        i = 9
        j = 8

        for a in range(1,i):
            cases.append([" . "] * j)

        cases[3][3] = " X "
        cases[3][4] = " 0 "
        cases[4][3] = " 0 "
        cases[4][4] = " X "

        return cases

    def menu(self):
        valeur = int(input("Que souhaitez vous faire ? ( 1- poser un pion X; 2-poser un pion 0; 3- passer votre tour)"))
        return valeur

    def coup(self):
        coord = input("Ou souhaitez vous jouer ? (Saisir les coordonnées séparer pas un \';\') ").split(";",)
        return coord
    
    
    def validite(self,coup, tableau):
        cl = int(coup[0]) - 1
        lg = int(coup[1]) - 1
        if tableau[lg][cl] == " X " or tableau[lg][cl] == " 0 ":
            return 1

        else:
            return 0

    def ajout_pion(self, coup, tableau, pion):
        if pion == 1:
            tableau[int(coup[1]) - 1][int(coup[0]) - 1] = " X "
            self.tab = tableau

        if pion == 2:
            tableau[int(coup[1]) - 1][int(coup[0]) - 1] = " 0 "
            self.tab = tableau



    def inversement(self, tableau, coup, pion):
        cl = int(coup[0]) - 1
        lg = int(coup[1]) - 1

        if pion == 1:
            a = " X "
            b = " 0 "

        if pion == 2:
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

            
            if tableau[lg][cl - 1] == b:                     #gauche du pion joué            
                ncl = cl - 1
                while tableau[lg][ncl] == b:
                    ncl -= 1
                    if tableau[lg][ncl] == a:
                        ncl = cl - 1
                        while tableau[lg][ncl] == b:
                            tableau[lg][ncl] = a
            

            if tableau[lg + 1][cl] == b:        #En haut du pion joué 
                nlg = lg + 1
                while tableau[nlg][cl] == b:
                    nlg += 1
                    if tableau[nlg][cl] == a:
                        nlg = lg + 1
                        while tableau[nlg][cl] == b:
                            tableau[nlg][cl] = a

            if tableau[lg - 1][cl] == b:            #En bas du pion joué 
                nlg = lg - 1
                while tableau[nlg][cl] == b:
                    nlg -= 1
                    if tableau[nlg][cl] == a:
                        nlg = lg - 1
                        while tableau[nlg][cl] == b:
                            tableau[nlg][cl] = a

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
                

    
        
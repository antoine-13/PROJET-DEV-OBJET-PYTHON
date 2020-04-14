class Partie:
    def __init__(self):
        super().__init__()
        self.tab = None 
        self.nbr_joueurs = 2
        self.tour = 1
        self.joueurs_du_tour = [1] * 1
        self.non_joueurs = [1] * 3

    def joueurs(self):
        type_pion = self.tour % self.nbr_joueurs
        
        if type_pion == 1:
            self.joueurs_du_tour[0] = " X "
            self.non_joueurs[0] = " 0 "
            self.non_joueurs[1] = " Y "
            self.non_joueurs[2] = " U "
        elif type_pion == 0:
            self.joueurs_du_tour[0] = " 0 "
            self.non_joueurs[0] = " X "
            self.non_joueurs[1] = " Y "
            self.non_joueurs[2] = " U "
           
        elif type_pion == 2:
            self.joueurs_du_tour[0] = " Y "
            self.non_joueurs[0] = " 0 "
            self.non_joueurs[1] = " X "
            self.non_joueurs[2] = " U "
           
        elif type_pion == 3:
            self.joueurs_du_tour[0] = " U "
            self.non_joueurs[0] = " 0 "
            self.non_joueurs[1] = " Y "
            self.non_joueurs[2] = " X "
            

    def coup(self):
        coord = input("Ou souhaitez vous jouer ? (Saisir les coordonnées séparer pas un \';\') ").split(";",)
        return coord
    
    
    def validite_case(self,coup, tableau):
        #récupération des coordonées ou le joueur souhaite poser son pion 
        cl = int(coup[0])
        lg = int(coup[1])
       
        #vérification si la case est déjà prise par un autre pion
        if tableau[lg][cl] == " X " or tableau[lg][cl] == " 0 ":
            return 1
        else:
            return 0

    def validite_pos(self, coup, tableau):
        #récupération des coordonées ou le joueur souhaite poser son pion 
        cl = int(coup[0])
        lg = int(coup[1])
        a = self.joueurs_du_tour[0]
        b = self.non_joueurs[0]
        c = self.non_joueurs[1]
        d = self.non_joueurs[2]

        for b in self.non_joueurs:                       
            if tableau[lg][cl + 1] == b or tableau[lg][cl + 1] == c or tableau[lg][cl + 1] == d:  #droite du pion joué
                ncl = cl + 1
                while tableau[lg][ncl] == b or tableau[lg][ncl] == c or tableau[lg][ncl] == d:
                    ncl += 1
                if tableau[lg][ncl] == a:
                    return 1

            if tableau[lg][cl - 1] == b or tableau[lg][cl - 1] == c or tableau[lg][cl - 1] == d:  #gauche du pion joué
                ncl = cl - 1
                while tableau[lg][ncl] == b or tableau[lg][ncl] == c or tableau[lg][ncl] == d:
                    ncl -= 1
                if tableau[lg][ncl] == a:
                    return 1

            if tableau[lg - 1][cl] == b or tableau[lg - 1][cl] == c or tableau[lg - 1][cl] == d:  #en haut du pion joué
                nlg = lg - 1
                while tableau[nlg][cl] == b or tableau[nlg][cl] == c or tableau[nlg][cl] == d:
                    nlg -= 1
                if tableau[nlg][cl] == a:
                    return 1
            
            if tableau[lg + 1][cl] == b or tableau[lg + 1][cl] == c or tableau[lg + 1][cl] == d:  #en bas du pion joué
                nlg = lg + 1
                while tableau[nlg][cl] == b or tableau[nlg][cl] == c or tableau[nlg][cl] == d:
                    nlg += 1
                if tableau[nlg][cl] == a:
                    return 1

            if tableau[lg + 1][cl + 1] == b or tableau[lg + 1][cl + 1] == c or tableau[lg + 1][cl + 1] == d:  #en bas a droite du pion joué
                nlg = lg + 1
                ncl = cl + 1
                while tableau[nlg][ncl] == b or tableau[nlg][ncl] == c or tableau[nlg][ncl] == d:
                    nlg += 1
                    ncl += 1
                if tableau[nlg][ncl] == a:
                    return 1

            if tableau[lg + 1][cl - 1] == b or tableau[lg + 1][cl - 1] == c or tableau[lg + 1][cl - 1] == d:  #en bas a gauche du pion joué
                nlg = lg + 1
                ncl = cl - 1
                while tableau[nlg][ncl] == b or tableau[nlg][ncl] == c or tableau[nlg][ncl] == d:
                    nlg += 1
                    ncl -= 1
                if tableau[nlg][ncl] == a:
                    return 1

            if tableau[lg - 1][cl - 1] == b or tableau[lg - 1][cl - 1] == c or tableau[lg - 1][cl - 1] == d:  #en haut a gauche du pion joué
                nlg = lg - 1
                ncl = cl - 1
                while tableau[nlg][ncl] == b or tableau[nlg][ncl] == c or tableau[nlg][ncl] == d:
                    nlg -= 1
                    ncl -= 1
                if tableau[nlg][ncl] == a:
                    return 1

            if tableau[lg - 1][cl + 1] == b or tableau[lg - 1][cl + 1] == c or tableau[lg - 1][cl + 1] == d:  #en haut a gauche du pion joué
                nlg = lg - 1
                ncl = cl + 1
                while tableau[nlg][ncl] == b or tableau[nlg][ncl] == c or tableau[nlg][ncl] == d:
                    nlg -= 1
                    ncl += 1
                if tableau[nlg][ncl] == a:
                    return 1

            
        return 0
        

    def ajout_pion(self, coup, tableau):

            tableau[int(coup[1])][int(coup[0])] = self.joueurs_du_tour[0]
            self.tab = tableau




    def inversement(self, tableau, coup):
        cl = int(coup[0])
        lg = int(coup[1])
        a = self.joueurs_du_tour[0]
        b = self.non_joueurs[0]
        c = self.non_joueurs[1]
        d = self.non_joueurs[2]
        
        if tableau[lg][cl] == a:                          #droite du pion joué
            if tableau[lg][cl + 1] == b or tableau[lg][cl + 1] == c or tableau[lg][cl + 1] == d:
                ncl = cl + 1
                while tableau[lg][ncl] == b or tableau[lg][ncl] == c or tableau[lg][ncl] == d:
                    ncl += 1
                    if tableau[lg][ncl] == a:
                        ncl = cl + 1
                        while tableau[lg][ncl] == b or tableau[lg][ncl] == c or tableau[lg][ncl] == d:
                            tableau[lg][ncl] = a
                            pion = [1] * 2
                            pion[0] = ncl
                            pion[1] = lg
                            self.inversement(tableau, pion)
                            ncl += 1

            
            if tableau[lg][cl - 1] == b or tableau[lg][cl - 1] == c or tableau[lg][cl - 1] == d:                     #gauche du pion joué            
                ncl = cl - 1
                while tableau[lg][ncl] == b or tableau[lg][ncl] == c or tableau[lg][ncl] == d:
                    ncl -= 1
                    if tableau[lg][ncl] == a:
                        ncl = cl - 1
                        while tableau[lg][ncl] == b or tableau[lg][ncl] == c or tableau[lg][ncl] == d:
                            tableau[lg][ncl] = a
                            pion = [1] * 2
                            pion[0] = ncl
                            pion[1] = lg
                            self.inversement(tableau, pion)
                            ncl -= 1
            

            if tableau[lg + 1][cl] == b or tableau[lg + 1][cl] == c or tableau[lg + 1][cl] == d:        #En bas du pion joué 
                nlg = lg + 1
                
                while tableau[nlg][cl] == b or tableau[nlg][cl] == c or tableau[nlg][cl] == d:
                    nlg += 1
                    if tableau[nlg][cl] == a:
                        nlg = lg + 1
                        while tableau[nlg][cl] == b or tableau[nlg][cl] == c or tableau[nlg][cl] == d:
                            tableau[nlg][cl] = a
                            pion = [1] * 2
                            pion[0] = cl
                            pion[1] = nlg
                            self.inversement(tableau, pion)
                            nlg += 1

            if tableau[lg - 1][cl] == b or tableau[lg - 1][cl] == c or tableau[lg - 1][cl] == d:            #En haut du pion joué 
                nlg = lg - 1
                while tableau[nlg][cl] == b or tableau[nlg][cl] == c or tableau[nlg][cl] == d:
                    nlg -= 1
                    if tableau[nlg][cl] == a:
                        nlg = lg - 1
                        while tableau[nlg][cl] == b or tableau[nlg][cl] == c or tableau[nlg][cl] == d:
                            tableau[nlg][cl] = a
                            pion = [1] * 2
                            pion[0] = cl
                            pion[1] = nlg
                            self.inversement(tableau, pion)
                            nlg -= 1

            if tableau[lg + 1][cl + 1] == b or tableau[lg + 1][cl + 1] == c or tableau[lg + 1][cl + 1] == d:            #En bas à droite du pion joué 
                nlg = lg + 1
                ncl = cl + 1
                while tableau[nlg][ncl] == b or tableau[nlg][ncl] == c or tableau[nlg][ncl] == d:
                    nlg += 1
                    ncl += 1
                    if tableau[nlg][ncl] == a:
                        nlg = lg + 1
                        ncl = cl + 1
                        while tableau[nlg][ncl] == b or tableau[nlg][ncl] == c or tableau[nlg][ncl] == d:
                            tableau[nlg][ncl] = a
                            pion = [1] * 2
                            pion[0] = ncl
                            pion[1] = nlg
                            self.inversement(tableau, pion)
                            nlg += 1
                            ncl += 1

            if tableau[lg - 1][cl - 1] == b or tableau[lg - 1][cl - 1] == c or tableau[lg - 1][cl - 1] == d:            #En haut à gauche du pion joué 
                nlg = lg - 1
                ncl = cl - 1
                while tableau[nlg][ncl] == b or tableau[nlg][ncl] == c or tableau[nlg][ncl] == d:
                    nlg -= 1
                    ncl -= 1
                    if tableau[nlg][ncl] == a:
                        nlg = lg - 1
                        ncl = cl - 1
                        while tableau[nlg][ncl] == b or tableau[nlg][ncl] == c or tableau[nlg][ncl] == d:
                            tableau[nlg][ncl] = a
                            pion = [1] * 2
                            pion[0] = ncl
                            pion[1] = nlg
                            self.inversement(tableau, pion)
                            nlg -= 1
                            ncl -= 1

            if tableau[lg - 1][cl + 1] == b or tableau[lg - 1][cl + 1] == c or tableau[lg - 1][cl + 1] == d:            #En haut à droite auche du pion joué 
                nlg = lg - 1
                ncl = cl + 1
                while tableau[nlg][ncl] == b or tableau[nlg][ncl] == c or tableau[nlg][ncl] == d:
                    ncl += 1
                    if tableau[nlg][ncl] == a:
                        nlg = lg - 1
                        ncl = cl + 1
                        while tableau[nlg][ncl] == b or tableau[nlg][ncl] == c or tableau[nlg][ncl] == d:
                            tableau[nlg][ncl] = a
                            pion = [1] * 2
                            pion[0] = ncl
                            pion[1] = nlg
                            self.inversement(tableau, pion)
                            nlg -= 1
                            ncl += 1
            
            if tableau[lg + 1][cl - 1] == b or tableau[lg + 1][cl - 1] == c or tableau[lg + 1][cl - 1] == d:            #En bas à gauche auche du pion joué 
                nlg = lg + 1
                ncl = cl - 1
                while tableau[nlg][ncl] == b or tableau[nlg][ncl] == c or tableau[nlg][ncl] == d:
                    nlg += 1
                    ncl -= 1
                    if tableau[nlg][ncl] == a:
                        nlg = lg + 1
                        ncl = cl - 1
                        while tableau[nlg][ncl] == b or tableau[nlg][ncl] == c or tableau[nlg][ncl] == d:
                            tableau[nlg][ncl] = a
                            pion = [1] * 2
                            pion[0] = ncl
                            pion[1] = nlg
                            self.inversement(tableau, pion)
                            nlg += 1
                            ncl -= 1
                

    
        
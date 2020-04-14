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

        for b in self.non_joueurs:                       
            if tableau[lg][cl + 1] == b:  #droite du pion joué
                ncl = cl + 1
                while tableau[lg][ncl] == b:
                    ncl += 1
                if tableau[lg][ncl] == a:
                    return 1

            if tableau[lg][cl - 1] == b:  #gauche du pion joué
                ncl = cl - 1
                while tableau[lg][ncl] == b:
                    ncl -= 1
                if tableau[lg][ncl] == a:
                    return 1

            if tableau[lg - 1 ][cl] == b:  #en haut du pion joué
                nlg = lg - 1
                while tableau[nlg][cl] == b:
                    nlg -= 1
                if tableau[nlg][cl] == a:
                    return 1
            
            if tableau[lg + 1 ][cl] == b:  #en bas du pion joué
                nlg = lg + 1
                while tableau[nlg][cl] == b:
                    nlg += 1
                if tableau[nlg][cl] == a:
                    return 1

            if tableau[lg + 1 ][cl + 1] == b:  #en bas a droite du pion joué
                nlg = lg + 1
                ncl = cl + 1
                while tableau[nlg][ncl] == b:
                    nlg += 1
                    ncl += 1
                if tableau[nlg][ncl] == a:
                    return 1

            if tableau[lg + 1 ][cl - 1] == b:  #en bas a gauche du pion joué
                nlg = lg + 1
                ncl = cl - 1
                while tableau[nlg][ncl] == b:
                    nlg += 1
                    ncl -= 1
                if tableau[nlg][ncl] == a:
                    return 1

            if tableau[lg - 1 ][cl - 1] == b:  #en haut a gauche du pion joué
                nlg = lg - 1
                ncl = cl - 1
                while tableau[nlg][ncl] == b:
                    nlg -= 1
                    ncl -= 1
                if tableau[nlg][ncl] == a:
                    return 1

            if tableau[lg - 1 ][cl + 1] == b:  #en haut a gauche du pion joué
                nlg = lg - 1
                ncl = cl + 1
                while tableau[nlg][ncl] == b:
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

        for b in self. non_joueurs:
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
                

    
        
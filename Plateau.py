class Plateau:
    def __init__(self):
        super().__init__()
        self.dimenssion = "8*8".split("*",)
        self.compteur_X = 0
        self.compteur_0 = 0
        self.compteur_Y = 0
        self.compteur_U = 0
        self.compteur_case_vide = 0
        
    
    def initialisation(self, nbr_joueurs):
        #création du tableau
        cases = [] 
        i = int(self.dimenssion[1])
        j = int(self.dimenssion[0])

        for a in range(0,i+2):
            cases.append([" . "] * (j+2))

        if nbr_joueurs == 2:
            cases[int(int(self.dimenssion[1])/2)][int(int(self.dimenssion[0])/2)] = " 0 "
            cases[int(int(self.dimenssion[1])/2)][int((int(self.dimenssion[0])/2) + 1)] = " X "
            cases[int((int(self.dimenssion[1])/2 + 1))][int(int(self.dimenssion[0])/2)] = " X "
            cases[int((int(self.dimenssion[1])/2) + 1)][int((int(self.dimenssion[0])/2) + 1)] = " 0 "
        if nbr_joueurs == 3:
            cases[int(int(self.dimenssion[1])/2)][int(int(self.dimenssion[0])/2)] = " Y "
            cases[int(int(self.dimenssion[1])/2)][int((int(self.dimenssion[0])/2) + 1)] = " 0 "
            cases[int((int(self.dimenssion[1])/2 + 1))][int(int(self.dimenssion[0])/2)] = " X "
        if nbr_joueurs == 4:
            cases[int(int(self.dimenssion[1])/2)][int(int(self.dimenssion[0])/2)] = " Y "
            cases[int(int(self.dimenssion[1])/2)][int((int(self.dimenssion[0])/2) + 1)] = " 0 "
            cases[int((int(self.dimenssion[1])/2 + 1))][int(int(self.dimenssion[0])/2)] = " X "
            cases[int((int(self.dimenssion[1])/2) + 1)][int((int(self.dimenssion[0])/2) + 1)] = " U "

        return cases

    def affiche(self, tableau, dimenssion):
        #gère l'affichage du plateau 

        #affiche les chiffres des collonnes
        print("")
        print("   | ", end="")
        for a in range(1, int(dimenssion[0]) + 1):
            if a < 10:
                print("0", a, " ", sep='', end='')
            else:
                print(a, " ", sep='', end = '')
        print("")

        print("---", "---" * int(dimenssion[0]), "--", sep="" )
      
            
        i = 0
        
        for a in tableau:
            if i >= 1 and i <= int(dimenssion[0]):
                if i < 10:
                    print("0", i, " ", end='|', sep='')
                else:
                    print(i, " ", end='|', sep='')
                
                compteur_cl = 0
                for b in a:
                    if compteur_cl >= 1 and compteur_cl <= int(dimenssion[1]):
                        print(b, end='')

                    compteur_cl += 1

                print("")
            i += 1
            

        print("")

    def joueur_eliminer(self, tour, nbr_joueurs):
        type_pion = tour % nbr_joueurs
        
        if type_pion == 1:
            if self.compteur_X == 0:
                return 1
            else:
                return 0

        elif type_pion == 0:
            if self.compteur_0 == 0:
                return 1
            else:
                return 0
           
        elif type_pion == 2:
            if self.compteur_Y == 0:
                return 1
            else:
                return 0
            
        elif type_pion == 3:
            if self.compteur_U == 0:
                return 1
            else:
                return 0
            


    def test(self, tableau):
        #gère la fin ou non de la partie
        self.compteur_X = 0
        self.compteur_0 = 0
        self.compteur_Y = 0
        self.compteur_U = 0
        self.compteur_case_vide = 0
        for a in tableau:
            for b in a:
                if b == " X ":
                    self.compteur_X += 1

                elif b == " 0 ":
                    self.compteur_0 += 1

                elif b == " Y ":
                    self.compteur_Y += 1
                
                elif b == " U ":
                    self.compteur_U += 1
                else:
                    self.compteur_case_vide += 1

        if self.compteur_case_vide == 0:
            compteurs = [self.compteur_0, self.compteur_X, self.compteur_U, self.compteur_Y]
            maxi = max(compteurs)

            if self.compteur_0 == maxi:
                print("")
                print("")
                print("------------------------------------------- 0 à gagné ! ----------------------------------------------------")
                return 1
            
            if self.compteur_X == maxi:
                print("")
                print("")
                print("------------------------------------------- X à gagné ! ----------------------------------------------------")
                return 1
            
            if self.compteur_Y == maxi:
                print("")
                print("")
                print("------------------------------------------- Y à gagné ! ----------------------------------------------------")
                return 1
            
            if self.compteur_U == maxi:
                print("")
                print("")
                print("------------------------------------------- U à gagné ! ----------------------------------------------------")
                return 1

        elif self.compteur_0 == 0 and self.compteur_Y == 0 and self.compteur_U == 0 and self.compteur_X > 0:
            print("")
            print("")
            print("------------------------------------------- X à gagné ! ---------------------------------------------------")
            return 1

        elif self.compteur_X == 0 and self.compteur_Y == 0 and self.compteur_U == 0 and self.compteur_0 > 0:
            print("")
            print("")
            print("------------------------------------------- 0 à gagné ! ----------------------------------------------------")
            return 1
        
        elif self.compteur_X == 0 and self.compteur_0 == 0 and self.compteur_U == 0 and self.compteur_Y > 0:
            print("")
            print("")
            print("------------------------------------------- Y à gagné ! ----------------------------------------------------")
            return 1

        elif self.compteur_X == 0 and self.compteur_Y == 0 and self.compteur_0 == 0 and self.compteur_U > 0:
            print("")
            print("")
            print("------------------------------------------- U à gagné ! ----------------------------------------------------")
            return 1
            
        else:
            return 0
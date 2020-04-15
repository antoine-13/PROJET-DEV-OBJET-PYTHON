###########################################################################################
#                                                                                         #
#                                                                                         #
#                                      Classe Plateau:                                    #
#                                                                                         #
#                           affiche et demande ce que l'utilisateur                       #
#                           veux faire au début                                           #
#                                                                                         #
#                                                                                         #
###########################################################################################

class Plateau:

    #definition des attributs de plateau
    def __init__(self):

        #initialisation de la taille du plateau
        self.dimenssion = "8*8".split("*")

        #initialisation des compteurs de pions
        self.compteur_X = 0
        self.compteur_0 = 0
        self.compteur_Y = 0
        self.compteur_U = 0
        self.compteur_case_vide = 0
        
    #methode initialisation qui crée le tableau et les position initiale des pions 
    def initialisation(self, nbr_joueurs):
        #création du tableau
        cases = [] 
        i = int(self.dimenssion[1])
        j = int(self.dimenssion[0])
        

        for a in range(0,i+2):
            cases.append([" . "] * (j+2))

        
        if nbr_joueurs == 2: #si il y a 2  joueurs
            cases[int(int(self.dimenssion[1])/2)][int(int(self.dimenssion[0])/2)] = " 0 "
            cases[int(int(self.dimenssion[1])/2)][int((int(self.dimenssion[0])/2) + 1)] = " X "
            cases[int((int(self.dimenssion[1])/2 + 1))][int(int(self.dimenssion[0])/2)] = " X "
            cases[int((int(self.dimenssion[1])/2) + 1)][int((int(self.dimenssion[0])/2) + 1)] = " 0 "

        if nbr_joueurs == 3: #Si il y a 3 joueurs
            cases[int(int(self.dimenssion[1])/2)][int(int(self.dimenssion[0])/2)] = " Y "
            cases[int(int(self.dimenssion[1])/2) + 1][int(int(self.dimenssion[0])/2) + 1] = " Y "
            cases[int(int(self.dimenssion[1])/2)][int((int(self.dimenssion[0])/2) + 1)] = " 0 "
            cases[int(int(self.dimenssion[1])/2) + 1][int((int(self.dimenssion[0])/2) + 2)] = " 0 "
            cases[int((int(self.dimenssion[1])/2 + 1))][int(int(self.dimenssion[0])/2)] = " X "
            cases[int((int(self.dimenssion[1])/2))][int(int(self.dimenssion[0])/2) + 2] = " X "


        if nbr_joueurs == 4: #Si il y a 4 joueurs
            cases[int(int(self.dimenssion[1])/2)][int(int(self.dimenssion[0])/2)] = " Y "
            cases[int(int(self.dimenssion[1])/2) + 1][int(int(self.dimenssion[0])/2) + 2] = " Y "
            cases[int(int(self.dimenssion[1])/2)][int((int(self.dimenssion[0])/2) + 1)] = " 0 "
            cases[int(int(self.dimenssion[1])/2) + 1][int((int(self.dimenssion[0])/2) - 1)] = " 0 "
            cases[int((int(self.dimenssion[1])/2 + 1))][int(int(self.dimenssion[0])/2)] = " X "
            cases[int((int(self.dimenssion[1])/2))][int(int(self.dimenssion[0])/2) + 2] = " X "
            cases[int((int(self.dimenssion[1])/2) + 1)][int((int(self.dimenssion[0])/2) + 1)] = " U "
            cases[int((int(self.dimenssion[1])/2))][int((int(self.dimenssion[0])/2) - 1)] = " U "

        return cases #on retourne le tableau initialisé

    #Methode qui gère l'affichage tu tableau
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
        for a in tableau:                                       #Pour chaque ligne
            if i >= 1 and i <= int(dimenssion[1]):
                if i < 10:
                    print("0", i, " ", end='|', sep='')            #affichage des numero des lignes
                else:
                    print(i, " ", end='|', sep='')                  #affichage des numero des lignes
                
                compteur_lg = 0 
                for b in a:                                       #Pour chaque collones
                    if compteur_lg >= 1 and compteur_lg <= int(dimenssion[0]):
                        print(b, end='')                                        #on affiche le contenu de la case du tableau

                    compteur_lg += 1

                print("")
            i += 1
            

        print("")                           #Print pour faire un retour à la ligne pour l'estéthique 

    #Methode pour savoir si un joueur est éléminer 
    def joueur_eliminer(self, tour, nbr_joueurs):
        type_pion = tour % nbr_joueurs
        
        if type_pion == 1:                  #Si c'est au pion 1 de jouer
            if self.compteur_X == 0:            #Si son compteur de pion est de 0
                return 1                            #On retourne 1
            else:
                return 0                            #Sinon on retourne 0

                                                    #idem pour le reste des pions en fonction de leur tour 
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
            

    #Methode test qui test si la partie est fini
    def test(self, tableau):
        #gère la fin ou non de la partie
        #A chaque test on remet les compteurs à 0
        self.compteur_X = 0
        self.compteur_0 = 0
        self.compteur_Y = 0
        self.compteur_U = 0
        self.compteur_case_vide = 0

        #On parcours le tableau
        for a in tableau:
            for b in a:
                if b == " X ":
                    self.compteur_X += 1

                elif b == " 0 ":
                    self.compteur_0 += 1            #Si in trouve un pion on rajoute 1 à son compteur

                elif b == " Y ":
                    self.compteur_Y += 1
                
                elif b == " U ":
                    self.compteur_U += 1
                else:
                    self.compteur_case_vide += 1

        #Si on à aucune case vide
        if self.compteur_case_vide == 0:
            compteurs = [self.compteur_0, self.compteur_X, self.compteur_U, self.compteur_Y] 
            maxi = max(compteurs)                                                                   #On regarde qui à le plus grand nombre de pions

            if self.compteur_0 == maxi:                                                         # Si 0 est le plus grand
                print("")
                print("")
                print("------------------------------------------- 0 à gagné ! ----------------------------------------------------")   #On affiche qu'il à gagner (Idem pour les autres joueurs)
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


        #Si il y encore des cases vides on vérifie qu'il n'y est pas qu'un seul pion dans quel cas il aurrait gagné

        elif self.compteur_0 == 0 and self.compteur_Y == 0 and self.compteur_U == 0 and self.compteur_X > 0:                        # Si il y à que des 0
            print("")
            print("")
            print("------------------------------------------- X à gagné ! ---------------------------------------------------")    #On affiche qu'il à gagné (Idem pour les autres)
            return 1                                                                                                                #On retourne 1 pour dire que la partie est fini                                   

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
            return 0  #Si aucun des cas n'est vérifié on retourne 0 pour dire que la partie continue
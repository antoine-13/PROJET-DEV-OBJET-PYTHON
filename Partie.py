###########################################################################################
#                                                                                         #
#                                                                                         #
#                                      Classe Partie:                                     #
#                                                                                         #
#                           gère le placement des pions, la                               #
#                           vérification des coups, la définition des joueurs             #
#                                                                                         #
#                                                                                         #
###########################################################################################


class Partie:

    #Initialisation des attributs de Partie 
    def __init__(self):
        self.tab = None 
        self.nbr_joueurs = 2
        self.tour = 1
        self.joueurs_du_tour = [1] * 1
        self.non_joueurs = [1] * 3

    #Méthode joueurs qui définie qui joue et qui ne joue pas en fonction du numéro du tour 
    def joueurs(self):
        type_pion = self.tour % self.nbr_joueurs
        
        if type_pion == 1:                      #Si c'est au tour de 1 de jouer on ajoute son symbole au tableau des joueurs et on ajoute les reste des joueurs au tableau des non joueurs
            self.joueurs_du_tour[0] = " X "
            self.non_joueurs[0] = " 0 "
            self.non_joueurs[1] = " Y "
            self.non_joueurs[2] = " U "
        elif type_pion == 0:                     #Si c'est au tour de 0 de jouer on ajoute son symbole au tableau des joueurs et on ajoute les reste des joueurs au tableau des non joueurs
            self.joueurs_du_tour[0] = " 0 "
            self.non_joueurs[0] = " X "
            self.non_joueurs[1] = " Y "
            self.non_joueurs[2] = " U "
           
        elif type_pion == 2:                     #Si c'est au tour de 2 de jouer on ajoute son symbole au tableau des joueurs et on ajoute les reste des joueurs au tableau des non joueurs
            self.joueurs_du_tour[0] = " Y "
            self.non_joueurs[0] = " 0 "
            self.non_joueurs[1] = " X "
            self.non_joueurs[2] = " U "
           
        elif type_pion == 3:                     #Si c'est au tour de 3 de jouer on ajoute son symbole au tableau des joueurs et on ajoute les reste des joueurs au tableau des non joueurs
            self.joueurs_du_tour[0] = " U "
            self.non_joueurs[0] = " 0 "
            self.non_joueurs[1] = " Y "
            self.non_joueurs[2] = " X "
            
    #Méthode qui demande à l'utilisateur ou il souhaite jouer
    def coup(self):
        coord = input("Ou souhaitez vous jouer ? (Saisir les coordonnées séparer pas un \';\') ").split(";",)
        return coord                                                                                                    #retourne dans un tableau les coordonées du choix
    
    #Méthode qui vérifie si la case est vide ou non 
    def validite_case(self,coup, tableau):
        #récupération des coordonées ou le joueur souhaite poser son pion 
        cl = int(coup[0])
        lg = int(coup[1])
       
        #vérification si la case est déjà prise par un autre pion
        if tableau[lg][cl] == " X " or tableau[lg][cl] == " 0 ":
            return 1                                                        #On retourne 1
        else:
            return 0                                                        #Sinon on retourne 0

    def validite_pos(self, coup, tableau):
        #récupération des coordonées ou le joueur souhaite poser son pion 
        cl = int(coup[0])
        lg = int(coup[1])
        possibilite = 0
        lg_add = [0, -1, +1]
        cl_add = [0, -1, +1]
        valid_dir_lg = []
        valid_dir_cl = []

        #On vérifie si dans toute les direction la case à coté contient un pion autre que celui qui joue
        #Si c'est le cas on continue dans la meme direction tant que le pion est différent de celui qui joue
        # Si on fini par croiser un pion correspondant à celui qui joue
        #On renvoi 1 pour dire que le coup est valable vue qu'il encadre bien d'autres pions 
        
        for a in lg_add:  
            for b in cl_add:                
                if tableau[lg + a][cl + b] in self.non_joueurs:
                    nlg = lg + a
                    ncl = cl + b
                    while tableau[nlg][ncl] in self.non_joueurs:
                        ncl += b
                        nlg += a
                        if tableau[nlg][ncl] in self.joueurs_du_tour:
                            valid_dir_lg.append(a)
                            valid_dir_cl.append(b)
                            possibilite += 1
                            
                        
        return possibilite, valid_dir_lg, valid_dir_cl
            
                                                            
        
    #Méthode ajout_pion qui ajoute un pion à la position souaitez par l'utilisateur
    def ajout_pion(self, coup, tableau):
            tableau[int(coup[1])][int(coup[0])] = self.joueurs_du_tour[0]           #ajoute la valeur du pion qui joue à l'emplacement souhaitez
            self.tab = tableau                                                      #Modifie le tableau final




    def inversement(self, tableau, coup, dir_lg, dir_cl):
        #récupération des coordonnées du coup
        cl = int(coup[0])
        lg = int(coup[1])

        


        #On vérifie si dans toute les direction la case à coté contient un pion autre que celui qui joue
        #Si c'est le cas on continue dans la meme direction tant que le pion est différent de celui qui joue
        # Si on fini par croiser un pion correspondant à celui qui joue
        #On renvoi 1 pour dire que le coup est valable vue qu'il encadre bien d'autres pions 
        for i in range (0, len(dir_cl)):
            nlg = lg + dir_lg[i]
            ncl = cl + dir_cl[i]
            while tableau[nlg][ncl] in self.non_joueurs:
                pion = [1] * 2
                pion[0] = ncl
                pion[1] = nlg
                self.ajout_pion(pion, tableau)
                possibilite, valid_dir_lg, valid_dir_cl = self.validite_pos(pion, tableau)
                self.inversement(tableau, pion, valid_dir_lg, valid_dir_cl)
                nlg += dir_lg[i]
                ncl += dir_cl[i]

            
                

    
        
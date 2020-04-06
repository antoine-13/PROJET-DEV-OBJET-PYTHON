class Partie:
    def __init__(self):
        super().__init__()

    
    def initialisation():
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

    def menu():
        valeur = int(input("Que souhaitez vous faire ? ( 1- poser un pion X; 2-poser un pion 0; 3- passer votre tour)"))
        return valeur

    def coup():
        coord = input("Ou souhaitez vous jouer ? (Saisir les coordonnées séparer pas un \';\') ").split(";",)
        return coord
    
    
    def validite(choix, tableau):
        if tableau[int(choix[0]) - 1][int(choix[1]) - 1] == " X " or tableau[int(choix[0]) - 1][int(choix[1]) - 1] == " 0 ":
            return 1

        else:
            return 0

    def ajout_pion(choix, tableau, pion):
        if pion == 1:
            tableau[int(choix[0]) - 1][int(choix[1]) - 1] = " X "
        if pion == 2:
             tableau[int(choix[0]) - 1][int(choix[1]) - 1] = " 0 "
        print(int(choix[0]), int(choix[1]))

        
class Partie:
    def __init__(self):
        super().__init__()

    def initialisation(self):
        #création du tableau
        cases = [] 
        i = 10
        j = 8

        for a in range(1,i):
            cases.append([" . "] * j)

        cases[3][3] = "0"
        cases[3][4] = "X"
        cases[4][3] = "0"
        cases[4][4] = "X"

        for a in cases:
            for b in a:
                print(b, end='')

            print("")

    def coup(self):
       return input("Ou souhaitez vous jouer ? (Saisir les coordonnées)")
    
    def validite(self, coup):
        #vérification de la validité du coup
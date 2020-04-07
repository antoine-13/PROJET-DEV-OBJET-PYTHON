class Plateau:
    def __init__(self):
        super().__init__()

    def affiche(self, tableau):
        #gère l'affichage du plateau 
        print("")
        print("   | 01 02 03 04 05 06 07 08") 
        print("_____________________________")
        i = 1
        for a in tableau:
            print("0", i, " ", end='|', sep='')
            for b in a:
                print(b, end='')

            print("")
            i += 1

        print("")


    def test(self, tableau):
        #gère la fin ou non de la partie
        compteur_X = 0
        compteur_0 = 0
        for a in tableau:
            for b in a:
                if b == " X ":
                    compteur_X = compteur_X + 1

                elif b == " 0 ":
                    compteur_0 = compteur_0 + 1

        if compteur_0 == 0 and compteur_X > 0:
            print("")
            print("")
            print("------------------------------------------- X à gagné ! ---------------------------------------------------")
            return 1

        elif compteur_0 > 0 and compteur_X == 0:
            print("")
            print("")
            print("------------------------------------------- 0 à gagné ! ----------------------------------------------------")
            return 1
            
        else:
            return 0
class Plateau:
    def __init__(self):
        super().__init__()
        
    
    def initialisation(self, dimenssion):
        #création du tableau
        cases = [] 
        i = int(dimenssion[1])
        j = int(dimenssion[0])

        for a in range(0,i+2):
            cases.append([" . "] * (j+2))

        cases[int(int(dimenssion[1])/2)][int(int(dimenssion[0])/2)] = " 0 "
        cases[int(int(dimenssion[1])/2)][int((int(dimenssion[0])/2) + 1)] = " X "
        cases[int((int(dimenssion[1])/2 + 1))][int(int(dimenssion[0])/2)] = " X "
        cases[int((int(dimenssion[1])/2) + 1)][int((int(dimenssion[0])/2) + 1)] = " 0 "

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
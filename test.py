cases = [] 
i = 10
j = 8

for a in range(1,i):
    cases.append([" . "] * j)

cases[3][3] = " X "
cases[3][4] = " 0 "
cases[4][3] = " 0 "
cases[4][4] = " X "

for a in cases:
    for b in a:
        print(b, end='')

    print("")
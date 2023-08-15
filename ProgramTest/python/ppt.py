import random
alter=True
cont_ply=0
cont_cons=0
while alter:
    print("\nPiedra, Papel ó Tijera\n========================\n")
    opc=str(input(" --> ")).upper()
    """ 1 - Piedra   2 - Papel   3 - Tijera """
    console=random.randint(1,3)
    if opc=="PIEDRA":
        if console==1:
            print("\nEmpate, la consola sacó Piedra")
        elif console==2:
            cont_cons+=1
            print("\nPierdes, la consola socó Papel")
        else:
            cont_ply+=1
            print("\nGanas, la consola sacó Tijera")
    elif opc=="PAPEL":
        if console==1:
            cont_ply+=1
            print("\nGanas, la consola sacó Piedra")
        elif console==2:
            print("\nEmpate, la consola socó Papel")
        else:
            cont_cons+=1
            print("\nPierdes, la consola sacó Tijera")
    elif opc=="TIJERA":
        if console==1:
            cont_cons+=1
            print("\nPierdes, la consola sacó Piedra")
        elif console==2:
            cont_ply+=1
            print("\nGanas, la consola socó Papel")
        else:
            print("\nEmpate, la consola sacó Tijera")
    else:
        print("\nValor no valido ó erroneo")
    print(f"Jugador: ",cont_ply,"\tConsola: ",cont_cons)
    if cont_ply==3:
        print("\nGana el jugador!!")
        alter=False
    elif cont_cons==3:
        print("\nGana la consola!!")
        alter=False
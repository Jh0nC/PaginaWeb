alter=True
cont_opc_1=cont_opc_2=cont_opc_3=cont_opc_4=cont_opc_5=cont_opc_6=cont_opc_7=vlr_pagar=ttl_vlr=0
while alter:
    print("\n\t\tLAVADO DE AUTOS\n=================================================="+"\n-Automovil:\t\tPrecios:\tOpción:\n---Pequeño\t\t$4000\t\t  1\n---Mediano\t\t$5000\t\t  2\n---De Lujo\t\t$6000\t\t  3\n\nCampero:\n---Sencillo\t\t$5000\t\t  4\n---De Lujo\t\t$8000\t\t  5\n\nCamioneta:\n---Cabina Sencilla\t$6000\t\t  6\n---Doble Cabina\t\t$8000\t\t  7\n\nREGLA DE NEGOCIO: Si su auto tiene\n8 o más años de antigüedad, el costo\nse incrementa en un 20%.\n\nSalir y ver recuento ---> 9\n")
    opc=int(input(" ---> "))
    if opc == 9:
        print(f"\nConteo: \tTotal dinero ingresado: $",ttl_vlr,"\n==========================================\nAutomóvil Pequeño\t\t--> ",cont_opc_1,"\nAutomóvil Mediano\t\t--> ",cont_opc_2,"\nAutomóvil de Lujo\t\t--> ",cont_opc_3,"\nCampero Sencillo\t\t--> ",cont_opc_4,"\nCampero de Lujo\t\t\t--> ",cont_opc_5,"\nCamioneta de cabina sencilla\t--> ",cont_opc_6,"\nCamioneta de doble cabina\t--> ",cont_opc_7,"\n\nHasta luego!!\n")
        alter=False
    else:
        antigd=int(input("Antigüedad del vehiculo: "))
        if opc == 1:
            cont_opc_1+=1
            vlr_pagar=4000
        elif opc == 2:
            cont_opc_2+=1
            vlr_pagar=5000
        elif opc == 3:
            cont_opc_3+=1
            vlr_pagar=6000
        elif opc == 4:
            cont_opc_4+=1
            vlr_pagar=5000
        elif opc == 5:
            cont_opc_5+=1
            vlr_pagar=8000
        elif opc == 6:
            cont_opc_6+=1
            vlr_pagar=6000
        elif opc == 7:
            cont_opc_7+=1
            vlr_pagar=8000
        else:
            print("\nNo se reconoce el valor como opción!!")
        if antigd >= 8:
            vlr_pagar=vlr_pagar+vlr_pagar*0.2
        print(f"\nEl valor a pagar por el servicio es: ",vlr_pagar)
    ttl_vlr+=vlr_pagar
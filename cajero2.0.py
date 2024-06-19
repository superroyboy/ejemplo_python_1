#cajero automatico 

import os 

os.system("cls")



def cuenta_corriente():

    #-------------------------------------------------------------

    print("elija opcion----")

    print("1...consulta de saldo ")

    print("2...Giro de saldo ")

    print("3...Salir\n")

    try:

        operacion_cc=int(input(" "))

    except:

        operacion_cc=3

    if operacion_cc ==1:

        print("desea su informacion por pantalla??")

        verccpantalla=input("si/no\n")

        if verccpantalla == "si":

            print(" NO HAY PLATA")

    elif operacion_cc ==2:

        try:

            monto_giro=int(input("ingrese monto --$\n:"))

        except:

            monto_giro=0

        print("retira tus chauchas ")

    else:

        print("adios")

    #fin menu cuenta corriente 



def tarjeta_credito():

    print("elija opcion----")

        

    print("1...Avance en cuotas  ")

    print("2...Avance en efectivo ")

    print("3...consulta de saldo")

    print("4...pago estado de cuenta ")

    print("5...Salir\n")

    try:

        operacion_tjc=int(input(" "))

    except:

        operacion_tjc=4

    if operacion_tjc ==1:

        print("desea un avance en cuotas ")

        vertjpantalla=input("si/no\n")

        if vertjpantalla == "si":

            print(" ingrese avance y num de cuotas ")

        elif vertjpantalla =="no":

            print("opcion invalida ")

    if operacion_tjc==2:

        print("desea un avance en efectivo?")

        avctjc=input("si/no")

        if avctjc=="si":

            print("indique monto y cuotas")

        elif avctjc=="no":

            print("opcion invalida ")

    if operacion_tjc==3:

        print("desea ver su informacion en pantalla ?")

        saldotjx=input("si/no")

        if saldotjx == "si" :

            print("tiene mas deuda que vida")

        elif saldotjx == "no":

            print("impromiendo su informacion mediante un comprobante ")    

    if operacion_tjc==4:

        print("desea pagar su cuenta ??")

        pagotjc=input("si/no")

        if pagotjc=="si":

            print("indique monto a pagar...")

        elif pagotjc =="no":

            print("page sus deudas mmhuevo ")

    elif operacion_tjc ==5:

        print("adios se humano ")

#menu tajeta de credito 





def cuenta_rut():

    print("elija opcion----")

    print("1...giro rapido ")

    print("2...consulta de saldo ")

    print("3...salir ")

    try:

        operacion_cntarut=int(input(" "))

    except:

        operacion_cntarut=3

    if operacion_cntarut ==1:

        print("solo giros rapidos de multiplos de 10 ,desea continuar ?")

        girocntarut=input("si/no")

        if girocntarut=="si":

            print("indique monto que desea girar")

        elif girocntarut=="no":

            print("vuelva al menu principal o vuelva a intentar ")

    if operacion_cntarut ==2:

        print("desea consultar el saldo de sus productos??")

        saldocntarut=input("si/no")

        if saldocntarut=="si":

            print("su saldo es $$$$")

        elif saldocntarut=="no":

            print("vuelva a intentar o volver al menu")

    if operacion_cntarut==3 :

        print("volviendo al menu")

#fin cuenta rut 



def cuenta_ahorro():

    print("elija opcion----")

    print("1...giro rapido ")

    print("2...consulta de saldo ")

    print("3...salir ")

    try:

        operacion_cntaahorro=int(input(" "))

    except:

        operacion_cntaahorro=3

        if operacion_cntaahorro==1:

            print("desea hacer un giro rapido ??")

            girocnta_ahorro=input("si/no")

            if girocnta_ahorro=="si":

                print("ingrese monto que desea girar")

            elif girocnta_ahorro =="no":

                print("vuelva a intentar o regrese al menu")

        if operacion_cntaahorro==2:

            print("desea consultar su saldo?")

            consult_ahorro=input("si/no")

            if consult_ahorro=="si":

                print("su saldo es $$$$")

            elif consult_ahorro =="no":

                print("vuelva a intentar o regrese al menu")

        if operacion_cntaahorro ==3:

            print("hasta luego :) ")

#fin cuenta rut 

    


tarjeta = None
while not tarjeta :
    tarjeta=input("ingrese su tarjeta ")
    if len(tarjeta) == 0 :
        print("tarjeta invalida mmhuevo")


clave = '0'
while len(clave) != 4 :
    clave=input("ingrese su clave ")
    if len(clave) != 4:
        print("clave invalida ")




print("escoger tipo de cuenta ") 

while True:

    print("1) cuenta corriente")

    print("2) chequera electronica")

    print("3) tarjeta de credito")

    print("4) cuenta vista-rut")

    print("5) cuenta ahorro")

    print("6) salir")

    

    try:

        op=int(input("elije una"))

    except:

        op=0 #valor por defecto 

        

    if op==1:

        print("cuenta corriente ")

        cuenta_corriente()

        break

    elif op==2:

        print(" chequera electronica ")

        print("en construccion")

        

    elif op==3:

        print("tarjeta de credito ")

        tarjeta_credito() 

    elif op==4:

        print("cuenta vista-rut ")

        cuenta_rut()

    elif op==5:

            print("cuenta ahorro ")   

           

    elif op==6:

        print("salir ")

        break

    else:

         print("opcion no valida ")

#fin del while        

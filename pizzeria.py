print("Bienvenido a Pizzeria Don Giovanni")

nombre = input("¿Cuál es tu nombre? ")

total  = 0
lleva_pizza = False
lleva_palitos = False
lleva_bebida = False

while True :
    
    print("Nuestros productos:")
    print("1.- Pizza")
    print("2.- Palitos de Ajo")
    print("3.- Bebida")
    print("4.- Salir")

    try :
        op = int(input("¿Que prefieres para comenzar? ") )
    except :
        op = 0 # valor que es invalido

    if op == 1 :
        
        print("Nuestras Pizzas :")
        print("1.- Pepperoni")
        print("2.- Margarita(Veggie)")
        print("3.- Cuatro Quesos")
        
        try :
            pizza = int(input("¿Que pizza te gustaria hoy? ") )
        except :
            pizza = 0 # valor que es invalido

        if pizza < 1 or pizza > 3 :
            print("elección inválida")
        else:
            
            lleva_pizza = True
            
            if pizza == 1 :
                print("pepperoni")
                total = total + 5000
            elif pizza == 2 :
                print("margarita")
                total = total + 5000
            elif pizza == 3 :
                print("4 quesos")
                total = total + 6000

            while True :
                print("Nuestros Tamaños :")
                print("1.- Individual")
                print("2.- Mediano")
                print("3.- Familiar")
                
                try :
                    tamanio = int(input("¿Cuanta hambre tienes? ") )
                except :
                    tamanio = 0 # valor que es invalido

                if tamanio == 2 :
                    if pizza == 1 or pizza == 2 :
                        total = total + 1500
                    else :
                        total = total + 2000
                    break    
                elif tamanio == 3 :
                    if pizza == 1 or pizza == 2 :
                        total = total + 3000
                    else :
                        total = total + 4000
                    break
                else :
                    print("no es valido")
                    
    elif op == 2 :
        print("Palitos de Ajo")
        lleva_palitos = True
        total = total + 2000
        
    elif op == 3 :
        print("Bebidas")
        print("1.- Limón Soda")
        print("2.- Pepsi")
        print("3.- Kem Piña")
        print("4.- Bilz")
        print("5.- Pap")
        print("6.- Canada Dry Ginger Ale")

        try :
            bebida = int(input("¿Que bebida? ") )
        except :
            bebida = 0 # valor que es invalido
        
        if bebida < 1 or bebida > 6 :
            print("no tenemos de esa")
        else :
            lleva_bebida = True
            if bebida == 2 :
                total = total + 2500
            else :
                total = total + 2000
                
    elif op == 4 :
        print ("Salir")
        break
    else :
        print("opcion no valida")
    
# end while

if lleva_palitos and not lleva_pizza :
    total = total + 1000
    
print("total a pagar", total)
print("gracias por preferirnos")

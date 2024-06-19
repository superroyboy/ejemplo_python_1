#Delivery de sushi

import time, os
os.system("cls")

#menu de sushi
valor_roll = [0,4500,5000,5200,4800]
nombre_roll =["", "Pikachu Roll","Otaku Roll","Pulpo Venenoso Roll","Anguila Eléctrica Roll"]

maximo = len(valor_roll)

#descuento
codigo_actual = "soyotaku"
descuento_x_codigo = 0.1 #10%

linea ="******************************"

cantidad_de_pedidos = 0
monto_total_vendido = 0

total_roll = [0,0,0,0,0]

nombre_producto_mas_popular=""
total_producto_mas_popular=0

while True:

    #cada nuevo pedido
    cantidad = 0
    subtotal = 0
    total = 0
    descuento = 0
    
    cant_roll = [0,0,0,0,0]    
    while True:

        print("Bienvenido a Otaku Sushirolls")
        print("\tMenu")
        for i in range(1,maximo):
            print(f"{i}. {nombre_roll[i]} ${valor_roll[i]} ")
        print(f"{maximo}. Salir")
        
        try:
            opcion = int(input("Seleccione el sushi que desea agregar a su pedido\n"))
        except:
            opcion = 0
        # end try

        if opcion < 1 or opcion > maximo :

            print(f"Opcion no valida, por favor seleccione del 1 al {maximo}")

        elif opcion >= 1 and opcion < maximo : 

            print(f"{nombre_roll[opcion]} ha sido agregado a su pedido")
            cant_roll[opcion] = cant_roll[opcion] + 1
            cantidad = cantidad + 1
            subtotal = subtotal + valor_roll[opcion]
            print("Subtotal:",subtotal)

        else : # maximo :salir

            codigo_descto = input("ingrese codigo de descuento : ")
            if codigo_descto == codigo_actual :
                descuento = descuento_x_codigo
            else :
                descuento = 0
            #end if
            monto_descontado = int(round(subtotal * descuento,0))
            total = subtotal - monto_descontado

            print(linea)
            print(f'TOTAL PRODUCTOS : { cantidad }') 
            print(linea)
            for i in range(1,maximo):
                print (f"{nombre_roll[i]} : {cant_roll[i]}")
            print(linea)
            print(f"Subtotal : ${subtotal}")
            print(f"Descuento por código : ${monto_descontado}")
            print(f"Total : ${total}")
            print(linea)
            print("Gracias por visitarnos")
            print(linea)

            cantidad_de_pedidos = cantidad_de_pedidos + 1
            monto_total_vendido = monto_total_vendido +  total 
            for i in range(1,maximo):
                total_roll[i] = total_roll[i] + cant_roll[i]
                
            break
            
        #end if
    #end while, fin de un pedido

    try:
        continuar = int(input("Desea realizar otro pedido?\n1.- Si (opcion por defecto)\n2.- No (salir del programa)\n> "))
    except:
        continuar = 1
    #end try
    
    if continuar != 1 :
        break
    #end if

#end while      

total_producto_mas_popular = total_roll[0]
nombre_producto_mas_popular=nombre_roll[0]

for i in range(1,maximo):
    
    if total_roll[i] > total_producto_mas_popular :
        total_producto_mas_popular = total_roll[i]
        nombre_producto_mas_popular=nombre_roll[i]
    #end if

print("\nResumen")     
print(f"Pedidos Realizados : {cantidad_de_pedidos}")
print(f"Total Vendido      : $ {monto_total_vendido}")
print(f"Rollo más popular  : {nombre_producto_mas_popular} ({total_producto_mas_popular})")

print("\nSayonara!")        


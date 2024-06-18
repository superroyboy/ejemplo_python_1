'''
La empresa de reparto de cilindros de gas a domicilio “Gaxplosive”, necesita desarrollar un sistema que permita registrar los pedidos antes de enviar su camión repartidos. Para el funcionamiento del sistema se requiere las siguientes funcionalidades
1.	Registrar pedido
2.	Listar los todos los pedidos
3.	Imprimir hoja de ruta
4.	Salir del programa
'''

# declarar variables

# definir funciones
def registra_pedido():
    print('eligio opcion 1')
#

def listar_pedido():
    print('eligio opcion 2')
#

def imprime_hoja_de_ruta():
    print('eligio opcion 3')
#


# programa principal

while True:
    # mostrar opciones de menu
    print("""1.	Registrar pedido
2.	Listar los todos los pedidos
3.	Imprimir hoja de ruta
4.	Salir del programa""")
    
    # ingrese una opcion
    try:
        op = int(input('ingrese opcion'))
    except:
        op = 0
    
    # validar opcion
    if op < 1 or op > 4 :
        print('opcion invalida')
    # ejecutar accion
    elif op == 1 :
        registra_pedido()
    elif op == 2 :
        listar_pedido()
    elif op == 3 :
        imprime_hoja_de_ruta()
    else :
        break 
#
print('bye bye')


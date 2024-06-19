ropa = []  # coleccion que inicia vacia

ropa.append('ropa interior')
ropa.append('pantalon')
ropa.append('calcetin')
ropa.append('zapatos')
ropa.append('polera')
ropa.append('chaleco')

print(ropa)  # el contenido, la lista completa
print( len(ropa) ) # la cantidad de elementos
#print( ropa[0] ) # un elemento en particular, en la posicion [ X ]

'''
print('---')
# 0, ... 7
for pos in range( len(ropa) ) :  
    print ( pos, '->', ropa[pos] )
# fin for

print('---')

# 7, ... 0
posicion = len(ropa) - 1  
while posicion >= 0  :
    print ( posicion, '->', ropa[posicion] )
    posicion = posicion - 1 
# fin while
'''

print('---')
for prenda in ropa  :  
    print ( prenda )







'''
for pos in range(1,10,1) :  # ranges( desde, hasta-1, aumento )
    print(pos, end='\t')

print()

for pos in range(1,10,2) :  # ranges( desde, hasta-1, aumento )
    print(pos, end='\t')

    
print()

for pos in range(1,6) :  # ranges( desde, hasta-1, aumento x defecto es 1 en 1 )
    print(pos, end='\t')

print()

for pos in range(8) :  # ranges( desde x defecto es 0, hasta-1, aumento x defecto es 1 en 1 )
    print(pos, end='\t')
'''





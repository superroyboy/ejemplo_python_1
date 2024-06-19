#crear archivo, w es permiso de escritura
#Las comillas al inicio y 3 al final del texto representan un texto
#con saltos de línea

datos = """Este es un archivo de texto simple que no tiene 
ningún formato en particular, lo podemos utilizar
para guardar todo tipo de texto. 
"""
with open('archivo.txt', 'w') as archivo:
    archivo.write(datos)

#---
    
datos = "Pikachu Roll,4500\nOtaku Roll,5000\nPulpo Venenoso Roll, 5200\nAnguila Electrica Roll, 4800\n"
with open('datos.txt', 'w') as archivo:
    archivo.write(datos)

# Opción 1
# Permisos: 'r' (lectura), 'w' (escritura), 'r+' (lectura/escritura)
archivo = open('datos.txt', 'r')
contenido = archivo.read()
print(contenido)
archivo.close()

# Opción 2
# Usando el contexto 'with', el archivo se cierra automáticamente al salir del bloque 'with'
with open('datos.txt', 'r') as archivo:
    contenido = archivo.read()
print(contenido)



import csv
# permiso w es escritura

with open('nuevo_archivo.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    # Escribir una fila en el archivo CSV
    escritor_csv.writerow(['Nombre', 'Edad', 'Comuna'])
    # Escribir múltiples filas en el archivo CSV
    escritor_csv.writerows([
    ['Esteban', 25, 'Santiago'],
    ['María', 30, 'Valparaíso'],
    ['Carlos', 22, 'Osorno'],
    ['Sigrid', 25, 'Santiago'],
    ['Daniela', 30, 'La Cisterna'],
    ['Aylen', 22, 'La florida']
    ])

# Leer Archivos CSV

import csv
# Sintaxis: open('nombre_del_archivo.csv', 'modo', newline='')

# Modo común: 'r' (lectura)
with open('nuevo_archivo.csv', 'r', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)


import json

# Datos JSON
datos = {
"nombre": "Esteban",
"edad": 25,
"comuna": "Santiago",
"estudios": ["colegio Arturo Prat", "liceo el bosque",
"Duoc UC", "Diplomado Duoc UC"]
}

# Abre el archivo, w es escritura
with open('archivo.json', 'w') as archivo:
    json.dump(datos, archivo)


import json

# Abrir archivo, r es permiso de lectura
with open('archivo.json', 'r') as archivo:
    datos_leidos = json.load(archivo)
print(datos_leidos)



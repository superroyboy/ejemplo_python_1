# Importamos las bibliotecas
import os
import csv
import json
os.system('cls')

with open('Archivo.csv', 'w', newline='') as archivo:
    escribir = csv.writer(archivo)
    escribir.writerow(['Nombre','Asignatura','Nota'])

# Crea un programa que tome los datos de un alumno validando que no sea nombre vacio
pregunta = 's'
while pregunta == 's':
    alumno = ''
    while alumno == '':
        alumno = input('Ingresa nombre de alumno: ').strip()
        if alumno == '':
            print('Nombre no valido')
        else:
# Preguntar cuantas materias esta cursando y en base a eso le pregunte los nombres de las materias
            while True:
                try:
                    asignatura = int(input('Cuantas asignaturas está cursando: '))
                except:
                    asignatura = 0
                if asignatura <1 or asignatura >7:
                    print('Valor no valido, ingrese solo números y valores entre 1 y 7')
                else: 
                    list_asignaturas = []
                    for i in range(asignatura):
                        while True:
                            nombre_asignatura = input(f'Ingresa el nombre de la asignatura {i+1}: ').strip()
                            if nombre_asignatura == '':
                                print('Asignatura no puede ir en blanco')
                            else:
                                list_asignaturas.append(nombre_asignatura)
                                break
                    break
    # Luego le pregunte las notas y finalemnte guardar en un archivo CSV con las cabeceras de: Nombre,Materia,Nota

            list_notas = []
            for n in list_asignaturas:
                while True:
                    try:
                        notas = float(input(f'Ingrese nota para {n}: '))
                    except:
                        notas = 0
                    if notas <1 or notas >7:
                        print('Formato de notas no valido, favor seleecionar una nota entre 1 y 7')
                    else:
                        list_notas.append(notas)
                        break
        with open('Archivo.csv', 'a', newline='') as archivo_csv:
            escribir = csv.writer(archivo_csv)
            for i in range(len(list_asignaturas)):
                escribir.writerow([f'{alumno}',f'{list_asignaturas[i]}',f'{list_notas[i]}'])
    pregunta = input('Desea ingresar otro alumno? s/n ').lower()
print('A finalizado el programa')

# luego consultar el archivo y calcular el promedio de notas de cada alumno
# exportar las notas aprobadas a un Json y las desaprobadas a otro Json
# Validaciones: No se aceptan nombres vacios ni notas fuera de rango ni numeros de materia = 0
# El programa debe repetirse N veces 









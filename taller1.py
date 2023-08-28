import pandas as pd
#import numpy as pd
#import matplot as pd
from datetime import datetime

# Cargar los conjuntos de datos desde archivos Excel (reemplaza 'archivo1.xlsx' y 'archivo2.xlsx' con los nombres de tus archivos)
data1 = pd.read_excel('DatosP01.xlsx')
data2 = pd.read_excel('DatosP02.xlsx')

# Mostrar las primeras filas de cada DataFrame para verificar la carga exitosa
print("Data1:")
print(data1.head())
print("\nData2:")
print(data2.head())

# Especifica las columnas clave para realizar la unión
key_columns = ['Id']

# Realiza la unión de los DataFrames basada en las columnas clave
merged_data = pd.merge(data1, data2, on=key_columns, how='inner')

# Reemplazar valores incoherentes en la columna 'Sexo'
data1['Sexo'] = data1['Sexo'].replace(['Femenino', 'Masculino', 'Mujer'], ['F', 'M', 'F'])

# Fusionar los conjuntos de datos usando la columna 'Id' como clave
data = pd.merge(data1, data2, on='Id')

# Calcular el promedio de calificaciones
data['Promedio'] = (data['Sistemas'] + data['Matematicas'] + data['Ingles'] + data['Comunicación']) / 4

# Filtrar aprendices aprobados y no aprobados
aprobados = data[data['Promedio'] > 3.5]
no_aprobados = data[data['Promedio'] <= 3.5]

# Obtener características de aprendices aprobados y no aprobados
data['FechaNacimiento'] = pd.to_datetime(data['FechaNacimiento'], format='%d/%m/%Y')

# Calcula las edades a partir de la fecha de nacimiento
hoy = datetime.now()
data['Edad'] = hoy.year - data['FechaNacimiento'].dt.year

# Filtra los aprendices aprobados (supongamos que 'Promedio' es la columna con el promedio de calificaciones)
aprobados = data[data['Promedio'] > 3.5]
noaprobados = data[data['Promedio'] <= 3.5]

# Calcula el promedio de edades de los aprendices aprobados
promedio_edad_aprobados = aprobados['Edad'].mean()
promedio_edad_noaprobados = noaprobados['Edad'].mean()


caracteristicas_aprobados = aprobados[['Id', 'Nombre', 'Sexo', 'Estrato', 'Trabaja', 'Enfermedad', 'Ubicacion', 'Promedio']]
caracteristicas_no_aprobados = no_aprobados[['Id', 'Nombre', 'Sexo', 'Estrato', 'Trabaja', 'Enfermedad', 'Ubicacion', 'Promedio']]

# Calcular el promedio de edad de los aprendices aprobados y no aprobados
#promedio_edad_aprobados = caracteristicas_aprobados['Edad'].mean()
#promedio_edad_no_aprobados = caracteristicas_no_aprobados['Edad'].mean()

# Imprimir resultados
print("Características de los aprendices aprobados:")
print(promedio_edad_aprobados)
print("\nCaracterísticas de los aprendices no aprobados:")
print(promedio_edad_noaprobados)
print("\nPromedio de edad de los aprendices aprobados:", promedio_edad_aprobados)
print("Promedio de edad de los aprendices no aprobados:", promedio_edad_noaprobados)

# Reemplazar las comas por puntos en las columnas numéricas
columnas_numericas = ['Asistencia', 'Entregas_Completas', 'Sistemas', 'Matematicas', 'Ingles', 'Comunicación']
data2[columnas_numericas] = data2[columnas_numericas].apply(lambda x: x.str.replace(',', '.'))

# Convertir las columnas numéricas al tipo float
data2[columnas_numericas] = data2[columnas_numericas].astype(float)

# Calcular el promedio ponderado para data2
data2['Promedio'] = (data2['Sistemas'] + data2['Matematicas'] + data2['Ingles'] + data2['Comunicación']) / 4

# Agregar una columna para indicar si el aprendiz aprobó o no en data2
data2['Aprobado'] = data2['Promedio'] > 3.5

# Filtrar aprendices que usaron el LMS en data2
usaron_lms_data2 = data2[data2['Uso_LMS'] == 'Si']

# Obtener características de aprendices que aprueban y no aprueban en data2
aprobados_data2 = usaron_lms_data2[usaron_lms_data2['Aprobado']]
no_aprobados_data2 = usaron_lms_data2[~usaron_lms_data2['Aprobado']]


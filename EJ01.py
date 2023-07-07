import pandas as pd
#====================================================
# Crea una Serie de los numeros 10, 20 and 10.
numeros = pd.Series([10, 20, 10])
#========================================================================
# Crea una Serie con tres objetos: 'rojo', 'verde', 'azul'
colores=pd.Series(['rojo','verde','azul'])
#========================================================================
# Crea un dataframe vacío llamado 'df'
df = pd.DataFrame()
#========================================================================
# Crea una nueva columna en el dataframe, y asignale la primera serie que has creado
df['columna_1']= numeros
df['columna_2']= colores
print(df)
#========================================================================
#Lee el archivo llamado 'avengers.csv" y crea un DataFrame, llamado 'avengers'. 
avengers = pd.read_csv(r'C:\Users\Pc\Desktop\PYTHON\PC05\avengers.csv', sep=',')
# Muestra las primeras 5 filas del DataFrame.
print(avengers.head())
# Muestra las primeras 10 filas del DataFrame.
print(avengers.head(10))
# Muestra las últimas 5 filas del DataFrame.
print(avengers.tail(5),'\n')
# Muestra el tamaño del DataFrame
(Filas,Columnas)=avengers.shape
print(f'El tamaño del DataFrame "Avengers":\nEl numero de Filas: {Filas}\nEl numero de columnas: {Columnas}\n')
# Muestra los data types del dataframe
print('Tipo de datos del DataFrame "Avengers"\n',avengers.dtypes,'\n')
# Cambia el indice a la columna "fecha_inicio"
avengers.set_index('fecha_inicio', inplace=True)
print(avengers.head(),'\n')
# Ordena el índice de forma descendiente
avengers.sort_index(ascending=False, inplace=True)
print(avengers.head(),'\n')
# Resetea el índice
avengers.reset_index(drop=True, inplace=True)
print(avengers.head(),'\n')
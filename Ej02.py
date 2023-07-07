import pandas as pd
import matplotlib.pyplot as plt
airbnb = pd.read_csv(r'C:\Users\Pc\Desktop\PYTHON\PC05\airbnb.csv', sep=',')
print(airbnb.head(),'\n','\nTipo de datos del DataFrame "Airbnbs":',airbnb.dtypes,'\n')
#==================================================================================================================
#CASO 1
#Alicia va a ir a Lisboa durante una semana con su marido y sus 2 hijos. Están buscando un apartamento 
# con habitaciones separadas para los padres y los hijos. No les importa donde alojarse o el precio, 
# simplemente quieren tener una experiencia agradable. Esto significa que solo aceptan lugares con más 
# de 10 críticas con una puntuación mayor de 4. Cuando seleccionemos habitaciones para Alicia, tenemos 
# que asegurarnos de ordenar las habitaciones de mejor a peor puntuación. Para aquellas habitaciones que 
#tienen la misma puntuación, debemos mostrar antes aquellas con más críticas. Debemos darle 3 alternativas.
#==================================================================================================================
filtro = (airbnb['reviews'] > 10) & (airbnb['overall_satisfaction'] > 4) & (airbnb['bedrooms'] == 2)
filas_filtradas = airbnb[filtro]
# Ordenar las filas filtradas por overall_satisfaction y reviews
filas_ordenadas = filas_filtradas.sort_values(by=['overall_satisfaction', 'reviews'], ascending=[False, False])
# Mostrar las filas ordenadas
print(filas_ordenadas.head(3),'\n')
#==================================================================================================================
#CASO 2
#Roberto es un casero que tiene una casa en Airbnb. De vez en cuando nos llama preguntando sobre cuales son las 
# críticas de su alojamiento. Hoy está particularmente enfadado, ya que su hermana Clara ha puesto una casa en 
# Airbnb y Roberto quiere asegurarse de que su casa tiene más críticas que las de Clara. Tenemos que crear un 
# dataframe con las propiedades de ambos. Las id de las casas de Roberto y Clara son 97503 y 90387  respectivamente. 
# Finalmente guardamos este dataframe como excel llamado "roberto.xlsx
#==================================================================================================================
filas_Roberto = airbnb[airbnb['room_id'].isin([97503, 90387])]
print(filas_Roberto,'\n')
#Guardamos en un archivo XLSX
roberto='roberto.xlsx'
filas_Roberto.to_excel(roberto, index=False)
print(f"Se ha guardado el resultado en el archivo Excel '{roberto}'.",'\n')
#==================================================================================================================
#CASO 3
#Diana va a Lisboa a pasar 3 noches y quiere conocer a gente nueva. Tiene un presupuesto de 50€ para su alojamiento. 
# Debemos buscarle las 10 propiedades más baratas, dandole preferencia a aquellas que sean habitaciones compartidas 
# *(room_type == Shared room)*, y para aquellas viviendas compartidas debemos elegir aquellas con mejor puntuación.
#==================================================================================================================
condicion = (airbnb['room_type'] == 'Shared room') & (airbnb['price'] < 50)
Filas_Condicionadas=airbnb[condicion]
#Luego ordenamos de mayor a menor
Satisfaccion=Filas_Condicionadas.sort_values(by=['overall_satisfaction', 'reviews'], ascending=[False, False])
print('Las habitaciones Disponibles para Diana seran:',Satisfaccion.head(10))
#==================================================================================================================
#Realizar un gráfico circular, de la cantidad de tipo de habitaciones `room_type`  
Numero_habitaciones = airbnb['room_type'].value_counts()
# Generamos el gráfico circular
plt.figure(figsize=(8, 8))
plt.pie(Numero_habitaciones, labels=None, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Tipos de Habitaciones', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.legend(Numero_habitaciones.index, loc='best')
plt.show()
#==================================================================================================================






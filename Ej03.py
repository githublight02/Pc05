import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from openpyxl import Workbook
import smtplib

#===================================================================================================
# Leemos el Dataframe
candidates = pd.read_csv(r'C:\Users\Pc\Desktop\PYTHON\PC05\candidates.csv', sep=';')
# Guardar el DataFrame en la base de datos
Base_Datos = sqlite3.connect('mi_base_de_datos.db')
candidates.to_sql('Tabla_Datos', Base_Datos, if_exists='replace', index=False)
#Lectura de DB
with sqlite3.connect(r'C:\Users\Pc\Desktop\PYTHON\PC05\mi_base_de_datos.db') as conn:
    query='Select* from Tabla_Datos'
    df=pd.read_sql_query(query,conn)
#===================================================================================================
# Procesamiento de Informacion
#separamos en diferentes hojas de  excel por country
with pd.ExcelWriter('Country.xlsx') as writer:       
    for country in df['Country'].unique():       
        country_df = df[df['Country'] == country]        
        country_df.to_excel(writer, sheet_name=country, index=False)

print("Se han separado los candidatos en diferentes hojas de Excel según sus Continenetes.\n")
#===================================================================================================
#Ordenamos por mayor puntaje de programacion y entrevista

mayor_code_challenge_score = df[df['Code Challenge Score'] >= 9]
mayor_technical_interview_score = df[df['Technical Interview Score'] >= 9]
intermedio_code_challenge_score = df[(df['Code Challenge Score'] >= 5) & (df['Code Challenge Score'] < 9)]
intermedio_technical_interview_score = df[(df['Technical Interview Score'] >= 5) & (df['Technical Interview Score'] < 9)]
peores_code_challenge_score = df[df['Code Challenge Score'] < 5]
peores_technical_interview_score = df[df['Technical Interview Score'] < 5]
excel_filename = 'candidatos_scores.xlsx'
writer = pd.ExcelWriter(excel_filename, engine='openpyxl')
mayor_code_challenge_score.to_excel(writer, sheet_name='Mayores Code Challenge Score', index=False)
mayor_technical_interview_score.to_excel(writer, sheet_name='Mayores Technical Interview Score', index=False)
intermedio_code_challenge_score.to_excel(writer, sheet_name='Intermedios Code Challenge Score', index=False)
intermedio_technical_interview_score.to_excel(writer, sheet_name='Intermedios Technical Interview Score', index=False)
peores_code_challenge_score.to_excel(writer, sheet_name='Peores Code Challenge Score', index=False)
peores_technical_interview_score.to_excel(writer, sheet_name='Peores Technical Interview Score', index=False)

writer.save()
writer.close()

print("Se han separado los candidatos en diferentes hojas de Excel según sus puntajes.\n")

#===================================================================================================
#Grafico en porcentaje de timpos de Technology y tipos de Seniority
technology_percentage = df['Technology'].value_counts(normalize=True) * 100
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].pie(technology_percentage, labels=technology_percentage.index, autopct='%1.1f%%')
axs[0].set_title('Porcentaje de Tipos de Technology')
seniority_percentage = df['Seniority'].value_counts(normalize=True) * 100
axs[1].pie(seniority_percentage, labels=seniority_percentage.index, autopct='%1.1f%%')
axs[1].set_title('Porcentaje de Niveles de Seniority')
plt.tight_layout()
plt.show()
#===================================================================================================
#Envio de Correo
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
# Datos del remitente
remitente = "espadachinoscuro27@gmail.com"
password = open(r'C:\Users\Pc\Desktop\PYTHON\PC05\password.txt' ).read().strip()

# Datos del destinatario
destinatario = "espadachinoscuro27@gmail.com"

# Crear el mensaje
mensaje = MIMEMultipart()
mensaje["From"] = remitente
mensaje["To"] = destinatario
mensaje["Subject"] = "Envio de archivo Candidates.csv"

# Adjuntar archivo
archivo_adjunto = r'C:\Users\Pc\Desktop\PYTHON\PC05\candidates.csv'  # Ruta y nombre del archivo a adjuntar

# Leer el archivo en modo binario
with open(archivo_adjunto, "rb") as archivo:
    # Crear el objeto MIME base
    adjunto = MIMEBase("application", "octet-stream")
    # Cargar el contenido del archivo
    adjunto.set_payload(archivo.read())

# Codificar el archivo adjunto en base64
encoders.encode_base64(adjunto)

# Establecer las cabeceras del archivo adjunto
adjunto.add_header("Content-Disposition", f"attachment; filename= {archivo_adjunto}")

# Adjuntar el archivo al mensaje
mensaje.attach(adjunto)

# Configurar el servidor SMTP de Gmail
smtp_server = "smtp-mail.outlook.com"
smtp_port = 587
with smtplib.SMTP(smtp_server, smtp_port) as server:
    
    server.starttls()
    server.login(remitente, password)

    # Enviar el correo electrónico
    server.send_message(mensaje)

print('Se ha enviado la base.csv al correo seleccionado')
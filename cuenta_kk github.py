import pandas as pd 

#Below needed the poop-file name to your .txt import whatsapp file
poop_file = "chat_cacas.txt"

fichero = open(poop_file, "r", encoding="UTF-8")
lineas = fichero.readlines()
fichero.close()

datos_caca = []

for numero_linea in range(0, len(lineas)):
    linea_analizando = lineas[numero_linea].split(":")
    
    try:
        es_caca = linea_analizando[2][1]
        
        if es_caca == "💩":
            quien_hizo_caca = linea_analizando[1][5:]
            fecha_hora = linea_analizando[0].split(",")
            fecha_caca = fecha_hora[0]
            hora_caca = fecha_hora[1]
            minutos_caca = linea_analizando[1][:2]

            fila_datos = [fecha_caca, hora_caca, minutos_caca, quien_hizo_caca]

            datos_caca.append(fila_datos)
        
    except IndexError:
        next

#print(datos_caca)
        
columnas = ["Date", "Hour", "Minute", "Who"]

df = pd.DataFrame(datos_caca, columns=columnas)

df.to_excel("Datos_caca.xlsx")
print(df)







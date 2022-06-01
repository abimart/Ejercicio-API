import pandas as pd
import time
import hashlib
import api_restcountries as api
from data_base import ConexionDateBase

def main():
    start_time = time.time()                               #Inicia tiempo
    lines = []             
    country = api.getPais()                                #Obtener Pais
    region = api.getRegion(country)                        #Obtener Region
    language = api.getLanguage(country)                    #Obtener Lenguaje
    list_leng = language.values()
    list_leng = list(list_leng)

    for value in list_leng:
        leng= hashlib.sha1(value.encode('UTF-8')).hexdigest()                               #Encriptar lenguaje con SHA1 
        lines.append([region, country, leng, (time.time() - start_time)])

    dataframe = pd.DataFrame(lines, columns=["Region", "Country", "Language", "Time"])      #Crear Dataframe

    print("----------- Tabla de tiempos ----------------")
    print(f"Tiempo total: {dataframe['Time'].sum()} seg")
    print(f"Tiempo promedio: {dataframe['Time'].mean()} seg")
    print(f"Tiempo minimo: {dataframe['Time'].min()} seg")
    print(f"Tiempo maximo: {dataframe['Time'].max()} seg")

    db = ConexionDateBase()                             #Iniciar conexion a SQL
    db.createTable()

    for value in lines:
        db.insertData(value)                            #Insertar datos en tabla
    
    dataframe.to_json(r'data.json')                     #Generar JSON de la informacion obtenida

if __name__ == "__main__":
    main()

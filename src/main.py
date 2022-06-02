import pandas as pd
import time
import hashlib
import api_restcountries as api
from data_base import ConexionDateBase

def tableCountries(number = None):
    start_time = time.time()                                        #Inicia tiempo
    lines = []             
    countries = api.getCountry()                                    #Obtener lista de Paises
    if number is None:                                   
        number_country = len(countries)
    else:
        number_country = number
    for values_country in range(number_country):
        country = countries[values_country]["name"]["official"]
        region = api.getRegion(country)                             #Obtener Region
        language = api.getLanguage(country)                         #Obtener Lenguaje
        if language is not None:
            list_leng = language.values()
            list_leng = list(list_leng)

            for value in list_leng:
                leng= hashlib.sha1(value.encode('UTF-8')).hexdigest()                           #Encriptar lenguaje con SHA1 
                lines.append([region, country, leng, (time.time() - start_time)])

    dataframe = pd.DataFrame(lines, columns=["Region", "Country", "Language", "Time"])          #Crear Dataframe

    print("----------- Tabla de tiempos ----------------")
    print(f"Tiempo total: {dataframe['Time'].sum()} ms")
    print(f"Tiempo promedio: {dataframe['Time'].mean()} ms")
    print(f"Tiempo minimo: {dataframe['Time'].min()} ms")
    print(f"Tiempo maximo: {dataframe['Time'].max()} ms")

    db = ConexionDateBase()                             #Iniciar conexion a SQL
    db.createTable()

    for value in lines:
        db.insertData(value)                            #Insertar datos en tabla

    #print("----------- Tabla de sqlite ----------------")
    #for i in db.showTable():
    #    print(i)
    
    dataframe.to_json(r'data.json')                     #Generar JSON de la informacion obtenida
    return True

if __name__ == "__main__":
    tableCountries()

import requests
import random
import json

def getCountry():
    url = f"https://restcountries.com/v3.1/all"
    response = requests.get(url)
    respuesta = json.loads(response.text)
    return respuesta

def getLanguage(name):
    try:
        url = f"https://restcountries.com/v3.1/name/{name}?fullText=true"
        response = requests.get(url)
        return json.loads(response.text)[0]["languages"]
    except Exception as error:
        print(error)

def getRegion(name):
    url = f"https://restcountries.com/v3.1/name/{name}?fullText=true"
    response = requests.get(url)
    return json.loads(response.text)[0]["region"]
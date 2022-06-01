import requests
import random
import json

def getPais():
    try:
        url = f"https://restcountries.com/v3.1/all"
        response = requests.get(url)
        respuesta = json.loads(response.text)
        return(respuesta[random.randint(0, len(respuesta) - 1)]["name"]["official"])

    except Exception as e:
        print(e)

def getLanguage(name):
    url = f"https://restcountries.com/v3.1/name/{name}?fullText=true"
    response = requests.get(url)
    return json.loads(response.text)[0]["languages"]


def getRegion(name):
    url = f"https://restcountries.com/v3.1/name/{name}?fullText=true"
    response = requests.get(url)
    return json.loads(response.text)[0]["region"]
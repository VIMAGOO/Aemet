import json
import os
import urllib3


def get_daily(city):

    path = f"data/{city}.json"
    if os.path.isfile(path):
        with open(path, "r") as file:
            data = file.read()
    else:
        data = get_data(city)
        if not os.path.isdir("data"):
            os.makedirs("data")

        with open(path, "w") as file:
            file.write(data)

    return json.loads(data)


def get_data(city):

    key = get_key()

    url = f"https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/{city}/?api_key={key}"

    response = urllib3.request("GET", url)
    if response.status == 200:
        datos = response.json()["datos"]
    else:
        raise Exception(f"Error {response.status}: {url}")

    response = urllib3.request("GET", datos)
    if response.status == 200:
        # data = response.json()
        # aemet torna la resposta en latin-1, no en unicode
        data = response.data.decode("latin-1")
        return data
    else:
        raise Exception(f"Error {response.status}: {url}")


def get_key():

    file = "config.json"
    if not os.path.isfile(file):
        raise Exception(f"Config file not found: {config.json}")

    with open(file, "r") as file:
        config = json.load(file)
        key = config["key"]

    return key

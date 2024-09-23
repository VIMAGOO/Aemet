import aemet
from tabulate import tabulate

city = input("City: (08017) ")
#city = "08017"

data = aemet.get_daily(city)[0]

print(data["nombre"] + " : " + data["provincia"])

print("Probabilitat precipitació:")

print(tabulate(data["prediccion"]["dia"][0]["probPrecipitacion"], 
      headers="keys"))




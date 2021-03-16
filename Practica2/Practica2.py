# Practica 2 - Laboratorio de Ciberseguridad
# Yahir Alejandro Navarro Amador

import requests
import json

output = []
def call(URL):
    R = requests.get(URL)
    return (json.loads(R.content))

output.append(call("https://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=4c35b48c9218dc4d08cd6eede31f455d"))
print(output,'\n')
output.append(call("https://api.openweathermap.org/data/2.5/weather?id=2172797&appid=4c35b48c9218dc4d08cd6eede31f455d"))
print(output)

with open("Practica2.txt","w+") as txt:
    for i in output:
        txt.write(str(i)+"\n")


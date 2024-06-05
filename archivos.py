#importar las librearias necesarias
import csv #Excel separado por comas
import json #

# función para crear un archivo de texto
def crear_archivo_texto(nombre_archivo, contenido):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(contenido)
    print(f"archivo: {nombre_archivo} creado exiosamnete ")


#funcion para crear un archivo CSV
def crear_archivo_csv(nombre_archivo, datos):
    with open(nombre_archivo, "w") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(datos)
    print(f"archivo: {nombre_archivo} creado exiosamnete ")

#crear un JSON
def crear_archivo_json(nombre_archivo, datos):
    with open (nombre_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)
    print(f"archivo JSON: {nombre_archivo} creado exitosamente")

#leer txt
def leer_archivo_txt (nombre_archivo):
    with open (nombre_archivo, "r") as archivo:
        return archivo.read()

#leer CSV
def leer_archivo_csv(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return list(csv.reader(archivo))
    
#leer JSON
def leer_archivo_json(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return json.load(archivo)
    
#agregar texto a un txt existente
def agregar_contenido_txt (nombre_archivo, contenido):
    with open(nombre_archivo, "a") as archivo:
        archivo.write(contenido)
    print(f"contenido agregado en: {nombre_archivo} exiosamnete ")

contenido_txt="esto es un texto de ejemplo"
crear_archivo_texto("ejemplo.txt", contenido_txt)

#datos JSON
datos_csv = [
    ["nombre", "edad", "comuna"],
    ["eduardo", 33, "puerto montt"],
    ["campo", 18, "puerto montt"],
    ["jhon", 24, "puerta sur"]

]
crear_archivo_csv("ejemplo.csv", datos_csv)

#datos JSON
datos_json= {
    "nombre": "marcelo",
    "edad": 37,
    "comuna": "llanquihue",
    "habilidades": ["Python","HTML","CSS"]
}

crear_archivo_json("ejemplo.json", datos_json)
print(leer_archivo_txt("ejemplo.txt"))

#leer y mostrar el contenido csv
for fila in leer_archivo_csv("ejemplo.csv"):
    print(fila)

#leer y mostrar 
print(json.dumps(leer_archivo_json("ejemplo.json"), indent=4))

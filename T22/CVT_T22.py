#Integrantes que participaron en la actividad
#Chris Villalobos Tamez
#Manuel Emilio Delgado Gómez

#Importación de módulos
import requests
import json
import logging
from getpass import *
import six
import argparse

headers = {}
headers ['content-type'] = 'application/json'
headers ['api-version'] = '3'
headers ['User-Agent'] = 'python'


if six.PY3 == True:
    print ("La versión de Python es Python3")
else:
    print ("La versión de Python es Python2.\n Saliendo del programa..." )
    
#Implemento de módulo 'argparser'
parser = argparse.ArgumentParser(description="Correo a revisar")
parser.add_argument("-c", dest= "correo", help= "Correo 1", required= True)
params = parser.parse_args()

#Implemento de modulo 'getpass' para la API key
key = getpass("Escriba la API key: ")

#Place that API key here
headers ['hibp-api-key'] = key

#Solicitud

#Try por si la API no funciona.
try: 

    url = 'https://haveibeenpwned.com/api/v3/breachedaccount/'+params.correo+'?truncateResponse=false'
    r = requests.get(url, headers=headers)
#Except de la request a la API.
except Exception as e: 

    print ("Error con request a la API")
    logging.error (e)

#En caso de que todo vaya bien.
else: 

    if r.status_code == 200:
        data = r.json()
        encontrados = len(data)

        if encontrados > 0:
            print ("Los sitios en los que se ha filtrado el correo", params.correo, "son:")
        else:
            print ("El correo", params.correo, "no ha sido filtrado")

#Escritura de log con toda la info de la API.
        with open ('ReporteFiltraciones.txt', 'w') as reporte:
            for filtracion in data:
                #Sacamos la informacion de nombre, dominio, fecha y descripcion de la brecha.
                nombre = filtracion.get ("Name")
                dominio = filtracion.get ("Domain")
                fecha = filtracion.get ("BreachDate")
                descripcion = filtracion.get ("Description")
                print (filtracion["Name"], filtracion["Domain"], filtracion["BreachDate"], filtracion["Description"])
                
                #Escribimos la informacion en el reporte.
                reporte.write ("Nombre:" + nombre + "\n")
                reporte.write ("Dominio:" + dominio + "\n")
                reporte.write ("fecha:" + fecha + "\n")
                reporte.write ("descripcion:" + descripcion + "\n")
                           
                           

        msg = params.correo+" Filtraciones encontradas: "+str(encontrados)
        logging.basicConfig (filename = 'hibpINFO.log', filemode = 'a', format ="%(asctime)s %(message)s", datefmt = "%m/%d/%Y %I:%M:%S %p", level = logging.INFO)
        logging.info (msg)
   
    else:
        print ("Error en la API\n", r.status_code)
        msg = r.text
        logging.basicConfig (filename = 'hibpERROR.log', filemode = 'a', format = "%(asctime)s %(message)s", datefmt = "%m/%d/%Y %H:%M:%S", level = logging.ERROR)
        logging.error (msg) 
finally:
    print ("Finalización de la request de la API")


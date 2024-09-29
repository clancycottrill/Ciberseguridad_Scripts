#Integrantes del equipo
#Chris Villalobos Tamez

import subprocess
from openpyxl import Workbook
import csv

ruta_script = r"C:\Users\chris\Desktop\Fac\ProgCib\Tareas\Python\T26\monitor_servicios.ps1"
ruta_csv = r"C:\Users\chris\Desktop\Fac\ProgCib\Tareas\Python\T26\servicios.csv"
ruta_excel = r"C:\Users\chris\Desktop\Fac\ProgCib\Tareas\Python\T26\servicios.xlsx"


try:
    resultado = subprocess.run (["powershell", "-File", ruta_script], capture_output=True, text=True)
    print ("Salida de comando Powershell:")
    print (resultado.stdout)

    #Creacion de libro de trabajo de Excel
    libro = Workbook()
    hoja = libro.active

    try:

        #Lectura de servicios del archivo CSV
        with open (ruta_csv, mode = 'r', newline='') as archivo_csv:
            lector_csv = csv.reader (archivo_csv)

            for fila in lector_csv:
                hoja.append(fila)

        #Guardamos modificaciones al libro de excel
        libro.save(ruta_excel)
        print("Datos guardados en archivo Excel correctamente")
    
    except Exception as e:
        print (f"Error al guardar datos en archivo Excel: {e}")

    if resultado.stderr:
        print ("Error de Powershell:")
        print(resultado.stderr)

except Exception as e:
    print (f"Error del script de Python: {e}")

finally:
    print ("Ejecución de script Powershell terminada.")




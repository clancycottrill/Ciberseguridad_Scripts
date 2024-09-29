#!/bin/python

"""
Chris Villalobos Tamez
Angel Saldaña Aguilar
Patricio Emiliano Garay ELizondo
"""


import subprocess  # Módulo para ejecutar comandos externos
import re  # Módulo para trabajar con expresiones regulares

standard_ports = {22, 25, 80, 465, 587, 8080}

# Función que ejecuta el script de bash 'monitor_conexiones.sh'
def ejecutar_bash_script():
    try:
        resultado = subprocess.run(['bash', 'monitor_conexiones.sh'], capture_output=True, text=True, check=True)
        return resultado.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error ejecutando el script: {e}")
        return None

# Función que analiza las conexiones de red para identificar puertos no estándar
def analizar_conexiones(salida):
    conexiones_sospechosas = []
    regex = re.compile(r':(\d+)\s')

    for linea in salida.splitlines():
        match = regex.search(linea)
        if match:
            puerto = int(match.group(1))
            # Verifica si el puerto no está en la lista de puertos estándar
            if puerto not in standard_ports:
                conexiones_sospechosas.append(linea)

    return conexiones_sospechosas

# Función que genera un reporte de conexiones sospechosas en un archivo de texto
def generar_reporte(conexiones_sospechosas, archivo_reporte='reporte_conexiones.txt'):
    with open(archivo_reporte, 'w') as f:
        f.write("Conexiones sospechosas detectadas:\n")
        f.write("\n".join(conexiones_sospechosas))
    print(f"Reporte generado: {archivo_reporte}")

if __name__ == "__main__":
    salida = ejecutar_bash_script()
    
    if salida:
        # Analiza las conexiones para identificar conexiones sospechosas
        conexiones_sospechosas = analizar_conexiones(salida)
        
        if conexiones_sospechosas:
            generar_reporte(conexiones_sospechosas)
        else:
            print("No se detectaron conexiones sospechosas.")

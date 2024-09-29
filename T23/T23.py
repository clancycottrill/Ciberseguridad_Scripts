import pyautogui
import subprocess 
import datetime

#Captura de pantalla
date=datetime.datetime.now()
date_comp=str(date.strftime('%Y%m%d_%H %M %S'))

try:
    screenshot = pyautogui.screenshot()

except:
    print("Hubo un error al tomar la captura de pantalla")

else:
    screenshot.save("Captura"+date_comp+".png")
    
    
#Lista de procesos  
try:
    procesos = subprocess.run(["tasklist"], capture_output=True, shell=True, text=True)
    
except Exception as e:
    print ("Error al generar lista de procesos")
    
else: 
    with open ('listaprocesos'+date_comp+'.txt','w') as lista:
        lista.write(str(procesos))

finally: 
    print ("Generación de lista completada")

        


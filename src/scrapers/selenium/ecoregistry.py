import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from datetime import datetime

from src.functions.get_download_path import get_download_path
from src.functions.setup_chrome_options import setup_chrome_options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc

def ecoregistry():
    """
    Login into EcoRegistry and then create a project 
    """
    download_path = get_download_path(__file__)
    options = setup_chrome_options(download_path)

    browser = webdriver.Chrome(options=options)
    wait = WebDriverWait(browser, 20)

    ##### OPEN ECOREGISTRY LOGIN #####
    browser.get("https://registry-ecoregistry-test.ecoregistry.io/login")
    try:
    
        time.sleep(4)
        # Encuentra el campo de email usando el atributo type
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        email_input.clear()
        email_input.send_keys("ecoregistry-technical-test@yopmail.com")
        time.sleep(4)

        # Encuentra el campo de contraseña usando el atributo type
        password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        password_input.clear()
        password_input.send_keys("Tech-test-2025.")

        # Botón de login
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/form/div[4]/button")))
        login_button.click()
        time.sleep(4)
        browser.maximize_window()
        time.sleep(4)
        print("Se ha logueado correctamente")

    except Exception as e:
        print("Posible error a la hora de loguearse. Error: ", e)
        time.sleep(1)
    try:
        ##### HOVER Y CLIC EN "CREAR PROYECTO" #####
        proyectos_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div[1]/div[2]/ul/li[3]/span")))

        actions = ActionChains(browser)
        actions.move_to_element(proyectos_menu).perform()
        time.sleep(1.5)

        crear_proyecto = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[1]/div[2]/ul/li[3]/ul/a[2]")))
        crear_proyecto.click()

        print(" Clic en 'Crear proyecto' exitoso.")
        time.sleep(5)

    except Exception as e:
        print(" No se pudo hacer clic en 'Crear proyecto'. Error:", e)
        time.sleep(3)


    try:
        ###NOMBRAR PROYECTO###
        nombre = f"Project {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

        campo_nombre = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/div[10]/div[1]/div/div/input")))
        browser.execute_script("window.scrollBy(0, 300);")
        time.sleep(1)
        campo_nombre.clear()
        campo_nombre.send_keys(nombre)
        time.sleep(2)
        print(" Se ha nombrado correctamente el proyecto")
    except Exception as e:
        print(" No se pudo  escribir el nombre del proyecto. Error:", e)
        time.sleep(3)

    try:
        # Hacer scroll al contenedor visible de "Documento de descripción del proyecto"
        upload_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[7]/div[2]/div[2]/div')))

    # Hacer scroll hasta el botón para asegurarse de que sea visible
        browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", upload_button)
        time.sleep(1)
        print(" Se ha scroleado correctamente")
    except Exception as e:
        print(" Error al  al scrolear:", e)



    try:
# Esperar a que el input de archivo esté presente por su XPath absoluto
        upload_button  = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[7]/div[2]/div[2]/div/input")))

        # Forzar visibilidad en caso de que esté oculto por FilePond u otros estilos
        browser.execute_script("""
            arguments[0].style.display = 'block';
            arguments[0].style.opacity = 1;
        """, upload_button)

        print(" el intento de identificar el input es exitoso.")
            
    except Exception as e:
        print(" Error al  intento de identificar el input:", e)
        time.sleep(3)



    
    try:
        upload_button  = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[7]/div[2]/div[2]/div/input")))
        ruta_archivo = "/home/emanuelnore/technical-test-automated-tests/PDD.pdf"
        print("¿Existe el archivo?", os.path.isfile(ruta_archivo))  # Ahora debe imprimir True

        upload_button.send_keys(ruta_archivo)
        print(" Archivo subido correctamente.")
        time.sleep(2)
    except Exception as e:
        print(" Error al subir archivo:", e)
    try:
        # Esperar y hacer scroll al botón "Guardar"
        guardar_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div/div[8]/div[2]/button[2]")))
        browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", guardar_btn)
        time.sleep(1)

        # Clic en "Guardar"
        guardar_btn.click()
        print(" Se hizo clic en 'Guardar' correctamente.")
        time.sleep(3)

        # Intentar confirmar si aparece el modal
        try:
            confirmar_btn = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Confirmar']"))
            )
            confirmar_btn.click()
            print(" Confirmación realizada.")
        except:
            print(" No apareció modal de confirmación. Se continúa.")

    except Exception as e:
        print(" Error al hacer clic en 'Guardar' o confirmar:", e)
        time.sleep(3)

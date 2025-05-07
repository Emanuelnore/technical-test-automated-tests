"""Script to get all projects, issuances  and retirements from Gold Standard Registry (as an Excel Files)"""

import os
import requests
import pandas as pd

from src.functions.get_download_path import get_download_path
from src.functions.validate_directory import validate_directory  # pylint: disable=E0401

def ecoregistry():
    """
    Login into EcoRegistry and then create get project positions and export it as .csv
    """
    download_path = get_download_path(__file__)
    validate_directory(download_path)
    # Paso 1: LOGIN
def hacer_login():
    """
    Realiza login en la API de EcoRegistry y retorna el token JWT.
    """
    login_url = "https://api-ecoregistry-test.ecoregistry.io/platform/user/login"
    login_payload = {
        "email": "ecoregistry-technical-test@yopmail.com",
        "password": "U2FsdGVkX1/84KPKf9i1r21Wi+MhuqFinH5cunWdlv0=",
        "recaptchaValue": "cualquier_string"
    }
    login_headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "lng": "es",
        "platform": "ecoregistry"
    }

    try:
        response = requests.post(login_url, json=login_payload, headers=login_headers)
        response.raise_for_status()
        token = response.json().get("token")

        if not token:
            print(" Login fallido: no se recibió token.")
            print(" Respuesta completa:", response.json())
            return None

        print(" Login exitoso. Token recibido.")
        return token

    except requests.RequestException as e:
        print(" Error al hacer login:", e)
        return None


def obtener_proyectos(token):
    """
    Usa el token para consultar la lista de proyectos.
    Retorna una lista de proyectos o None.
    """
    data_url = "https://api-ecoregistry-test.ecoregistry.io/platform/projectCompanySerial/projectsVintage"
    data_headers = {
        "accept": "application/json",
        "authorization": f"Bearer {token}",
        "content-type": "application/json",
        "lng": "es",
        "platform": "ecoregistry"
    }

    try:
        response = requests.get(data_url, headers=data_headers)
        response.raise_for_status()
        data = response.json()
        projects = data.get("projects", [])

        if not projects:
            print(" No se encontraron datos en 'projects'.")
            return None

        print(f" {len(projects)} proyectos recibidos.")
        return projects

    except requests.RequestException as e:
        print(" Error al obtener los proyectos:", e)
        return None


def exportar_csv(projects, output_dir):
    """
    Exporta la lista de proyectos a un archivo CSV en el directorio indicado.
    """
    try:
        df = pd.DataFrame(projects)
        output_path = os.path.join(output_dir, "projects.csv")
        df.to_csv(output_path, index=False)
        print(f" Archivo CSV guardado en: {output_path}")
    except Exception as e:
        print(" Error al exportar a CSV:", e)


def ecoregistry():
    """
    Función principal que coordina todo el flujo.
    """
    # Preparar ruta de salida
    download_path = get_download_path(__file__)
    validate_directory(download_path)

    # Login
    token = hacer_login()
    if not token:
        return

    # Obtener proyectos
    projects = obtener_proyectos(token)
    if not projects:
        return

    # Exportar CSV
    exportar_csv(projects, download_path)


if __name__ == "__main__":
    ecoregistry()
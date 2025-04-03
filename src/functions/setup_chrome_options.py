import os
from pathlib import Path
from selenium import webdriver

from src.functions.validate_directory import validate_directory

def setup_chrome_options(download_path):
    # Set chrome options
    options = webdriver.ChromeOptions()
    # options.add_experimental_option(
    #     "detach", True)  # the browser doesn't close
        # Leer la variable de entorno para el modo interactivo
    interactive_mode = os.getenv("interactive_mode", "False").lower() == "true"
    
    if not interactive_mode:
        options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    validate_directory(download_path)
    path = Path(download_path)
    # Define downloads directory
    prefs = {"download.default_directory": str(path.absolute())}
    options.add_experimental_option("prefs", prefs)
    return options
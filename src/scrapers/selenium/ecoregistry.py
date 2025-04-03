import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.functions.get_download_path import get_download_path
from src.functions.setup_chrome_options import setup_chrome_options

def ecoregistry():
    """
    Login into EcoRegistry and then create a project 
    """
    download_path = get_download_path(__file__)
    options = setup_chrome_options(download_path)

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(60)

    ##### OPEN ECOREGISTRY LOGIN #####
    browser.get("https://registry-ecoregistry-test.ecoregistry.io/login")
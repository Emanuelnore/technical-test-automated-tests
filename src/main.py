""" Entry point for all automated tests. """

from dotenv import load_dotenv

from src.functions.log_error import log_error

from src.scrapers.http.ecoregistry import ecoregistry as ecoregistry_http
from src.scrapers.selenium.ecoregistry import ecoregistry as ecoregistry_selenium

load_dotenv()

functions = [
    ecoregistry_selenium,
    ecoregistry_http,
]

for func in functions:
    try:
        print("**************************************************")
        print(f"RUNNING {func.__name__}...")
        func()
        print("**************************************************\n\n")
    except Exception as e:
        log_error(func.__name__, e)
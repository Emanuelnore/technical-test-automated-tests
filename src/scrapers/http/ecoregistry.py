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
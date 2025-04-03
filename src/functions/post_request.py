""" Functions needed for http request for web scraping """

import requests
from .validate_directory import validate_directory


def post_request(
        url: str,
        headers: dict,
        payload: dict,
        download_path: str,
        file_name: str,
        payload_type: str):
    """ 
    This function makes a post HTTP request, and saves the response in a file.
    -----------
    Parameters:

    url: str
        The url of the request
    headers: dict
        The headers of the request
    payload: dict
        The payload of the request
    download_path: str
        The path where the file will be saved
    file_name: str
        The name of the file
    payload_type: str
        The type of the payload, could be 'form' or 'json'

    --------
    Returns:

    None
    """
    validate_directory(download_path)

    if payload_type == 'form':
        with requests.post(url, headers=headers, data=payload, timeout=120) as req:
            with open(download_path + '/' + file_name, 'wb') as file_response:
                file_response.write(req.content)

    elif payload_type == 'json':
        with requests.post(url, headers=headers, json=payload, timeout=120) as req:
            with open(download_path + '/' + file_name, 'wb') as file_response:
                file_response.write(req.content)

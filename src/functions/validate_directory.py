""" Module for validating directories """
from pathlib import Path


def validate_directory(path):
    """
    Validates  that the path is a directory.
    If it is not, it will create the directory.
    ---------------------------
    Parameters:
        path: str
    """
    path = Path(path)
    if not path.absolute().exists():
        path.absolute().mkdir(parents=True, exist_ok=True)

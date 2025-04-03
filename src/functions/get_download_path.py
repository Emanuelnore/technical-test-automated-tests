import os

def get_download_path(caller_file):
    file_name = os.path.splitext(os.path.basename(caller_file))[0]
    output_folder = os.getenv("output_folder", "registries")
    download_path = f"{output_folder}/{file_name}"
    return download_path
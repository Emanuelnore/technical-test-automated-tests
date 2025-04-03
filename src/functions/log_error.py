""" Function to log errors in a file """
import json
import traceback
from datetime import datetime

from src.functions.validate_directory import validate_directory

error_logs_directory = 'error_logs'

def log_error(func_name, error):
    validate_directory(error_logs_directory)
    
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"{error_logs_directory}/error_log_{current_time}.json"
    
    print("----------------------------------------------------------------------------------------------")
    print(f"ERROR IN {func_name}\n")
    print(traceback.format_exc())
    print("----------------------------------------------------------------------------------------------")
    error_info = {
        "function": func_name,
        "file": __file__,
        "error": str(error),
        "traceback": traceback.format_exc(),
        "timestamp": current_time
    }
    
    with open(file_name, 'a') as f:
        json.dump(error_info, f, indent=4)
        f.write('\n')
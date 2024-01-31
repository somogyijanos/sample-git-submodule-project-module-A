import sys

from src.utils.prettify import greet
from src.read import read_folder_contents

def check_folder(path:str):
    # Greet
    greet()
    
    # Check Python version
    python_version = sys.version.split(" (")[0]
    print(f'I am using Python {python_version}!\n')

    # Read contents
    read_folder_contents(path)
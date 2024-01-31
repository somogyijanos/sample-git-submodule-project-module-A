from src.utils.prettify import greet

def print_version(tag:str):
    greet()
    print(f'This is version: {tag}!')
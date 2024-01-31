import os

def read_folder_contents(path:str):
    contents = os.listdir(path)
    folders = [c for c in contents if os.path.isdir(os.path.join(path, c))]
    files = [c for c in contents if os.path.isfile(os.path.join(path, c))]

    print(f'Found:\n  - {len(files)} files\n  - {len(folders)} folders')
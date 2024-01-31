import click

import sys
sys.path.append('.')

from src.core import check_folder

@click.command()
@click.argument('path')
@click.help_option('-h', '--help')
def main(path:str):
    check_folder(path)

if __name__ == '__main__':
    main()
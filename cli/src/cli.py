# will include the commands but not the controller handling said command
import click
import os
import shutil
from datetime import datetime

from .config import *

# Set the base directory for file management
BASE_DIR = ""

CONFG = loadConfig()


@click.group()
def cli():
    pass

# python cli.py date
@cli.command()
@click.option('--format', type=click.Choice(['long', 'short', 'custom']), default=CONFG['date-format'], help='Date format')
def date(format):
    now = datetime.now()
    if format == 'short':
        formatted_date = now.strftime('%b %d, %y')
        modifyConfig("date-format", formatted_date)

    elif format == 'custom':
        custom_format = click.prompt('Enter custom date format', default='%b %d, %y')
        formatted_date = now.strftime(custom_format)

    else:
        formatted_date = now.strftime('%B %d, %Y')
    click.echo(formatted_date)


# Time Command
# python cli.py time
@cli.command()
@click.option('--format', type=click.Choice(['12-hour', '24-hour']), default='12-hour', help='Time format')
def time(format):
    now = datetime.now()
    if format == '24-hour':
        formatted_time = now.strftime('%H:%M')
        
    else:
        formatted_time = now.strftime('%I:%M %p')

    click.echo(formatted_time)


# Auto Deploy Command
# python cli.py audp
@cli.command()
def audp():
    click.echo('Auto deploy command executed.')
    # Place your auto-deployment logic here


# File Management Command
@cli.command()
@click.argument('action', type=click.Choice(['cr', 'rd', 'upd', 'del', 'mv', 'copy', 'conv']))
@click.argument('filename', required=False)
def file(action, filename):
    file_path = os.path.join(BASE_DIR, filename) if filename else None

    match action:
        case 'cr':
            click.echo('Creating file...')
            with open(file_path, 'w') as file:
                file.write('This is a sample file.')

        case 'rd':
            click.echo('Reading file...')
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    click.echo(content)
            except FileNotFoundError:
                click.echo(f'File "{filename}" not found.')

        case 'upd':
            click.echo('Updating file...')
            try:
                with open(file_path, 'a') as file:
                    file.write('\nUpdated content.')
            except FileNotFoundError:
                click.echo(f'File "{filename}" not found.')

        case 'del':
            click.echo('Deleting file...')
            try:
                os.remove(file_path)
                click.echo(f'File "{filename}" deleted.')
            except FileNotFoundError:
                click.echo(f'File "{filename}" not found.')

        case ('mv' | 'copy'):
            destination = click.prompt('Enter destination directory')
            destination_path = os.path.join(destination, filename)
            match action:
                case 'move':
                    click.echo('Moving file...')
                    shutil.move(file_path, destination_path)
                case 'copy':
                    click.echo('Copying file...')
                    shutil.copy(file_path, destination_path)

        case 'conv':
            extension = click.prompt('Enter target file extension')
            target_file_path = os.path.join(BASE_DIR, f'converted.{extension}')
            click.echo(f'Converting file to {extension}...')
            try:
                shutil.copy(file_path, target_file_path)
                click.echo(f'File converted to {extension}.')
            except FileNotFoundError:
                click.echo(f'File "{filename}" not found.')


        case _:
            click.echo("Command unkown")


# Package Management Command
@cli.command()
def pkg():
    click.echo('Package management command executed.')
    # Place your package management logic here


@click.command()
def pkg_ver():
    return 


if __name__ == '__main__':
    cli()


"""
Date Command:
To display the default long-format date:
python cli.py date

To display the date in short format:
python cli.py date --format short

To display the date in a custom format:
python cli.py date --format custom

Time Command:
    To display the default 12-hour time:
    python cli.py time

    To display the time in 24-hour format:
    python cli.py time --format 24-hour

Auto Deploy Command:
    To execute the auto deploy command:
    python cli.py audp

File Management Command:
    To create a file named example.txt:
        python cli.py file crt example.txt

    To read the content of the file:
        python cli.py file rd example.txt

    To update the content of the file:
    python cli.py file upd example.txt

    To move the file to another directory:
        python cli.py file mv example.txt /path/to/destination/

    To convert the file to a different format:
        python cli.py file conv example.txt

Package Management Command:

    To execute the package management command:
    python cli.py pkg
"""
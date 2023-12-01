import asyncio
import subprocess
import shutil
import os
import click
from git import Repo
from ..config import *

CONF = loadConfig()

async def build(script_path, landing_page_repo_path, landing_page_exe_name):
    # Step 1: Build the .exe using PyInstaller
    build_command = f'pyinstaller --onefile {script_path}'
    process = await asyncio.create_subprocess_shell(
        build_command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = await process.communicate()

    # Check if the build was successful
    if process.returncode == 0:
        click.echo('Build successful.')

    else:
        click.echo(f'Build failed. Error: {stderr.decode()}')
        return

    # Step 2: Replace the existing .exe in the landing page repo
    try:
        exe_name = script_path.split(".")[0] + ".exe"
        new_exe_path = os.path.join(landing_page_repo_path, landing_page_exe_name)
        shutil.copy(exe_name, new_exe_path)
        click.echo(f'Replaced {exe_name} in the landing page repo.')

    except Exception as e:
        click.echo(f'Replacement failed. Error: {str(e)}')
        return

    # Step 3: Commit and push the changes to the landing page repo
    repo = Repo(landing_page_repo_path)

    try:
        # new_version = CONF['app-version']
        # modifyConfig("app-version", new_version)

        await repo.git.add(update=True)
        await repo.git.commit('-m', f'App uploaded to new Version: Version {CONF["app-version"]}')
        await repo.git.push()
        click.echo('Changes committed and pushed to the landing page repo.')
        
    except Exception as e:
        click.echo(f'Failed to commit and push changes. Error: {str(e)}')

if __name__ == '__main__':
    if CONF['alpha'] == "True":
        click.echo("Not implemented yet")

    else:
        # Specify the path to your Python script, landing page repo, and landing page executable name
        main_src                = '../../../run.py'
        landing_page_repo_path  = 'tba, not created yet >__<'
        landing_page_exe_name   = 'run.exe'

        # Run the asynchronous function
        asyncio.run(
            build(main_src, landing_page_repo_path, landing_page_exe_name)
        )

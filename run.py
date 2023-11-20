# todo:
# run fastapi server in 1 process
# run front-end react with another process

from server.main import run
import subprocess
import multiprocessing


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

def run_front_end():
    node_modules_path = "./dnd_panel" 


server = multiprocessing.Process(target=run)
front_end = multiprocessing.Process()
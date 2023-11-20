# todo:
# run fastapi server in 1 process
# run front-end react with another process

from server.main import run
import os
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
    specific_path = './dnd_panel'
    node_modules_path = os.path.join(specific_path, 'node_modules')

    # Check if the directory exists
    if os.path.exists(node_modules_path) and os.path.isdir(node_modules_path):
        print('The node_modules directory exists in the specified path.')

        run_command("npm run start")
    else:
        print('The node_modules directory does not exist in the specified path.')

        run_command("npm install")

    
    run_command("npm run start")


server = multiprocessing.Process(target=run)
front_end = multiprocessing.Process(target=run_front_end)

processes = {server, front_end}

def runner():
    try:
        for process in processes:
            process.start()

    except KeyboardInterrupt:
        print("KeyboardInterrupt: Terminating all processes")

        for end_process in processes:
            if end_process.is_alive():
                end_process.terminate()
                end_process.join()

            else:
                if end_process.is_alive() is False:
                    print(f"process: {end_process.name} is not running")

    except Exception as e:
        print(f"error running: \n{str(e)}")
        return
    

if __name__ == "__main__":
    runner()
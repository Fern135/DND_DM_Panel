from server.main import run
import subprocess
import os
import multiprocessing

def run_command(command, cwd=None):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True, cwd=cwd)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

def run_front_end():
    react_project_path = os.path.abspath('./dnd_panel')
    node_modules_path = os.path.join(react_project_path, 'node_modules')

    if os.path.exists(node_modules_path) and os.path.isdir(node_modules_path):
        print('The node_modules directory exists in the specified path.')
        run_command("npm install", cwd=react_project_path)
    else:
        print('The node_modules directory does not exist in the specified path.')
        run_command("npm install", cwd=react_project_path)

    run_command("npm run start", cwd=react_project_path)

server      = multiprocessing.Process(target=run)  # Replace with your actual FastAPI server target
front_end   = multiprocessing.Process(target=run_front_end)

processes: list = [server, front_end]

def runner():
    try:
        for process in processes:
            process.start()

    except KeyboardInterrupt:
        print("KeyboardInterrupt: Terminating all processes")

        for end_process in processes:
            if end_process.is_alive(): # check if process is alive then terminate
                end_process.terminate()
                end_process.join()

            else:
                if end_process.is_alive() is False: # if there's no process alive
                    print(f"process: {end_process.name} is not running") # show the dead process

                    break

    except Exception as e:
        print(f"error running: \n{str(e)}")
        return

if __name__ == "__main__":
    runner()

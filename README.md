# 🛠️ Keylogger with Telegram Exfiltration + HID Dropper

This project consists of:

- A **Python-based keylogger** that logs keystrokes, clipboard data, and exfiltrates logs via a Telegram bot.
- A **HID-based dropper script** (written for Digispark/Arduino) that automates the deployment and persistence of the keylogger on Windows systems.

> **For educational purposes only. Do not use this on systems without explicit permission. Misuse may violate laws and ethical guidelines.**

---

## Project Contents

### `keylogger.py`
- Logs key presses and clipboard contents.
- Sends data to Telegram once it exceeds a threshold or upon kill switch trigger.
- Kill switch: typing `wecanshutitnow` ends execution and sends all logs.
- Saves bot credentials in `Dependency/telegram.details`.

### `dropper.ino`
- Runs on Digispark or similar USB HID devices.
- Emulates keystrokes to:
  - Open PowerShell/CMD as admin.
  - Disable PowerShell execution restrictions.
  - Add Windows Defender exclusions.
  - Download and run the keylogger.
  - Set it to auto-start on system boot.

---
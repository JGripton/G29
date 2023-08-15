Pedal-to-Key/Mouse Program
This script allows you to use Logitech G29 pedal presses to trigger mouse clicks or keyboard key presses.

Configuration
You can customize the behavior of each pedal using the config.json file.

Fields Explanation:
sensitivity: This determines how hard you need to press a pedal before it's registered. This is a value between 0 (lightest press) and 1 (full press). For instance, a sensitivity of `0.5` means the pedal needs to be pressed halfway or more to register.

sleep_time: This determines how often the program checks the pedal input. It's in seconds. A value of `0.1` means it checks every 100 milliseconds.

accelerator, brake, and clutch: Configuration for each pedal.

enabled: If set to `true`, the pedal will trigger an action. If `false`, it won't.

action_type: Determines if the pedal triggers a mouse click or a keyboard press.

`"mouse"`: The pedal will trigger a mouse click.
`"keyboard"`: The pedal will trigger a keyboard press.
button: If `action_type` is set to `"mouse"`, this determines which mouse button will be clicked.

`"left"`: Left mouse button.
`"right"`: Right mouse button.
`"middle"`: Middle mouse button (scroll wheel click).
key: If `action_type` is set to `"keyboard"`, this specifies the keyboard key to press. You can use any character like `"a"`, `"b"`, etc., or special keys like `"space"`, `"enter"`, etc.

Editing the Configuration:
To change any setting, just open the `config.json` file in a text editor and modify the value you want to change. Save the file and restart the script for the changes to take effect.

Running the Script
Ensure you have the required modules installed using pip:

```
pip install pygame pyautogui
pip install pygame pygame
```

Then, simply run the script:

```
python G29.py
```

Installing Python and pip for Windows
Installing Python:
Go to the official Python downloads page: https://www.python.org/downloads/
Download the latest version for Windows.
Launch the installer.
Make sure to check the box that says Add Python x.x to PATH at the bottom. This ensures that Python and pip are accessible from the command line.
Choose the default installation or customize as needed and click on the Install button.
Verifying Installation:
Open a new Command Prompt.
Type `python --version` and press Enter. You should see the version number of Python displayed.
Type `pip --version` and press Enter. You should see the version number of pip displayed.





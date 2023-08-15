import pygame
import time
import pyautogui
import json

# Load configuration from JSON
with open("config.json", "r") as config_file:
    config = json.load(config_file)

SENSITIVITY = config["sensitivity"]
SLEEP_TIME = config["sleep_time"]
ACCELERATOR = config["accelerator"]
BRAKE = config["brake"]
CLUTCH = config["clutch"]

# Initialize pygame
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick detected!")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

previous_accelerator = 0
previous_brake = 0
previous_clutch = 0

last_time_pressed = time.time()

while True:
    pygame.event.pump()

    current_time = time.time()
    time_since_last_press = (current_time - last_time_pressed) * 1000

    accelerator = joystick.get_axis(1)
    brake = joystick.get_axis(2)
    clutch = joystick.get_axis(3)

    threshold = -SENSITIVITY

    # Accelerator detection
    if accelerator < threshold and previous_accelerator >= threshold:
        print(f"Accelerator pressed! Time since last press: {time_since_last_press}ms")
        if ACCELERATOR["enabled"]:
            if ACCELERATOR["action_type"] == "mouse":
                pyautogui.click(button=ACCELERATOR["button"])
            elif ACCELERATOR["action_type"] == "keyboard":
                pyautogui.press(ACCELERATOR["key"])
        last_time_pressed = current_time

    # Brake detection
    if brake < threshold and previous_brake >= threshold:
        print(f"Brake pressed! Time since last press: {time_since_last_press}ms")
        if BRAKE["enabled"]:
            if BRAKE["action_type"] == "mouse":
                pyautogui.click(button=BRAKE["button"])
            elif BRAKE["action_type"] == "keyboard":
                pyautogui.press(BRAKE["key"])
        last_time_pressed = current_time

    # Clutch detection
    if clutch < threshold and previous_clutch >= threshold:
        print(f"Clutch pressed! Time since last press: {time_since_last_press}ms")
        if CLUTCH["enabled"]:
            if CLUTCH["action_type"] == "mouse":
                pyautogui.click(button=CLUTCH["button"])
            elif CLUTCH["action_type"] == "keyboard":
                pyautogui.press(CLUTCH["key"])
        last_time_pressed = current_time

    previous_accelerator = accelerator
    previous_brake = brake
    previous_clutch = clutch

    time.sleep(SLEEP_TIME)

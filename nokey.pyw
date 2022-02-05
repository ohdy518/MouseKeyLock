import keyboard
while True:
    if keyboard.read_key() != "":
        keyboard.press_and_release("backspace")
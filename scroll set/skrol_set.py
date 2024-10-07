import pyautogui
import keyboard


def scroll_down(amount):
    # Scroll down
    pyautogui.scroll(-amount)

def scroll_up(amount):
    # # Scroll up
    pyautogui.scroll(amount)


print("Press 's' to scroll down or 'w' to scroll up. Press 'q' to exit.")

while True:
    if keyboard.is_pressed('s'):
        scroll_down(100)  # Set units
    elif keyboard.is_pressed('w'):  # Set units
        scroll_up(100)
    elif keyboard.is_pressed('q'):  # exit
        print("exit...")
        break

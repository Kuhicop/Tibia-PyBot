import os
import time
import pyautogui
import win32gui
from threading import Thread
from tkinter import *
from pynput import keyboard

bot = True
running = False
status_alerts = False
status_healer = False
status_runemaker = False
spell = ""
spell_time = 0

# CREATE KEYS
COMBINATION = [
    {keyboard.Key.ctrl, keyboard.Key.end},
    {keyboard.Key.shift, keyboard.Key.end}
    ]

current = set()


def execute():
    print("executed2")
    os._exit(1)


def on_press(key):
    if any([key in COMBO for COMBO in COMBINATION]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATION):
            execute()


def on_release(key):
    pass


def listen():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


threads = list()
lt = Thread(target=listen)
threads.append(lt)
lt.start()


class WindowMgr:
    # FOCUS GAME
    def __init__ (self):
        self._handle = None

    def find_window(self, class_name, window_name=None):
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        win32gui.SetForegroundWindow(self._handle)


def focus():
    # FOCUS GAME
    w = WindowMgr()
    w.find_window_wildcard(".*Tibia.*")
    w.set_foreground()


def alerts():
    print("You've selected (1) Alerts.")
    menu()


def healer():
    print("You've selected (2) Healer.")
    menu()


def eat_food():
    try:
        foodXY = pyautogui.locateOnScreen("food.png")
        pyautogui.moveTo(foodXY.x, foodXY.y)
        pyautogui.click(x=foodXY.x, y=foodXY.y, button="right")
    except:
        print("Exception: eat_food")

def making_runes(rune_spell, rune_time):
    while rune_spell != "":
        try:
            pyautogui.locateOnScreen("mana.png", grayscale=True)
            # Make the rune
            focus()
            pyautogui.typewrite(rune_spell)
            pyautogui.press('enter')
            eat_food()
        except:
            print("Except: making runes")
        print("Making runes: " + rune_spell)
        time.sleep(rune_time)


def runemaker():
    print("You've selected (3) Runemaker.")
    print("")
    global spell
    spell = input("Spell: ")
    global spell_time
    spell_time = int(input("Spell time: "))
    menu()


def setup_client():
    print("You've selected (5) Setup new client.")
    menu()


def start():
    print("You've selected (0) START.")
    global running
    running = True
    global spell
    global spell_time
    if spell != "":
        thread1 = Thread(target=making_runes, args=(spell, spell_time, ))
        thread1.start()


# MENU
def menu():
    os.system('cls')

    print("SHIFT + END WILL CLOSE THE BOT")
    print("")
    print("(1) Alerts")
    print("(2) Healer")
    print("(3) Runemaker")
    print("")
    print("(5) Setup new client")
    print("")
    print("(0) START")

    choice = input("Choice: ")
    os.system('cls')

    if choice == '1':
        alerts()
    elif choice == "2":
        healer()
    elif choice == "3":
        runemaker()
    elif choice == "5":
        setup_client()
    elif choice == "0":
        start()
    else:
        print("Wrong choice!")
        input("Press any key to exit...")


# DEFAULT ROUTINE #
# IMAGES
# Move to images folder
os.chdir("images")

# Create an image list
image_list = ["health", "mana", "battle_list", "food"]
# Loop image_list to check if images exists, so we avoid calling null files
for i in image_list:
    if not os.path.isfile(i + ".png"):
        print("Unable to find image file: " + i + ".png")
        wait = input("Press any key to quit.")
        sys.exit(0)


while bot:
    if running:
        print("Bot running.")
        time.sleep(1)
    else:
        menu()


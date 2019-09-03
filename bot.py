# Imports
import sys
import time
import datetime
import pyautogui
import ctypes

# Vars
delay = 1
running = True
mx = 0
my = 0
spell1 = "adori vita vis"
spell2 = "adori vita vis"
food_delay = 130
runes_in_a_row_1 = 1
runes_in_a_row_2 = 1

SendInput = ctypes.windll.user32.SendInput
pyautogui.FAILSAFE = False

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# Actuals Functions
def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def findimage(image, position):
    global mx
    global my
    image = image + ".png"
    try:
        if position == 1:        
            mx, my = pyautogui.locateCenterOnScreen(image, region=(0, 0, 960, 1080))
            print("return TRUE for " + image)
            return True        
        if position == 2:
            mx, my = pyautogui.locateCenterOnScreen(image, region=(960, 0, 1920, 1080))
            print("return TRUE for " + image)
            return True
    except:
        print("return FALSE for " + image)
        return False        


def makerunes(side):
    if findimage('blankrune', side):
        runex = mx
        runey = my
        print(runex, runey)
        pyautogui.click(x=runex, y=runey)
        time.sleep(delay)
        if findimage('hand', side):
            pyautogui.dragTo(mx, my, button='left')
            time.sleep(delay)
            pyautogui.typewrite(spell1, interval=0.25)
            time.sleep(delay)
            PressKey(0x1C)
            time.sleep(delay)
            ReleaseKey(0x1C)
            time.sleep(delay)
            pyautogui.dragTo(runex, runey, button='left')
            time.sleep(delay)


def runemaker():
    # Make runes 1
    if findimage('mana', 1):
        for i in range(runes_in_a_row_1):
            makerunes(1)
    # Make runes 2
    if findimage('mana', 2):
        for i in range(runes_in_a_row_2):
            makerunes(2)


def eatfood():
    # Eat food 1
    if findimage('mushroom', 1):
        pyautogui.click(x=mx, y=my, button='right', clicks=5, interval=0.5)
        time.sleep(delay)
    # Eat food 2
    if findimage('mushroom', 2):
        pyautogui.click(x=mx, y=my, button='right', clicks=5, interval=0.5)
        time.sleep(delay)


print("Welcome back, Kuhi")
print("Your script is running...")
print()

# Main loop
script_local_time = 0
while running:
    try:
        # directx scan codes https://gist.github.com/tracend/912308
        # if (datetime.datetime.now().hour < 7) or (datetime.datetime.now().hour > 14):
        runemaker()
        # else:
        # time.sleep(4)

        if script_local_time >= food_delay:
            eatfood()
            script_local_time = 0
        else:
            script_local_time += 5

        print(script_local_time)
    except error:
        print(error)
        
sys.exit()


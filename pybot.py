import pyautogui
import os
import sys
import time
import configparser

running = True


def alerts():
    print("You've selected (1) Alerts.")
    menu()


def healer():
    print("You've selected (2) Healer.")
    menu()


def runemaker():
    print("You've selected (3) Runemaker.")
    menu()


def setup_client():
    print("You've selected (5) Setup new client.")
    menu()


def start():
    print("You've selected (0) START.")
    menu()


# MENU
def menu():
    time.sleep(3)
    os.system('cls')
    print("(1) Alerts")
    print("(2) Healer")
    print("(3) Runemaker")
    print("")
    print("(5) Setup new client")
    print("")
    print("(9) START")
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

menu()


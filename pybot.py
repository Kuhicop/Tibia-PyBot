import pyautogui
import os
import sys
import time
from tkinter import *
import threading
import configparser

running = True


class FakeConsole(Frame):
    def __init__(self, root, *args, **kargs):
        Frame.__init__(self, root, *args, **kargs)

        # white text on black background, for extra versimilitude
        self.text = Text(self, bg="black", fg="white")
        self.text.pack()

        # list of things not yet printed
        self.printQueue = []

        # one thread will be adding to the print queue,
        # and another will be iterating through it.
        # better make sure one doesn't interfere with the other.
        self.printQueueLock = threading.Lock()

        self.after(5, self.on_idle)

    # check for new messages every five milliseconds
    def on_idle(self):
        with self.printQueueLock:
            for msg in self.printQueue:
                self.text.insert(END, msg)
                self.text.see(END)
            self.printQueue = []
        self.after(5, self.on_idle)

    # print msg to the console
    def show(self, msg, sep="\n"):
        with self.printQueueLock:
            self.printQueue.append(str(msg) + sep)

def makeConsoles(amount):
    root = Tk()
    consoles = [FakeConsole(root) for n in range(amount)]
    for c in consoles:
        c.pack()
    threading.Thread(target=root.mainloop).start()
    return consoles


def alerts():
    print("You've selected (1) Alerts.")
    menu()


def healer():
    print("You've selected (2) Healer.")
    menu()


def runemaker_on():
    print("Making runes.")
    time.sleep(3)


def runemaker():
    print("You've selected (3) Runemaker.")
    thread1 = Thread(target=runemaker_on)
    thread1.start()
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


# DEFAULT ROUTINE #

a = makeConsoles(1)

a.show("This is Console 1")
a.show("I've got a lovely bunch of cocounts")
a.show("Here they are standing in a row")

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


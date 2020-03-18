from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import pdb
import copy
import time

paste_history = []
kb = Controller()


class Paste:
    def __init__(self, number=1):
        self.number = number - 1

    def paste_data(self):
        if not paste_history:
            return
        try:
            data = paste_history[self.number]
        except IndexError as e:
            print(e)
            return
        pyperclip.copy(data)

        kb.press(keyboard.Key.ctrl.value)
        kb.press("v")
        kb.release("v")
        kb.release(keyboard.Key.ctrl.value)


def paste_all():
    if not paste_history:
        return
    data = "\n".join(paste_history)
    pyperclip.copy(data)
    kb.press(keyboard.Key.ctrl.value)
    kb.press("v")
    kb.release("v")
    kb.release(keyboard.Key.ctrl.value)


def copy_data():
    paste_history.append(pyperclip.paste())
    print(pyperclip.paste())
    with open("clipboard_history.txt", "a") as data_file:
        data_file.write("\n")
        data_file.write(pyperclip.paste())

def clear_clipboard():
    paste_history = []


hotkeys = {"<ctrl>+c": copy_data, "<ctrl>+<alt>+v": paste_all, "<ctrl>+<alt>+0":clear_clipboard}
paste_hotkeys = {f"<ctrl>+{x}": Paste(x).paste_data for x in range(0, 10)}
hotkeys.update(paste_hotkeys)
with keyboard.GlobalHotKeys(hotkeys) as h:
    h.join()

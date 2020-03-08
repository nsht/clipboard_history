from pynput import keyboard
import pyperclip

# The currently active modifiers
current = set()


def on_press(key):
    try:
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.add(key)
            if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
                print("COMBO HIT!!!!!!")
                print(pyperclip.paste())
                with open("clipboard_history.txt", "a") as data_file:
                    data_file.write("\n")
                    data_file.write(pyperclip.paste())
    except AttributeError:
        print("special key {0} pressed".format(key))


def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        if key in current:
            current.remove(key)
    if key == keyboard.Key.esc:
        # Stop listener
        return False


COMBINATIONS = [
    {keyboard.Key.ctrl, keyboard.KeyCode(char="c")},
    {keyboard.Key.ctrl, keyboard.KeyCode(char="C")},
]


def on_triggered():  # define your function to be executed on hot-key press
    print(text_to_print)


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()

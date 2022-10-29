import random
import string
import time

import pyautogui
import win32api
import win32con


def generator_pass(t):
    # Включена ли клавиша NumLock
    num_status = win32api.GetKeyState(win32con.VK_NUMLOCK)
    if num_status == 1:
        password = ''
        for i in range(14):
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        print(password)
        return password
    else:
        return None


def press_key(password):
    if password is not None:
        # Удалить один символ
        pyautogui.press('backspace')
        time.sleep(0.2)
        pyautogui.typewrite(password)
        time.sleep(0.3)


if __name__ == '__main__':
    password = generator_pass()
    print(password)
    press_key(password)


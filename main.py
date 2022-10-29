import threading
import time

import keyboard
import os
import generator_pass as gp


def main(check):
    # Присвоеть текущее время в переменную t
    # t = time.time()
    if check:
        print(check)
        # keyboard.add_hotkey('ctrl+alt+num 3', lambda: gp.press_key(gp.generator_pass()))

        keyboard.add_hotkey(71, lambda: gp.press_key(gp.generator_pass(time.time())))  # 71
    else:
        print(check)
        # Остановить слежение за клавишами
        keyboard.unhook_all()

    # keyboard.wait()


# def key_listener():
#     # Запустить слушатель клавиш и выводить их DEC коды
#     while True:
#         try:
#             # Слушаем клавиши
#             key = keyboard.read_key()
#             # Выводим DEC коды нажатых клавиш
#             print(keyboard._pressed_events)
#         except KeyboardInterrupt:
#             # Если нажали Ctrl+C, то прерываем цикл
#             break
#
#     keyboard.wait()


if __name__ == '__main__':
    main(True)

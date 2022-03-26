import time

import pyautogui
from pynput.mouse import Button, Controller
from pynput.mouse import Events

mouse = Controller()
scroll = Events()
# TODO: drag and drop


class Mouse:
    def __init_(self):
        pass

    def left_click(self, delay=0.05):
        mouse.press(Button.left)
        time.sleep(delay)
        mouse.release(Button.left)

    def right_click(self, delay=0.05):
        mouse.press(Button.right)
        time.sleep(delay)
        mouse.release(Button.right)

    def middle_click(self, delay=0.05):
        mouse.press(Button.middle)
        time.sleep(delay)
        mouse.release(Button.middle)

    def scroll_up(self, count, delay=0.05):
        for i in range(count):
            mouse.scroll(0, 1)
            time.sleep(delay)

    def scroll_down(self, count, delay=0.05):
        for i in range(count):
            mouse.scroll(0, -1)
            time.sleep(delay)

# WIP
    # def move(self, to_x, to_y):
    #     pyautogui.moveTo(to_x, to_y)
    #
    # def drag(self, from_x, from_y, to_x, to_y):
    #
    #     self.left_click()

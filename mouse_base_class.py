import time

import pyautogui
from pynput.mouse import Button, Controller
from pynput.mouse import Events

mouse = Controller()
scroll = Events()
# TODO: drag and drop


class Mouse:
    def left_click_hold(self):
        mouse.press(Button.left)

    def left_click_release(self):
        mouse.release(Button.left)

    def left_click(self, delay=0):
        mouse.press(Button.left)
        time.sleep(delay)
        mouse.release(Button.left)

    def right_click(self, delay=0):
        mouse.press(Button.right)
        time.sleep(delay)
        mouse.release(Button.right)

    def middle_click(self, delay=0):
        mouse.press(Button.middle)
        time.sleep(delay)
        mouse.release(Button.middle)

    def scroll_up(self, count, delay=0):
        for i in range(count):
            mouse.scroll(0, 1)
            time.sleep(delay)

    def scroll_down(self, count, delay=0):
        for i in range(count):
            mouse.scroll(0, -1)
            time.sleep(delay)

    def move(self, to_x, to_y):
        pyautogui.moveTo(to_x, to_y)

    def drag(self, to_x, to_y):
        self.left_click_hold()
        self.move(to_x, to_y)
        self.left_click_release()


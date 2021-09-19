# Get key from dictionary in keys_dictionary

import ctypes
import time

import pynput
from pynput._util.win32 import SendInput

from keys_dictionary import keys


def get_key(key):
    """ This allows the user of the program to type for example 'left_control' or 'Left_Control' and still have it work.
    :param key: Grabs the corresponding hex code from the keys_dictionary, dictionary
    :return: Key hex code """
    return keys[key]


class KeyAction:
    def __init__(self, *key):
        """
        :param key: Can be multiple parameters, if you are simple holding a key, then pass one param like: KeyAction('A').down()
        Alternatively if you are using a method that uses multiple keys then pass more params like: KeyAction('A', 'B', 'C').multi_press(1) """
        if len(key) == 1:
            self.keys = get_key(key[0].upper())
        else:
            self.keys = []  # I'm a mother fucking list now
            for i in key:
                self.keys.append(get_key(i.upper()))

    @staticmethod
    def __key_down(key):
        extra = ctypes.c_ulong(0)
        ii_ = pynput._util.win32.INPUT_union()
        ii_.ki = pynput._util.win32.KEYBDINPUT(0, key, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
        x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    # Releases a keyboard key if it is currently pressed down
    @staticmethod
    def __key_up(key):
        extra = ctypes.c_ulong(0)
        ii_ = pynput._util.win32.INPUT_union()
        ii_.ki = pynput._util.win32.KEYBDINPUT(0, key, 0x0008 | 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
        x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


    def __key_hold(self, key, seconds):
        self.__key_down(key)
        time.sleep(seconds)
        self.__key_up(key)

    def down(self):
        """ Holds a key down
        :return: none """
        self.__key_down(self.keys)

    def up(self):
        """ Releases a key
        :return: none """
        self.__key_up(self.keys)

    def hold(self, hold_time):
        """ Presses a key, waits, then releases it
        :param hold_time: Time to wait before releasing the key
        :return: none """
        self.__key_hold(self.keys, hold_time)

    def combo(self, hold_key, combo_key):
        """ Holds the first key before pressing the second key, then releases the first key.
        :param hold_key: Key to hold before pressing the combo_key
        :param combo_key: Key to press in while holding the hold_key """
        self.__key_down(get_key(hold_key.upper()))
        self.__key_hold(get_key(combo_key.upper()), 0.1)
        self.__key_up(get_key(hold_key.upper()))

    def repeat_input(self, repeats, delay):
        for i in range(repeats):
            self.__key_hold(self.keys, delay)

    # Helper function to press keys in succession
    def sequential_press(self, delay):
        """ Presses multiple keys in sequence
        :param delay: Time in seconds to wait between key presses
        :return: none """
        for i in self.keys:
            self.__key_down(i)
            time.sleep(delay)
            self.__key_up(i)

    def multi_press(self, delay):
        for i in self.keys:
            self.__key_down(i)

        time.sleep(delay)

        for i in self.keys:
            self.__key_up(i)
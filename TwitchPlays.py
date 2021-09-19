# Written by DougDoug (DougDoug on Youtube, DougDougW on Twitch)

# Hello!
# This file contains the main logic to process Twitch chat and convert it to game commands.
# All sections that you need to update are labeled with a "TODO" comment.
# The source code primarily comes from:
    # Wituz's "Twitch Plays" tutorial: http://www.wituz.com/make-your-own-twitch-plays-stream.html
    # PythonProgramming's "Python Plays GTA V" tutorial: https://pythonprogramming.net/direct-input-game-python-plays-gta-v/

# There are 2 other files needed to run this code:
    # TwitchPlays_AccountInfo.py is where you put your Twitch username and OAuth token. This is to keep your account details separated from the main source code.
    # TwitchPlays_Connection.py is the code that actually connects to Twitch. You should not modify this file.

# Disclaimer: 
    # This code is NOT optimized or well-organized. I am not a Python programmer.
    # I created a simple version that works quickly, and I'm sharing it for educational purposes.

###############################################
# Import and define our functions / key codes to send key commands

# General imports
import time
import subprocess
import ctypes
import random
import string

# Twitch imports
import pynput

import TwitchPlays_Connection
from TwitchPlays_AccountInfo import TWITCH_USERNAME, TWITCH_OAUTH_TOKEN

# Controller imports
import pyautogui
from pynput.mouse import Button, Controller

# Data imports
from keys_dictionary import keys

SendInput = ctypes.windll.user32.SendInput


# Get key from dictionary in keys_dictionary
def get_key(key):
    """ This allows the user of the program to type for example 'left_control' or 'Left_Control' and still have it work.
    :param key: Grabs the corresponding hex code from the keys_dictionary, dictionary
    :return:
    """
    return keys[key].upper()

# KEY PRESS NOTES
# The standard "Twitch Plays" tutorial key commands do NOT work in DirectX games (they only work in general windows applications)
# Instead, we use DirectX key codes and input functions below.
# This DirectX code is partially sourced from: https://stackoverflow.com/questions/53643273/how-to-keep-pynput-and-ctypes-from-clashing


# Class call syntax: KeyAction(key).function(param)
class KeyAction:
    def __init__(self, *key):
        """
        :param key: Can be multiple parameters, if you are simple holding a key, then pass one param like: KeyAction('A').down()
        Alternatively if you are using a method that uses multiple keys then pass more params like: KeyAction('A', 'B', 'C').multi_press(1) """
        if len(key) == 1:
            self.keys = get_key(key)
        else:
            self.keys = []  # I'm a mother fucking list now
            for i in key:
                self.keys = self.keys(i)

    # Presses and permanently holds down a keyboard key
    def down(self):
        """ Holds a key down
        :return: none """
        extra = ctypes.c_ulong(0)
        ii_ = pynput._util.win32.INPUT_union()
        ii_.ki = pynput._util.win32.KEYBDINPUT(0, self.keys, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
        x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    # Releases a keyboard key if it is currently pressed down
    def up(self):
        """ Releases a key
        :return: none """
        extra = ctypes.c_ulong(0)
        ii_ = pynput._util.win32.INPUT_union()
        ii_.ki = pynput._util.win32.KEYBDINPUT(0, self.keys, 0x0008 | 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
        x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    # Helper method. Holds down a key for the specified number of seconds, then releases it.
    def hold(self, seconds):
        self.down()
        time.sleep(seconds)
        self.up()

    def repeat(self, times, seconds):
        for i in range(times):
            self.hold(seconds)

    # Helper function to press keys in succession
    def multi_press(self, seconds):
        """ Presses multiple keys in sequence
        :param seconds: Time in seconds to wait between key presses
        :return: none """
        for i in self.keys:
            KeyAction(i).down()
            time.sleep(seconds)
            KeyAction(i).up()


# Helper function. Holds control, presses the key and releases control.
def ctrl(key):
    """ First holds down the LEFT_CONTROL key, then presses a key for 0.1 seconds, then releases the LEFT_CONTROL key.
    :param key: Key to press while holding LEFT_CONTROL
    :return: none """
    KeyAction('LEFT_CONTROL').down()
    KeyAction(key).hold(0.1)
    KeyAction('LEFT_CONTROL').up()


# Helper function. Holds shift, presses the key and releases shift.
def shift(key):
    """ First holds down the LEFT_SHIFT key, then presses a key for 0.1 seconds, then releases the LEFT_SHIFT key.
    :param key: Key to press while holding LEFT_SHIFT
    :return: none """
    KeyAction('LEFT_SHIFT').down()
    KeyAction(key).hold(0.1)
    KeyAction('LEFT_SHIFT').up()


# Mouse Controller, using pynput
    # pynput.mouse functions are found at: https://pypi.org/project/pynput/
    # NOTE: pyautogui's click() function permanently holds down in DirectX, so I used pynput instead for mouse instead.
mouse = Controller()

# An optional countdown before the code actually starts running, so you have time to load up the game before messages are processed.
# TODO: Set the "countdown" variable to whatever countdown length you want.
countdown = 5 # The number of seconds before the code starts running
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

# Connects to your twitch chat, using your username and OAuth token.
# TODO: make sure that your Twitch username and OAuth token are added to the "TwitchPlays_AccountInfo.py" file
t = TwitchPlays_Connection.Twitch()
t.twitch_connect(TWITCH_USERNAME, TWITCH_OAUTH_TOKEN)

# Main loop, will constantly check input from chat
while True:
    # Check for new chat messages
    new_messages = t.twitch_recieve_messages()
    if not new_messages:
        # No new messages. 
        continue
    else:
        try:  
            for message in new_messages:
                # We got a new message! Get the message and the username.
                msg = message['message'].lower()
                username = message['username'].lower()
                
                # TODO:
                # Now that you have a chat message, this is where you add your game logic.
                # Use the "PressKeyPynput(KEYCODE)" function to press and hold down a keyboard key.
                # Use the "ReleaseKeyPynput(KEYCODE)" function to release a specific keyboard key.
                # Use the "PressAndHoldKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
                # Use "mouse.press(Button.left)" or "mouse.release(Button.left)" to press/release the mouse. Can use Button.right for right click.

                # I've added some example videogame logic code below:

                ###################################
                # Example GTA V Code 
                ###################################

                # If the chat message is "left", then hold down the A key for 2 seconds
                if msg == 'left':
                    KeyAction('A').hold(2)

                # If the chat message is "right", then hold down the D key for 2 seconds
                if msg == 'right':
                    KeyAction('D').hold(2)

                # If message is "drive", then permanently hold down the W key
                if msg == 'drive':
                    KeyAction('S').up()  # release brake key first
                    KeyAction('W').down()  # start permanently driving

                # If message is "reverse", then permanently hold down the S key
                if msg == 'reverse':
                    KeyAction('W').up()  # release drive key first
                    KeyAction('S').hold(2)  # start permanently reversing

                # Release both the "drive" and "reverse" keys
                if msg == 'stop':
                    KeyAction('W').hold(2)
                    KeyAction('S').hold(2)

                # Press the spacebar for 0.7 seconds
                if msg == 'brake':
                    KeyAction('SPACE').hold(0.7)

                # Presses the left mouse button down for 1 second, then releases it
                if msg == 'shoot':
                    mouse.press(Button.left)
                    time.sleep(1)
                    mouse.release(Button.left)

                # Press multiple keys in succession
                if msg == 'tapitbaby':
                    KeyAction('A', 'B', 'C',).multi_press(0.5)

                # Press multiple keys in succession 2
                if msg == 'tapitbaby':
                    KeyAction('A', 'A', 'A').multi_press(0.1)
                    # or
                    KeyAction('A').repeat(5, 0.1)
 
                ###################################
                # Example Miscellaneous Code 
                ###################################

                # Clicks and drags the mouse upwards, using the Pyautogui commands.
                # NOTE: unfortunately, Pyautogui does not work in DirectX games like GTA V. It will work in all other environments (e.g. on your desktop)
                # If anyone finds a reliable way to move the mouse in DirectX games, please let me know!
                if msg == "drag mouse up":
                    pyautogui.drag(0, -50, 0.25, button='left')

                # Clicks and drags the mouse downwards, using the Pyautogui commands
                if msg == "drag mouse down":
                    pyautogui.drag(0, 50, 0.25, button='left')

                # Hold control press a key, then release
                if msg == "select all":
                    ctrl('A')
                elif msg == "copy":
                    ctrl('C')
                elif msg == "cut":
                    ctrl('X')
                elif msg == "paste":
                    ctrl('V')
                
                # Can use pyautogui.typewrite() to type messages from chat into the keyboard.
                # Here, if a chat message says "type ...", it will type out their text.
                if msg.startswith("type "): 
                    try:
                        typeMsg = msg[5:] # Ignore the "type " portion of the message
                        pyautogui.typewrite(typeMsg)
                    except:
                        # There was some issue typing the msg. Print it out, and move on.
                        print("Typing this particular message didn't work: " + msg)

                ####################################
                ####################################

        except:
            # There was some error trying to process this chat message. Simply move on to the next message.
            print('Encountered an exception while reading chat.')

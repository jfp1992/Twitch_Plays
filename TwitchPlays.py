"""
Written by DougDoug (DougDoug on Youtube, DougDoug on Twitch)

Refactored, Upgraded and Edited by jfp1992

Hello!

This file contains the main logic to process Twitch chat and convert it to game commands.
All sections that you need to update are labeled with a "TODO" comment.
The source code primarily comes from:
    Wituz's "Twitch Plays" tutorial: http://www.wituz.com/make-your-own-twitch-plays-stream.html
    PythonProgramming's "Python Plays GTA V" tutorial: https://pythonprogramming.net/direct-input-game-python-plays-gta-v/

There are 2 other files needed to run this code:
    TwitchPlays_AccountInfo.py is where you put your Twitch username and OAuth token. This is to keep your account details separated from the main source code.
    TwitchPlays_Connection.py is the code that actually connects to Twitch. You should not modify this file.

KEY PRESS NOTES
The standard "Twitch Plays" tutorial key commands do NOT work in DirectX games (they only work in general windows applications)
Instead, we use DirectX key codes and input functions below.
This DirectX code is partially sourced from: https://stackoverflow.com/questions/53643273/how-to-keep-pynput-and-ctypes-from-clashing

Mouse Controller, using pynput
    pynput.mouse functions are found at: https://pypi.org/project/pynput/
    NOTE: pyautogui's click() function permanently holds down in DirectX, so I used pynput instead for mouse instead."""

import time
from collections import Counter

import pyautogui

import TwitchPlays_Connection
from TwitchPlays_AccountInfo import TWITCH_USERNAME, TWITCH_OAUTH_TOKEN
from keys_base_class import KeyAction
# TODO: Set the "countdown" variable to whatever countdown length you want.
from mouse_base_class import Mouse

countdown = 2  # The number of seconds before the code starts running

while countdown > 0:
    print(f'Counting down: {countdown}')
    countdown -= 1
    time.sleep(1)

# Connects to your twitch chat, using your username and OAuth token.
# TODO: make sure that your Twitch username and OAuth token are added to the "TwitchPlays_AccountInfo.py" file
t = TwitchPlays_Connection.Twitch()
t.twitch_connect(TWITCH_USERNAME, TWITCH_OAUTH_TOKEN)

# Main loop, will constantly check input from chat
while True:
    new_messages = t.twitch_recieve_messages()
    if not new_messages:
        continue
    else:
        try:
            msg = Counter(new_messages).most_common(1)[0][0].lower()  # Finds the most common message in messages

            """
            TODO:
            Now that you have a chat message, this is where you add your game logic.

            Use "mouse.press(Button.left)" or "mouse.release(Button.left)" to press/release the mouse. Can use Button.right for right click."""

            # KeyAction('a').down()                                 Press and hold x key
            # KeyAction('a').up()                                   Release x key if down
            # KeyAction('a').hold(1)                                Press x key and hold x seconds
            # KeyAction('a').combo('left_control', 'c')             Press and hold x key, then press and release x key
            # KeyAction('a').repeat_input(5, 1)                     Repeat a key x times with x seconds in between
            # KeyAction('a', 'b', 'c', 'etc').sequential_press(1)   Press a sequence of keys with x seconds in between
            # KeyAction('a', 'b', 'c', 'etc').multi_press(0.1)      Press multiple keys at the same time then release after some delay (Note: this won't be perfect as there will be a few ms between)

            # I've added some example videogame logic code below:

            ######################
            # Example GTA V Code #
            ######################

            # If the chat message is "left", then hold down the A key for 2 seconds
            if msg == 'left':
                KeyAction('A').hold(2)

            # If the chat message is "right", then hold down the D key for 2 seconds
            if msg == 'right':
                KeyAction('d').hold(2)

            # If message is "drive", then permanently hold down the W key
            if msg == 'drive':
                KeyAction('s').up()  # release brake key first
                KeyAction('w').down()  # start permanently driving

            # If message is "reverse", then permanently hold down the S key
            if msg == 'reverse':
                KeyAction('w').up()  # release drive key first
                KeyAction('s').hold(2)  # start permanently reversing

            # Release both the "drive" and "reverse" keys
            if msg == 'stop':
                KeyAction('w').hold(2)
                KeyAction('s').hold(2)

            # Press the spacebar for 0.7 seconds
            if msg == 'brake':
                KeyAction('space').hold(0.7)

            # Presses the left mouse button down for 1 second, then releases it
            if msg == 'shoot':
                Mouse().left_click()

            ##################
            # Other examples #
            ##################

            # Press multiple keys in succession
            if msg == 'tapitbaby':
                KeyAction('a', 'a', 'a').sequential_press(0.5)

            # Press multiple keys in succession 2
            if msg == 'tapitbaby':
                KeyAction('a', 'a', 'a').sequential_press(0.1)
                # or
                KeyAction('a').repeat_input(3, 0.1)

            ###############################
            # Example Miscellaneous Code #
            ##############################

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
                KeyAction().combo('left_control', 'a')
            elif msg == "copy":
                KeyAction().combo('left_control', 'c')
            elif msg == "cut":
                KeyAction().combo('left_control', 'x')
            elif msg == "paste":
                KeyAction().combo('left_control', 'v')

            # Can use pyautogui.typewrite() to type messages from chat into the keyboard.
            # Here, if a chat message says "type ...", it will type out their text.
            if msg.startswith("type "):
                try:
                    typeMsg = msg[5:] # Ignore the "type " portion of the message
                    pyautogui.typewrite(typeMsg)
                except:
                    # There was some issue typing the msg. Print it out, and move on.
                    print("Typing this particular message didn't work: " + msg)
        except:
            # There was some error trying to process this chat message. Simply move on to the next message.
            print('Encountered an exception while reading chat.')

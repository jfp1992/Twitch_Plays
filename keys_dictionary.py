#####################################################################################################################################
# DIRECTX KEY CODES                                                                                                                 #
# These codes identify each key on the keyboard.                                                                                    #
# Note that DirectX's key codes (or "scan codes") are NOT the same as Windows virtual hex key codes.                                #
#   DirectX codes are found at: https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-6.0/aa299374(v=vs.60) #
#####################################################################################################################################
keys = {
    # Letters
    'Q':                0x10,
    'W':                0x11,
    'E':                0x12,
    'R':                0x13,
    'T':                0x14,
    'Y':                0x15,
    'U':                0x16,
    'I':                0x17,
    'O':                0x18,
    'P':                0x19,
    'A':                0x1E,
    'S':                0x1F,
    'D':                0x20,
    'F':                0x21,
    'G':                0x22,
    'H':                0x23,
    'J':                0x24,
    'K':                0x25,
    'L':                0x26,
    'Z':                0x2C,
    'X':                0x2D,
    'C':                0x2E,
    'V':                0x2F,
    'B':                0x30,
    'N':                0x31,
    'M':                0x32,

    # Numbers
    'ONE':              0x02,
    'TWO':              0x03,
    'THREE':            0x04,
    'FOUR':             0x05,
    'FIVE':             0x06,
    'SIX':              0x07,
    'SEVEN':            0x08,
    'EIGHT':            0x09,
    'NINE':             0x0A,
    'ZERO':             0x0B,

    # Miscellaneous
    'ESC':              0x01,
    'MINUS':            0x0C,
    'EQUALS':           0x0D,
    'BACKSPACE':        0x0E,
    'SEMICOLON':        0x27,
    'TAB':              0x0F,
    'CAPS':             0x3A,
    'ENTER':            0x1C,
    'LEFT_CONTROL':     0x1D,
    'LEFT_ALT':         0x38,
    'LEFT_SHIFT':       0x2A,
    'SPACE':            0x39,
    'DELETE':           0x53,
    'COMMA':            0x33,
    'PERIOD':           0x34,
    'BACKSLASH':        0x35,

    # Number Pad
    'NUMPAD_0':         0x52,
    'NUMPAD_1':         0x4F,
    'NUMPAD_2':         0x50,
    'NUMPAD_3':         0x51,
    'NUMPAD_4':         0x4B,
    'NUMPAD_5':         0x4C,
    'NUMPAD_6':         0x4D,
    'NUMPAD_7':         0x47,
    'NUMPAD_8':         0x48,
    'NUMPAD_9':         0x49,
    'NUMPAD_PLUS':      0x4E,
    'NUMPAD_MINUS':     0x4A,

    # Arrow keys
    'LEFT_ARROW':       0xCB,
    'RIGHT_ARROW':      0xCD,
    'UP_ARROW':         0xC8,
    'DOWN_ARROW':       0xD0,

    # Mouse
    'LEFT_MOUSE':       0x100,
    'RIGHT_MOUSE':      0x101,
    'MIDDLE_MOUSE':     0x102,
    'MOUSE3':           0x103,
    'MOUSE4':           0x104,
    'MOUSE5':           0x105,
    'MOUSE6':           0x106,
    'MOUSE7':           0x107,
    'MOUSE_WHEEL_UP':   0x108,
    'MOUSE_WHEEL_DOWN': 0x109
}
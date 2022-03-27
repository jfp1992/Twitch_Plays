"""
DIRECTX KEY CODES
These codes identify each key on the keyboard.
Note that DirectX's key codes (or "scan codes") are NOT the same as Windows virtual hex key codes.
DirectX codes are found at: https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-6.0/aa299374(v=vs.60)
"""

keys = {
    # Letters
    'A':                0x1E,
    'B':                0x30,
    'C':                0x2E,
    'D':                0x20,
    'E':                0x12,
    'F':                0x21,
    'G':                0x22,
    'H':                0x23,
    'I':                0x17,
    'J':                0x24,
    'K':                0x25,
    'L':                0x26,
    'M':                0x32,
    'N':                0x31,
    'O':                0x18,
    'P':                0x19,
    'Q':                0x10,
    'R':                0x13,
    'S':                0x1F,
    'T':                0x14,
    'U':                0x16,
    'V':                0x2F,
    'W':                0x11,
    'X':                0x2D,
    'Y':                0x15,
    'Z':                0x2C,

    # Numbers
    '1':                0x02,
    '2':                0x03,
    '3':                0x04,
    '4':                0x05,
    '5':                0x06,
    '6':                0x07,
    '7':                0x08,
    '8':                0x09,
    '9':                0x0A,
    '0':                0x0B,

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
    'NUM_0':            0x52,
    'NUM_1':            0x4F,
    'NUM_2':            0x50,
    'NUM_3':            0x51,
    'NUM_4':            0x4B,
    'NUM_5':            0x4C,
    'NUM_6':            0x4D,
    'NUM_7':            0x47,
    'NUM_8':            0x48,
    'NUM_9':            0x49,
    'NUM_PLUS':         0x4E,
    'NUM_MINUS':        0x4A,

    # Arrow keys
    'UP_ARROW':         0xC8,
    'DOWN_ARROW':       0xD0,
    'LEFT_ARROW':       0xCB,
    'RIGHT_ARROW':      0xCD,

    # Mouse
    'LEFT_MOUSE':       0x100,
    'RIGHT_MOUSE':      0x101,
    'MIDDLE_MOUSE':     0x102,
    'MOUSE_WHEEL_UP':   0x108,
    'MOUSE_WHEEL_DOWN': 0x109,
    'MOUSE3':           0x103,
    'MOUSE4':           0x104,
    'MOUSE5':           0x105,
    'MOUSE6':           0x106,
    'MOUSE7':           0x107

}


import ctypes
import pynput

_SendInput = ctypes.windll.user32.SendInput

_pause = 0

W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
X = 0x2D
SPACE = 0x39

def DIPressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    _SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def DIReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    _SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))




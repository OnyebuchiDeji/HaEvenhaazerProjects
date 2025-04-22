
#   From pywin32
from win32file import * #   Features CreateFileW, a function
from min32api import *  #   CloseHandle, Sleep etc.
from win32gui import *  #   GDI functions
from win32con import *  #   Constants like GENERIC_READ, etc.
from win32ui import *   #   Object Oriented Windows API objects.
import sys #    Used to exit th ecurrent process. One might also use ExitProcess(0), however sys.exit() is more Pythonic

#   Displaying a Warning

title = "! Warning !"
description = "You are currently seeing this message box for test purposes. Continue as you wish."


if MessageBox(description, title, MB_ICONWARNING | MB_YESNO) == IDNO:
    print("No Pressed")
    print("Exiting Process")
    sys.exit(0)
else:
    print("Yes Pressed")


title = "!! Last Warning !!"


print("Continuing... Finishing...")
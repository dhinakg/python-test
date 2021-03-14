from ast import Import


try:
    try:
        import Tkinter

        tkinter = Tkinter
    except ImportError:
        import tkinter
except ImportError:
    tkinter = None

import sys

print(sys.version)
print(sys.executable)
if tkinter:
    print(tkinter.Tcl().eval("info patchlevel"))
else:
    print("No tkinter available")

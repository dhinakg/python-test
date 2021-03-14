from ast import Import


try:
    import Tkinter
    tkinter = Tkinter
except ImportError:
    import tkinter

import sys
print(sys.version)
print(sys.executable)
print(tkinter.Tcl().eval('info patchlevel'))

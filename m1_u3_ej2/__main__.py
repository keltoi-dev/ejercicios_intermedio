# Practicando POO
# Germán Fraga

from tkinter import Tk
from vista import MasterWindow

if __name__ == "__main__":
    root = Tk()
    vista = MasterWindow(root)
    vista.base_window()
    root.mainloop()

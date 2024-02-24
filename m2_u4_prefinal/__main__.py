# Practicando POO
# Germán Fraga

from tkinter import Tk
import vista


class Controller:
    def __init__(self, root: object) -> None:
        self.root = root
        self.obj_view = vista.MasterWindow(self.root)


if __name__ == "__main__":
    root = Tk()
    view = Controller(root)
    view.obj_view.base_window()
    root.mainloop()

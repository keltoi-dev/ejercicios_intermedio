"""
main.py:
    Lanzador de la aplicacion.
"""

import vista

__author__ = "German Fraga"
__maintainer__ = "German Fraga"
__email__ = "gdfraga@gmail.com"
__copyright__ = "Copyright 2024"
__version__ = "0.2.6"

from tkinter import Tk
import vista


class Controller:
    def __init__(self, root: object) -> None:
        """
        Instancia la MasterWindow de la vista
        :param root: Objeto de Tk
        """
        self.root = root
        # Se instancia la vista
        self.obj_view = vista.MasterWindow(self.root)


# Verificacion que se inicia la applicacion desde este archivo
if __name__ == "__main__":
    root = Tk()
    # Instancia el controller
    view = Controller(root)
    # Llamado al modulo vista
    view.obj_view.base_window()
    root.mainloop()

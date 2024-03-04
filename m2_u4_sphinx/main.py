"""
main.py:
    Lanzador de la aplicación.
    Instancia a tkinter y mantiene la ventana abierta con el mainloop
"""

__author__ = "German Fraga"
__maintainer__ = "German Fraga"
__email__ = "gdfraga@gmail.com"
__copyright__ = "Copyright 2024"
__version__ = "0.2.7"

from tkinter import Tk
from vista import MasterWindow


class Controller:
    def __init__(self, root: object) -> None:
        """
        Instancia la MasterWindow de la vista

        :param root: Objeto de Tk
        """
        self.root = root
        # Se instancia la vista
        self.obj_view = MasterWindow(self.root)


# Verificación que se inicia la aplicación desde este archivo
if __name__ == "__main__":
    root = Tk()
    # Instancia el controller
    view = Controller(root)
    # Llamado al modulo vista
    view.obj_view.base_window()
    root.mainloop()

from tkinter import Tk
import vista


class Controlador:
    def __init__(self, root):
        self.root = root
        self.obj_vista = vista.VentanaPrincipal(self.root)
        self.obj_vista.ventana()


if __name__ == "__main__":
    window = Tk()
    vista = Controlador(window)
    window.mainloop()

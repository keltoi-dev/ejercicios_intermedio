from tkinter import Tk
import vista


class Controlador:
    def __init__(self, root):
        self.root = root
        self.obj_vista = vista.VentanaPrincipal(self.root)


if __name__ == "__main__":
    window = Tk()
    views = Controlador(window)
    views.obj_vista.ventana()
    window.mainloop()

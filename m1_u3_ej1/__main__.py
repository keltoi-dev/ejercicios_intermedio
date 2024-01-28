from tkinter import Tk
from vista import VentanaPrincipal

if __name__ == "__main__":
    window = Tk()
    vista = VentanaPrincipal(window)
    vista.ventana()
    window.mainloop()

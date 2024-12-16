from tkinter import *
from tkinter_app.interfaz import *

def main():
    # Crear la ventana principal
    raiz=Tk()
    raiz.wm_title("Cafetería")

    app=Interfaz(raiz)

    app.mainloop()

if __name__ == "__main__":
    main() 
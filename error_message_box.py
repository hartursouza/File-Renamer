from tkinter import Tk, messagebox


def show_error(message):
    """
    Exibe uma mensagem de erro em uma caixa de diálogo.
    """
    root = Tk()
    root.withdraw()
    messagebox.showerror("Erro", message)
    root.destroy()

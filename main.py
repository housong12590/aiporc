from tkinter import Tk, Label, LEFT, BOTTOM


class MainWindow(object):

    def __init__(self):
        self.tk = Tk()
        self.init_root()

    def init_root(self):
        self.tk.title('uiToPy')
        self.tk.geometry('400x300')
        self.tk.resizable(False, False)
        l = Label(self.tk, text="show", bg="green", font=("Arial", 12), width=5, height=2)
        l.pack(side=LEFT)

    def show(self):
        self.tk.mainloop()


if __name__ == '__main__':
    MainWindow().show()

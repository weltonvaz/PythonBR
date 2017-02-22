from tkinter import *

class Senha:
    def __init__(self, master=None):
        self.valor = IntVar
        self.valor = 0

        self.datauser = Frame(master)
        self.datauser["pady"] = 10
        self.datauser.pack()

        self.senha = Entry(self.datauser)
        self.senha["width"] = 25
        self.senha.grid(row=2, column=2)

        self.exibe = Checkbutton(self.datauser, var=self.valor, command=self.changepass)
        self.exibe["text"] = "Ocultar Senha"
        self.exibe.grid(row=3, column=2)

        def changepass(self):
            if self.valor == 1:
                self.valor.set(0)
            elif self.valor == 0:
                self.valor.set(1)
            while True:
                if self.valor == 1:
                    self.senha.configure(show="*")
                elif self.valor == 0:
                    self.senha,configure(show="")


inicio = Tk()
inicio.title("Senha")
inicio.geometry("300x250+525+275")
Senha(inicio)
inicio.mainloop()

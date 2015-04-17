import wx
import sqlite3

con = sqlite3.connect("cadastro.db3")
c = con.cursor()

def criar_tabela():
    c.execute('CREATE TABLE IF NOT EXISTS cliente(id integer primary key autoincrement, nome varchar(120) not null, idade integer)')
criar_tabela()


class MeuFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Cadastro de Clientes', size = (600, 300), style = wx.DEFAULT_FRAME_STYLE)
        self.painel = wx.Panel(self)
        self.painel.SetBackgroundColour('#B0C4DE')

        wx.StaticText(self.painel, 1, 'Codigo:', (15,15))
        wx.StaticText(self.painel, 2, 'Nome:', (15,40))
        wx.StaticText(self.painel, 3, 'Idade:', (15,65))


        self.id = wx.TextCtrl(self.painel,4,'',(60,12), (50, -1))
        self.nome = wx.TextCtrl(self.painel,5,'',(60,37), (350, -1))
        self.idade = wx.TextCtrl(self.painel,6,'',(60,62), (50, -1))

        wx.Button(self.painel, 7, 'Registrar', (50, 130))
        self.Bind(wx.EVT_BUTTON, self.OnReg, id=7)


    def OnReg(self, event):
        dlg = wx.MessageBox("Voce tem certeza que deseja salvar?", 'Mensagem', wx.YES_NO | wx.ICON_QUESTION)
        if (dlg == wx.YES):
            conec = sqlite3.connect('cadastro.db3')
            conn = conec.cursor()
            #conn.execute("INSERT INTO cliente(id) VALUES(null,?),"[self.id])
            conn.execute('INSERT INTO cliente (nome) VALUES(null,?),'[self.nome])
            conn.execute('INSERT INTO cliente (idade) VALUES(null,?),'[self.idade])
            conec.commit()
            if(dlg == wx.NO):
                self.Destroy()


if __name__ == '__main__':
    frame = wx.App()
    f = MeuFrame(parent=None, id= 999)
    f.Center()
    f.Show()
    frame.MainLoop()

import wx


class TwoTOU(wx.Frame):

    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, title=title, parent=parent)
        self.init_ui()

    def init_ui(self):
        self.SetSize(600, 600)

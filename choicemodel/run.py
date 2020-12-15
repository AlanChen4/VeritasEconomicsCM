import wx


class ChoiceModelFrame(wx.Frame):

    def __init__(self):
        super().__init__(None, title="Veritas Economics 2020")
        self.SetSize((1024, 840))


class ChoiceModelApp(wx.App):

    def __init__(self):
        super().__init__()
        self.frame = ChoiceModelFrame()
        self.frame.Show()


if __name__ == '__main__':
    app = ChoiceModelApp()
    app.MainLoop()

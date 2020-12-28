import wx


class TwoTOU(wx.Frame):

    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, title=title, parent=parent)
        self.init_ui()

    def init_ui(self):
        self.SetSize(600, 600)
        self.SetBackgroundColour('White')

        vbox = wx.BoxSizer(wx.VERTICAL)
        plans_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # status quo plan
        status_quo_sizer = wx.BoxSizer(wx.VERTICAL)
        status_quo_label = wx.StaticText(self, label='Status Quo')
        status_quo_sizer.Add(status_quo_label, proportion=1, flag=wx.ALL, border=10)

        status_quo_rate = wx.StaticText(self, label='Status Quo Rate ($/kWh)  $0.10')
        status_quo_sizer.Add(status_quo_rate, proportion=1, flag=wx.ALL, border=10)

        plans_sizer.Add(status_quo_sizer)

        vbox.Add(plans_sizer)
        self.SetSizer(vbox)


import wx


class StatusQuo(wx.Panel):

    def __init__(self, parent=None):
        super(StatusQuo, self).__init__(parent=parent)
        self.init_ui()

    def init_ui(self):
        status_quo_sizer = wx.BoxSizer(wx.VERTICAL)

        # Create label and rate
        status_quo_font = wx.Font(wx.FontInfo(10).Bold())
        status_quo_label = wx.StaticText(self, label='Status Quo')
        status_quo_label.SetFont(status_quo_font)

        status_quo_rate = wx.StaticText(self, label='Status Quo Rate ($/kWh)  $0.10')

        # Add label and rate to the sizer
        status_quo_sizer.Add(status_quo_label, flag=wx.ALL, border=10)
        status_quo_sizer.Add(status_quo_rate, flag=wx.ALL, border=10)

        self.SetSizer(status_quo_sizer)

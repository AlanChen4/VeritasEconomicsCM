import wx


class Fixed(wx.Panel):

    def __init__(self, plan_title, parent=None):
        super(Fixed, self).__init__(parent=parent)
        self.init_ui(plan_title)

    def init_ui(self, plan_title):
        root_sizer = wx.BoxSizer(wx.VERTICAL)

        fixed_font = wx.Font(wx.FontInfo(10).Bold())
        fixed_label = wx.StaticText(self, label=f'Fixed Bill {plan_title}')
        fixed_label.SetFont(fixed_font)
        root_sizer.Add(fixed_label, flag=wx.ALL, border=10)

        premium_sizer = wx.BoxSizer(wx.HORIZONTAL)
        premium_label = wx.StaticText(self, size=(150, 20), label='Premium (%)')
        premium_rate = wx.ComboBox(self, choices=[
            '2%', '5%', '15%'
        ])

        premium_sizer.Add(premium_label, flag=wx.ALL, border=10)
        premium_sizer.Add(premium_rate, flag=wx.ALL, border=10)

        contract_sizer = wx.BoxSizer(wx.HORIZONTAL)
        contract_label = wx.StaticText(self, size=(150,20), label='Contract Length')
        contract_length = wx.ComboBox(self, choices=[
            '1 year', '2 years', '3 years'
        ])

        contract_sizer.Add(contract_label, flag=wx.ALL, border=10)
        contract_sizer.Add(contract_length, flag=wx.ALL, border=10)

        root_sizer.Add(premium_sizer)
        root_sizer.Add(contract_sizer)

        self.SetSizer(root_sizer)

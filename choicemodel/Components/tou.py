import wx


class TOU(wx.Panel):

    def __init__(self, plan_title, parent=None):
        super(TOU, self).__init__(parent=parent)
        self.init_ui(plan_title)

    def init_ui(self, plan_title):
        root_sizer = wx.BoxSizer(wx.VERTICAL)

        options_sizer = wx.BoxSizer(wx.VERTICAL)

        # Create title label
        title_font = wx.Font(wx.FontInfo(10).Bold())
        title_label = wx.StaticText(self, label=f'Time-of-Use (TOU) {plan_title}')
        title_label.SetFont(title_font)

        # Create labels
        off_peak_price_label = wx.StaticText(self, label='Off-Peak Price   ($k/Wh)', size=(150, 20))
        peak_price_label = wx.StaticText(self, label='Peak Price   ($k/Wh)', size=(150, 20))
        peak_period_label = wx.StaticText(self, label='Peak Period', size=(150, 20))
        peak_season_label = wx.StaticText(self, label='Peak Season', size=(150, 20))

        # Create inputs
        self.off_peak_price_input = wx.ComboBox(self, choices=[
            '$0.03', '$0.04', '$0.05', '$0.06', '$0.07', '$0.08', '$0.09',
        ])
        self.peak_price_input = wx.ComboBox(self, choices=[
            '$0.12', '$0.13', '$0.14', '$0.15', '$0.16', '$0.17', '$0.18',
            '$0.19', '$0.20', '$0.21', '$0.22', '$0.23', '$0.24', '$0.25',
            '$0.26', '$0.27', '$0.28', '$0.29', '$0.30', '$0.31', '$0.32',
            '$0.33', '$0.34', '$0.35', '$0.37', '$0.38', '$0.39', '$0.40',
            '$0.41', '$0.42', '$0.43', '$0.44', '$0.45'
        ])
        self.peak_period_input = wx.ComboBox(self, choices=[
            '(2 hours) 5PM to 7PM',
            '(3 hours) 2PM to 5PM',
            '(3 hours) 3PM to 6PM',
            '(3 hours) 4PM to 7PM',
            '(4 hours) 2PM to 6PM',
            '(6 hours) 2PM to 8PM'
        ])
        self.peak_season_input = wx.ComboBox(self, choices=[
            'Summer', 'Summer and Winter'
        ])

        # Create sizer for each options
        off_peak_price_sizer = wx.BoxSizer(wx.HORIZONTAL)
        peak_price_sizer = wx.BoxSizer(wx.HORIZONTAL)
        peak_period_sizer = wx.BoxSizer(wx.HORIZONTAL)
        peak_season_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add labels and input to each respective sizer
        off_peak_price_sizer.Add(off_peak_price_label, border=10, flag=wx.ALL)
        off_peak_price_sizer.Add(self.off_peak_price_input, border=10, flag=wx.ALL)
        peak_price_sizer.Add(peak_price_label, border=10, flag=wx.ALL)
        peak_price_sizer.Add(self.peak_price_input, border=10, flag=wx.ALL)
        peak_period_sizer.Add(peak_period_label, border=10, flag=wx.ALL)
        peak_period_sizer.Add(self.peak_period_input, border=10, flag=wx.ALL)
        peak_season_sizer.Add(peak_season_label, border=10, flag=wx.ALL)
        peak_season_sizer.Add(self.peak_season_input, border=10, flag=wx.ALL)

        # Add each sizer to the options_sizer
        options_sizer.Add(off_peak_price_sizer)
        options_sizer.Add(peak_price_sizer)
        options_sizer.Add(peak_period_sizer)
        options_sizer.Add(peak_season_sizer)

        root_sizer.Add(title_label, border=10, flag=wx.ALL)
        root_sizer.Add(options_sizer)
        self.SetSizer(root_sizer)

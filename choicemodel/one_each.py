import wx


class OneEach(wx.Frame):

    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, title=title, parent=parent)
        self.SetBackgroundColour('white')
        self.init_ui()

    def init_ui(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        # plans sizer
        plans_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # status quo
        status_quo_sizer = wx.BoxSizer(wx.VERTICAL)
        status_quo_label = wx.StaticText(self, label='Status Quo')
        status_quo_sizer.Add(status_quo_label, flag=wx.ALL, border=10)
        status_quo_rate = wx.StaticText(self, label='Status Quo Rate ($/kWh)  $0.10')
        status_quo_sizer.Add(status_quo_rate, flag=wx.ALL, border=10)

        # time of use plan
        tou_sizer = wx.BoxSizer(wx.VERTICAL)
        tou_label = wx.StaticText(self, label='Time-of-Use (TOU) A')
        tou_sizer.Add(tou_label, proportion=1, flag=wx.ALL, border=10)

        # off peak price
        off_peak_sizer = wx.BoxSizer(wx.HORIZONTAL)
        off_peak_label = wx.StaticText(self, label='Off-Peak Price')
        off_peak_sizer.Add(off_peak_label, proportion=1, flag=wx.ALL, border=10)
        off_peak_price = wx.ComboBox(self, value='SELECT', choices=[
            'Price A',
            'Price B',
            'Price C'
        ])
        off_peak_sizer.Add(off_peak_price, proportion=1, flag=wx.ALL, border=10)
        tou_sizer.Add(off_peak_sizer)

        # peak price
        peak_price_sizer = wx.BoxSizer(wx.HORIZONTAL)
        peak_label = wx.StaticText(self, label='Peak Price')
        peak_price_sizer.Add(peak_label, proportion=1, flag=wx.ALL, border=10)
        peak_price = wx.ComboBox(self, value='SELECT', choices=[
            'Price A',
            'Price B',
            'Price C'
        ])
        peak_price_sizer.Add(peak_price, proportion=1, flag=wx.ALL, border=10)
        tou_sizer.Add(peak_price_sizer)

        # peak period
        peak_period_sizer = wx.BoxSizer(wx.HORIZONTAL)
        peak_period_label = wx.StaticText(self, label='Peak Period')
        peak_period_sizer.Add(peak_period_label, proportion=1, flag=wx.ALL, border=10)
        peak_period = wx.ComboBox(self, value='SELECT', choices=[
            'Price A',
            'Price B',
            'Price C'
        ])
        peak_period_sizer.Add(peak_period, proportion=1, flag=wx.ALL, border=10)
        tou_sizer.Add(peak_period_sizer)

        # peak season
        peak_season_sizer = wx.BoxSizer(wx.HORIZONTAL)
        peak_season_label = wx.StaticText(self, label='Peak Season')
        peak_season_sizer.Add(peak_season_label, proportion=1, flag=wx.ALL, border=10)
        peak_season = wx.ComboBox(self, value='SELECT', choices=[
            'Price A',
            'Price B',
            'Price C'
        ])
        peak_season_sizer.Add(peak_season, proportion=1, flag=wx.ALL, border=10)
        tou_sizer.Add(peak_season_sizer)

        # Fixed Plan
        fixed_sizer = wx.BoxSizer(wx.VERTICAL)
        fixed_label = wx.StaticText(self, label='Fixed Bill A')
        fixed_sizer.Add(fixed_label, flag=wx.ALL, border=10)

        premium_sizer = wx.BoxSizer(wx.HORIZONTAL)
        premium_label = wx.StaticText(self, label='Premium (%)')
        premium_rate = wx.ComboBox(self, choices=['Some %'])
        premium_sizer.Add(premium_label, flag=wx.ALL, border=10)
        premium_sizer.Add(premium_rate, flag=wx.ALL, border=10)
        fixed_sizer.Add(premium_sizer)

        contract_sizer = wx.BoxSizer(wx.HORIZONTAL)
        contract_label = wx.StaticText(self, label='Contract Length')
        contract_length = wx.ComboBox(self, choices=['Some Length'])
        contract_sizer.Add(contract_label, flag=wx.ALL, border=10)
        contract_sizer.Add(contract_length, flag=wx.ALL, border=10)
        fixed_sizer.Add(contract_sizer)

        # Add to plans sizer
        plans_sizer.Add(status_quo_sizer)
        plans_sizer.Add(tou_sizer)
        plans_sizer.Add(fixed_sizer)

        # results label
        results_label = wx.StaticText(self, label='Results - Predictions of Potential Market Size')

        # calculate service
        calculate_sizer = wx.BoxSizer(wx.HORIZONTAL)
        calculate_service_label = wx.StaticText(self, label='Potential Market Size')
        calculate_sizer.Add(calculate_service_label, flag=wx.ALL, border=10)

        # service territory
        service_sizer = wx.BoxSizer(wx.VERTICAL)
        service_label = wx.StaticText(self, label='Service Territory')
        service_button = wx.Button(self, label='Calculate')
        service_sizer.Add(service_label)
        service_sizer.Add(service_button, flag=wx.ALL, border=10)
        calculate_sizer.Add(service_sizer, flag=wx.LEFT, border=20)

        # zip code
        zip_sizer = wx.BoxSizer(wx.VERTICAL)
        zip_label = wx.StaticText(self, label='By Zip Code')
        zip_button = wx.Button(self, label='Calculate')
        zip_sizer.Add(zip_label)
        zip_sizer.Add(zip_button, flag=wx.ALL, border=10)
        calculate_sizer.Add(zip_sizer, flag=wx.LEFT, border=20)

        # Add components to main sizer
        vbox.Add(plans_sizer)
        vbox.Add(results_label, flag=wx.ALL, border=10)
        vbox.Add(calculate_sizer)

        vbox.SetSizeHints(self)
        self.SetSizer(vbox)

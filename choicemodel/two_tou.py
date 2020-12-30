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

        # time of use A plan
        tou_a_sizer = wx.BoxSizer(wx.VERTICAL)
        tou_a_label = wx.StaticText(self, label='Time-of-Use (TOU) A')
        tou_a_sizer.Add(tou_a_label, proportion=1, flag=wx.ALL, border=10)

        plans_sizer.Add(tou_a_sizer)

        # off peak price
        off_peak_sizer_a = wx.BoxSizer(wx.HORIZONTAL)
        off_peak_label_a = wx.StaticText(self, label='Off-Peak Price')
        off_peak_sizer_a.Add(off_peak_label_a, proportion=1, flag=wx.ALL, border=10)
        off_peak_price_a = wx.ComboBox(self, value='SELECT', choices=[
            'Price A',
            'Price B',
            'Price C'
        ])
        off_peak_sizer_a.Add(off_peak_price_a, proportion=1, flag=wx.ALL, border=10)
        tou_a_sizer.Add(off_peak_sizer_a)

        # peak price
        peak_price_sizer_a = wx.BoxSizer(wx.HORIZONTAL)
        peak_label_a = wx.StaticText(self, label='Peak Price')
        peak_price_sizer_a.Add(peak_label_a, proportion=1, flag=wx.ALL, border=10)
        peak_price = wx.ComboBox(self, value='SELECT', choices=[
            'Price A',
            'Price B',
            'Price C'
        ])
        peak_price_sizer_a.Add(peak_price, proportion=1, flag=wx.ALL, border=10)
        tou_a_sizer.Add(peak_price_sizer_a)

        # peak period
        peak_period_sizer_a = wx.BoxSizer(wx.HORIZONTAL)
        peak_period_label_a = wx.StaticText(self, label='Peak Period')
        peak_period_sizer_a.Add(peak_period_label_a, proportion=1, flag=wx.ALL, border=10)
        peak_period_a = wx.ComboBox(self, value='SELECT', choices=[
            'Price A',
            'Price B',
            'Price C'
        ])
        peak_period_sizer_a.Add(peak_period_a, proportion=1, flag=wx.ALL, border=10)
        tou_a_sizer.Add(peak_period_sizer_a)

        # peak season
        peak_season_sizer_a = wx.BoxSizer(wx.HORIZONTAL)
        peak_season_label_a = wx.StaticText(self, label='Peak Season')
        peak_season_sizer_a.Add(peak_season_label_a, proportion=1, flag=wx.ALL, border=10)
        peak_season_a = wx.ComboBox(self, value='SELECT', choices=[
            'Price A',
            'Price B',
            'Price C'
        ])
        peak_season_sizer_a.Add(peak_season_a, proportion=1, flag=wx.ALL, border=10)
        tou_a_sizer.Add(peak_season_sizer_a)

        # time of use B plan
        tou_b_sizer = wx.BoxSizer(wx.VERTICAL)
        tou_b_label = wx.StaticText(self, label='Time-of-Use (TOU) B')
        tou_b_sizer.Add(tou_b_label, proportion=1, flag=wx.ALL, border=10)

        plans_sizer.Add(tou_b_sizer)

        # off peak price
        off_peak_sizer_b = wx.BoxSizer(wx.HORIZONTAL)
        off_peak_label_b = wx.StaticText(self, label='Off-Peak Price')
        off_peak_sizer_b.Add(off_peak_label_b, proportion=1, flag=wx.ALL, border=10)
        off_peak_price_b = wx.ComboBox(self, value='SELECT', choices=[
            'Price A',
            'Price B',
            'Price C'
        ])
        off_peak_sizer_b.Add(off_peak_price_b, proportion=1, flag=wx.ALL, border=10)
        tou_b_sizer.Add(off_peak_sizer_b)

        # peak price
        peak_price_sizer_b = wx.BoxSizer(wx.HORIZONTAL)
        peak_label_b = wx.StaticText(self, label='Peak Price')
        peak_price_sizer_b.Add(peak_label_b, proportion=1, flag=wx.ALL, border=10)
        peak_price = wx.ComboBox(self, value='SELECT', choices=[
            'Price A',
            'Price B',
            'Price C'
        ])
        peak_price_sizer_b.Add(peak_price, proportion=1, flag=wx.ALL, border=10)
        tou_b_sizer.Add(peak_price_sizer_b)

        # peak period
        peak_period_sizer_b = wx.BoxSizer(wx.HORIZONTAL)
        peak_period_label_b = wx.StaticText(self, label='Peak Period')
        peak_period_sizer_b.Add(peak_period_label_b, proportion=1, flag=wx.ALL, border=10)
        peak_period_b = wx.ComboBox(self, value='SELECT', choices=[
            'Price A',
            'Price B',
            'Price C'
        ])
        peak_period_sizer_b.Add(peak_period_b, proportion=1, flag=wx.ALL, border=10)
        tou_b_sizer.Add(peak_period_sizer_b)

        # peak season
        peak_season_sizer_b = wx.BoxSizer(wx.HORIZONTAL)
        peak_season_label_b = wx.StaticText(self, label='Peak Season')
        peak_season_sizer_b.Add(peak_season_label_b, proportion=1, flag=wx.ALL, border=10)
        peak_season_b = wx.ComboBox(self, value='SELECT', choices=[
            'Price A',
            'Price B',
            'Price C'
        ])
        peak_season_sizer_b.Add(peak_season_b, proportion=1, flag=wx.ALL, border=10)
        tou_b_sizer.Add(peak_season_sizer_b)

        # Spacer between calculate buttons
        results_spacer_sizer = wx.BoxSizer(wx.HORIZONTAL)
        results_spacer = wx.StaticText(self, label='Results - Predictions of Potential Market Size')
        results_spacer_sizer.Add(results_spacer, flag=wx.ALL, border=10)

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

        # Add all components to the main sizer in order
        vbox.Add(plans_sizer)
        vbox.Add(results_spacer_sizer)
        vbox.Add(calculate_sizer)

        vbox.SetSizeHints(self)
        self.SetSizer(vbox)


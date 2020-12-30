import wx


class TwoFixed(wx.Frame):

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

        # fixed A
        fixed_sizer_a = wx.BoxSizer(wx.VERTICAL)
        fixed_label_a = wx.StaticText(self, label='Fixed Bill A')
        fixed_sizer_a.Add(fixed_label_a, flag=wx.ALL, border=10)

        premium_sizer_a = wx.BoxSizer(wx.HORIZONTAL)
        premium_label_a = wx.StaticText(self, label='Premium (%)')
        premium_rate_a = wx.ComboBox(self, choices=['Some %'])
        premium_sizer_a.Add(premium_label_a, flag=wx.ALL, border=10)
        premium_sizer_a.Add(premium_rate_a, flag=wx.ALL, border=10)
        fixed_sizer_a.Add(premium_sizer_a)

        contract_sizer_a = wx.BoxSizer(wx.HORIZONTAL)
        contract_label_a = wx.StaticText(self, label='Contract Length')
        contract_length_a = wx.ComboBox(self, choices=['Some Length'])
        contract_sizer_a.Add(contract_label_a, flag=wx.ALL, border=10)
        contract_sizer_a.Add(contract_length_a, flag=wx.ALL, border=10)
        fixed_sizer_a.Add(contract_sizer_a)

        # fixed B
        fixed_sizer_b = wx.BoxSizer(wx.VERTICAL)
        fixed_label_b = wx.StaticText(self, label='Fixed Bill B')
        fixed_sizer_b.Add(fixed_label_b, flag=wx.ALL, border=10)

        premium_sizer_b = wx.BoxSizer(wx.HORIZONTAL)
        premium_label_b = wx.StaticText(self, label='Premium (%)')
        premium_rate_b = wx.ComboBox(self, choices=['Some %'])
        premium_sizer_b.Add(premium_label_b, flag=wx.ALL, border=10)
        premium_sizer_b.Add(premium_rate_b, flag=wx.ALL, border=10)
        fixed_sizer_b.Add(premium_sizer_b)

        contract_sizer_b = wx.BoxSizer(wx.HORIZONTAL)
        contract_label_b = wx.StaticText(self, label='Contract Length')
        contract_length_b = wx.ComboBox(self, choices=['Some Length'])
        contract_sizer_b.Add(contract_label_b, flag=wx.ALL, border=10)
        contract_sizer_b.Add(contract_length_b, flag=wx.ALL, border=10)
        fixed_sizer_b.Add(contract_sizer_b)

        # Add to plans sizer
        plans_sizer.Add(status_quo_sizer)
        plans_sizer.Add(fixed_sizer_a)
        plans_sizer.Add(fixed_sizer_b)

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

        # Add to main sizer
        vbox.Add(plans_sizer)
        vbox.Add(results_label, flag=wx.ALL, border=20)
        vbox.Add(calculate_sizer)

        vbox.SetSizeHints(self)
        self.SetSizer(vbox)

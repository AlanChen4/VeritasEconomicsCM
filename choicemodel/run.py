import wx

from .two_tou import TwoTOU


class ChoiceModelFrame(wx.Frame):

    def __init__(self):
        super().__init__(None, title="Veritas Economics")
        self.SetSize((1000, 600))
        self.panel = wx.Panel(self)
        self.init_ui()

    def init_ui(self):
        self.panel.SetBackgroundColour('cream')

        vbox = wx.BoxSizer(wx.VERTICAL)

        plan_type_sizer = wx.BoxSizer(wx.HORIZONTAL)
        plan_type_label = wx.StaticText(self.panel, label='Plan Type:')
        plan_type_input = wx.ComboBox(self.panel, choices=['average plan', 'amazing plan', 'terrible plan'])
        plan_type_sizer.Add(plan_type_label, flag=wx.ALL, border=10)
        plan_type_sizer.Add(plan_type_input, proportion=1, flag=wx.ALL, border=10)
        vbox.Add(plan_type_sizer, flag=wx.RIGHT | wx.EXPAND)

        cost_one_sizer = wx.BoxSizer(wx.HORIZONTAL)
        cost_one_label = wx.StaticText(self.panel, label='Cost One:')
        cost_one_input = wx.TextCtrl(self.panel)
        cost_one_sizer.Add(cost_one_label, flag=wx.ALL, border=10)
        cost_one_sizer.Add(cost_one_input, proportion=1, flag=wx.ALL, border=10)
        vbox.Add(cost_one_sizer, flag=wx.RIGHT | wx.EXPAND)

        cost_two_sizer = wx.BoxSizer(wx.HORIZONTAL)
        cost_two_label = wx.StaticText(self.panel, label='Cost One:')
        cost_two_input = wx.TextCtrl(self.panel)
        cost_two_sizer.Add(cost_two_label, flag=wx.ALL, border=10)
        cost_two_sizer.Add(cost_two_input, proportion=1, flag=wx.ALL, border=10)
        vbox.Add(cost_two_sizer, flag=wx.RIGHT | wx.EXPAND)

        cost_three_sizer = wx.BoxSizer(wx.HORIZONTAL)
        cost_three_label = wx.StaticText(self.panel, label='Cost One:')
        cost_three_input = wx.TextCtrl(self.panel)
        cost_three_sizer.Add(cost_three_label, flag=wx.ALL, border=10)
        cost_three_sizer.Add(cost_three_input, proportion=1, flag=wx.ALL, border=10)
        vbox.Add(cost_three_sizer, flag=wx.RIGHT | wx.EXPAND)

        calculate_sizer = wx.BoxSizer(wx.HORIZONTAL)
        calculate_button = wx.Button(self.panel, label="Calculate Plan Rate")
        calculate_button.Bind(wx.EVT_BUTTON, self.calculate_plan)
        calculate_sizer.Add(calculate_button, proportion=1, flag=wx.ALL, border=10)
        vbox.Add(calculate_sizer, flag=wx.ALL | wx.EXPAND)

        two_time_plans_sizer = wx.BoxSizer(wx.HORIZONTAL)
        two_time_plans_button = wx.Button(self.panel, label="Two Time-of-Use (TOU) Plans")
        two_time_plans_button.Bind(wx.EVT_BUTTON, self.calculate_two_tou)
        two_time_plans_sizer.Add(two_time_plans_button, proportion=1, flag=wx.ALL, border=10)
        vbox.Add(two_time_plans_sizer, flag=wx.ALL | wx.EXPAND)

        self.panel.SetSizer(vbox)

    @staticmethod
    def calculate_plan(self, *args):
        graph_frame = wx.Frame(None)
        graph_panel = wx.Panel(graph_frame)
        graph_panel.SetBackgroundColour('white')
        graph_label = wx.StaticText(graph_panel, label='This is a graph')
        graph_frame.Show()

    def calculate_two_tou(self, *args):
        two_tou_frame = TwoTOU(title="Two TOU",
                               parent=wx.GetTopLevelParent(self))
        two_tou_frame.Show()


class ChoiceModelApp(wx.App):

    def __init__(self):
        super().__init__()
        self.frame = ChoiceModelFrame()
        self.frame.Show()


def run():
    app = ChoiceModelApp()
    app.MainLoop()

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

import wx

from .one_each import OneEach
from .two_fixed import TwoFixed
from .two_tou import TwoTOU


class ChoiceModelFrame(wx.Frame):

    def __init__(self):
        super().__init__(None, title="Veritas Economics")
        self.init_ui()

    def init_ui(self):
        self.SetBackgroundColour('cream')

        vbox = wx.BoxSizer(wx.VERTICAL)

        options_sizer = wx.BoxSizer(wx.HORIZONTAL)

        one_each_button = wx.Button(self, label="One Fixed One TOU")
        one_each_button.Bind(wx.EVT_BUTTON, self.calculate_one_each)
        options_sizer.Add(one_each_button, border=10, proportion=1, flag=wx.ALL | wx.EXPAND)

        two_fixed_button = wx.Button(self, label="Two Fixed Plans")
        two_fixed_button.Bind(wx.EVT_BUTTON, self.calculate_two_fixed)
        options_sizer.Add(two_fixed_button, border=10, proportion=1,  flag=wx.ALL | wx.EXPAND)

        two_time_button = wx.Button(self, label="Two Time-of-Use (TOU) Plans")
        two_time_button.Bind(wx.EVT_BUTTON, self.calculate_two_tou)
        options_sizer.Add(two_time_button, border=10, proportion=1, flag=wx.ALL | wx.EXPAND)

        vbox.Add(options_sizer, flag=wx.ALL | wx.EXPAND)
        vbox.SetSizeHints(self)
        self.SetSizer(vbox)

    def calculate_one_each(self, *args):
        one_each_frame = OneEach(title="One TOU and One Fixed",
                                 parent=wx.GetTopLevelParent(self))
        one_each_frame.Show()

    def calculate_two_fixed(self, *args):
        two_fixed_frame = TwoFixed(title="Two Fixed",
                                   parent=wx.GetTopLevelParent(self))
        two_fixed_frame.Show()

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

import wx

from .two_tou import TwoTOU


class ChoiceModelFrame(wx.Frame):

    def __init__(self):
        super().__init__(None, title="Veritas Economics")
        self.init_ui()

    def init_ui(self):
        self.SetBackgroundColour('cream')
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Title of the home page
        title_font = wx.Font(wx.FontInfo(15).Bold())
        title_label = wx.StaticText(self, label='Electricity Service Plan Preferences and Selection Probabilities',
                                    style=wx.ALIGN_CENTER)
        title_label.SetFont(title_font)

        # Description under the title label
        description_sizer = wx.BoxSizer(wx.VERTICAL)
        description_label_one = wx.StaticText(self, label='Double click the module with the plans you want to evaluate',
                                              style=wx.ALIGN_CENTER)
        description_label_two = wx.StaticText(self, label='I want to evaluate:',
                                              style=wx.ALIGN_CENTER)
        description_sizer.Add(description_label_one, wx.CENTER, border=10, flag=wx.ALL | wx.EXPAND)
        description_sizer.Add(description_label_two, wx.CENTER, border=10, flag=wx.ALL | wx.EXPAND)

        # Used for adding the 3 buttons with their respective choices
        options_sizer = wx.BoxSizer(wx.HORIZONTAL)

        two_time_button = wx.Button(self, label="Two Time-of-Use (TOU) Plans")
        two_time_button.Bind(wx.EVT_BUTTON, self.calculate_two_tou)
        options_sizer.Add(two_time_button, border=10, proportion=1, flag=wx.ALL | wx.EXPAND)

        # Add individual box sizer(s) to main box sizer(vbox)
        vbox.Add(title_label, flag=wx.ALL | wx.EXPAND, border=20)
        vbox.Add(description_sizer, wx.CENTER, flag=wx.EXPAND)
        vbox.Add(options_sizer, flag=wx.EXPAND)

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

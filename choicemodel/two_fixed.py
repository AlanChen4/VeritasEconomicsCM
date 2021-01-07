import wx

from .Components.fixed import Fixed
from .Components.results import Results
from .Components.status_quo import StatusQuo


class TwoFixed(wx.Frame):

    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, title=title, parent=parent)
        self.SetBackgroundColour('white')
        self.init_ui()

    def init_ui(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Used to store status quo and plans
        plans_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create Status Quo and Fixed Plans
        status_quo = StatusQuo(self)
        fixed_a = Fixed(parent=self, plan_title='A')
        fixed_b = Fixed(parent=self, plan_title='B')

        results = Results(self)

        plans_sizer.Add(status_quo)
        plans_sizer.Add(fixed_a)
        plans_sizer.Add(fixed_b)

        vbox.Add(plans_sizer)
        vbox.Add(results)

        vbox.SetSizeHints(self)
        self.SetSizer(vbox)

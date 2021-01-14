import wx

from .Components.results import Results
from .Components.status_quo import StatusQuo
from .Components.tou import TOU


class TwoTOU(wx.Frame):

    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, title=title, parent=parent)
        self.tou_a = TOU(parent=self, plan_title='A')
        self.tou_b = TOU(parent=self, plan_title='B')
        self.init_ui()

    def init_ui(self):
        self.SetSize(600, 600)
        self.SetBackgroundColour('white')

        vbox = wx.BoxSizer(wx.VERTICAL)

        plans_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create Status Quo info
        status_quo = StatusQuo(self)

        # Add status quo to plans sizer
        plans_sizer.Add(status_quo)

        # Create TOU A and TOU B

        # Add TOU A and TOU B to plans sizer
        plans_sizer.Add(self.tou_a)
        plans_sizer.Add(self.tou_b)

        # Create results components
        results = Results(self)

        # Add all components to the main sizer in order
        vbox.Add(plans_sizer)
        vbox.Add(results)

        vbox.SetSizeHints(self)
        self.SetSizer(vbox)


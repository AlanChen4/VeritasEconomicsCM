import wx

from .fixed import Fixed
from .results import Results
from .status_quo import StatusQuo
from .tou import TOU


class OneEach(wx.Frame):

    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, title=title, parent=parent)
        self.SetBackgroundColour('white')
        self.init_ui()

    def init_ui(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        plans_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create billing plans
        status_quo = StatusQuo(self)
        tou = TOU(parent=self, plan_title='')
        fixed = Fixed(parent=self, plan_title='')

        plans_sizer.Add(status_quo)
        plans_sizer.Add(tou)
        plans_sizer.Add(fixed)

        results = Results(self)

        vbox.Add(plans_sizer)
        vbox.Add(results)

        vbox.SetSizeHints(self)
        self.SetSizer(vbox)

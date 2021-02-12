import wx

from ..geomodel import GeoModel
from ..model import Model, show_graphs


class Results(wx.Panel):

    def __init__(self, parent=None):
        super(Results, self).__init__(parent=parent)
        self.init_ui()

    def init_ui(self):
        root_sizer = wx.BoxSizer(wx.VERTICAL)

        # Description before calculate buttons
        results_sizer = wx.BoxSizer(wx.HORIZONTAL)
        results_font = wx.Font(wx.FontInfo(12).Bold())
        results_label = wx.StaticText(self, label='Results - Predictions of Potential Market Size')
        results_label.SetFont(results_font)

        results_sizer.Add(results_label, flag=wx.ALL, border=10)

        # calculate service
        calculate_sizer = wx.BoxSizer(wx.HORIZONTAL)
        calculate_service_label = wx.StaticText(self, label='Potential Market Size')

        # service territory
        service_sizer = wx.BoxSizer(wx.VERTICAL)
        service_label = wx.StaticText(self, label='Service Territory')
        service_button = wx.Button(self, label='Calculate')
        service_button.Bind(wx.EVT_BUTTON, self.calculate_service)
        service_sizer.Add(service_label)
        service_sizer.Add(service_button, flag=wx.ALL, border=10)

        # geo-model
        geo_sizer = wx.BoxSizer(wx.VERTICAL)
        geo_label = wx.StaticText(self, label='Load Geomodel')
        geo_button = wx.Button(self, label='Load')
        geo_button.Bind(wx.EVT_BUTTON, self.calculate_geo)
        geo_sizer.Add(geo_label)
        geo_sizer.Add(geo_button, flag=wx.ALL, border=10)

        calculate_sizer.Add(calculate_service_label, flag=wx.ALL, border=10)
        calculate_sizer.Add(service_sizer, flag=wx.LEFT, border=20)
        calculate_sizer.Add(geo_sizer, flag=wx.LEFT, border=20)

        root_sizer.Add(results_sizer)
        root_sizer.Add(calculate_sizer)

        self.SetSizer(root_sizer)

    def calculate_service(self, *args):
        """
        This function is bound to the calculate by Service Territory button
        """
        # determine plan type by calling name magic method on parent widget
        plan_type = type(self.GetParent()).__name__
        plan_a, plan_b = self.get_info(plan_type)
        if plan_a is not None and plan_b is not None:
            choice_model = Model(plan_a, plan_b)
            p_a, p_b = choice_model.get_plans()
            show_graphs(p_a, p_b)

    def calculate_geo(self, *args):
        """
        This function is bound to the Load Geo model button
        """
        plan_type = type(self.GetParent()).__name__
        plan_a, plan_b = self.get_info(plan_type)
        if plan_a is not None and plan_b is not None:
            # create model on backend to find switch probability
            choice_model = Model(plan_a, plan_b)
            prob_a, prob_b = choice_model.get_plans()
            geo_model = GeoModel()
            geo_model.show_map(prob_a, prob_b)

    def get_info(self, plan_type):
        """
        Checks if all inputs are complete and then returns the values for each
        :param plan_type: either TOU, OneEach, or TwoFixed
        :return: inputs for plan A and B respectively
        """
        # implement backend logic based on method
        if plan_type == 'TwoTOU':
            plan_a = {
                'off_peak': self.GetParent().tou_a.off_peak_price_input.GetValue(),
                'peak_price': self.GetParent().tou_a.peak_price_input.GetValue(),
                'peak_period': self.GetParent().tou_a.peak_period_input.GetValue(),
                'peak_season': self.GetParent().tou_a.peak_season_input.GetValue()
            }
            plan_b = {
                'off_peak': self.GetParent().tou_b.off_peak_price_input.GetValue(),
                'peak_price': self.GetParent().tou_b.peak_price_input.GetValue(),
                'peak_period': self.GetParent().tou_b.peak_period_input.GetValue(),
                'peak_season': self.GetParent().tou_b.peak_season_input.GetValue()
            }
            # return if any of the inputs are empty, as this will result in errors for the model
            for a, b in zip(plan_a.values(), plan_b.values()):
                if a == '' or b == '':
                    error_popup = wx.MessageDialog(None, "Please make sure that no inputs are empty!")
                    error_popup.ShowModal()
                    return None, None
            return plan_a, plan_b
        # 2/5: Currently these are unsupported
        elif plan_type == 'TwoFixed':
            print(plan_type)
        elif plan_type == 'OneEach':
            print(plan_type)

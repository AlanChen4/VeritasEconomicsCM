import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from .constants import *
from pathlib import Path


def show_graphs(lp1_rate_by_segment, lp2_rate_by_segment):
    """
    Show graphs based on data from the get_plans_function
    :param lp1_rate_by_segment: Switch probability for each market segment in plan one
    :param lp2_rate_by_segment: Switch probability for each market segment in plan two
    """
    p1_x_values = []
    p2_x_values = []
    p1_y_values = []
    p2_y_values = []
    for name1, value1, name2, value2 in zip(lp1_rate_by_segment.index, lp1_rate_by_segment.values,
                                            lp2_rate_by_segment.index, lp2_rate_by_segment.values):
        split_name_1, split_name_2 = name1[0].split(' - '), name2[0].split(' - ')
        short_name_1, short_name_2 = f'{split_name_1[1]} ({split_name_1[0]})', \
                                     f'{split_name_2[1]} ({split_name_2[0]})'
        p1_x_values.append(short_name_1)
        p2_x_values.append(short_name_2)
        p1_y_values.append(value1[0])
        p2_y_values.append(value2[0])

    # Number of total groups of bars
    n = len(p1_x_values)

    # Position of bars on x-axis
    ind = np.arange(n)

    # Width of a bar
    width = 0.3

    plt.figure('Bar Graph Model', figsize=(12, 8))
    plt.bar(ind, p1_y_values, width, label='Plan One', color='orange')
    plt.bar(ind + width, p2_y_values, width, label='Plan Two', color='royalblue')
    plt.xticks(ind + width / 2, p1_x_values, rotation=90)
    plt.tight_layout()

    # add legend: plan A is orange, plan B is blue
    colors = {'Plan A': 'orange', 'Plan B': 'royalblue'}
    labels = list(colors.keys())
    handles = [plt.Rectangle((0, 0), 1, 1, color=colors[label]) for label in labels]
    plt.legend(handles, labels)
    plt.show()


class Model:

    def __init__(self, plan_a, plan_b):
        """
        :param plan_a: Array containing information belonging to plan A
        :param plan_b: Array containing information belonging to plan B
        """
        self.p1_off_peak = np.array([float(plan_a['off_peak'][1:])])  # [1:] is to remove dollar sign
        self.p1_peak = np.array([float(plan_a['peak_price'][1:])])
        self.p1_peak_time = BASE[plan_a['peak_period']]
        self.p1_peak_season = SEASONS[plan_a['peak_season']]

        self.p2_off_peak = np.array([float(plan_b['off_peak'][1:])])
        self.p2_peak = np.array([float(plan_b['peak_price'][1:])])
        self.p2_peak_time = BASE[plan_b['peak_period']]
        self.p2_peak_season = SEASONS[plan_b['peak_season']]

    def get_plans(self):
        """
        Using the input from the UI, switch probability for plan 1 and plan 2 are found (for each market segment)
        :return: switch probability for each market segment
        """
        # import TN data
        tn_data_path = Path(__file__).parent / '../data/tn_data.csv'
        tn_df = pd.read_csv(tn_data_path)

        # remove first column and headers from TN data
        tn_df = tn_df.drop(tn_df.columns[[0]], axis=1)
        tn_data = tn_df.values

        # import participation coefficient data
        participation_coefficients_path = Path(__file__).parent / '../data/participation_coefficients.csv'
        pc_df = pd.read_csv(participation_coefficients_path)

        # separate participation coefficients into labels and data
        pc_labels = pc_df.values[:, [0]]
        pc_data = pc_df.values[:, [1]].astype(float)

        # calculate exponential utility for each plan
        p1_xu = np.exp(
            BASE['peak'] * self.p1_peak
            + BASE['off_peak'] * self.p1_off_peak
            + self.p1_peak_time * np.array([1])
            + self.p1_peak_season * np.array([1])
        )
        p2_xu = np.exp(
            BASE['peak'] * self.p2_peak
            + BASE['off_peak'] * self.p2_off_peak
            + self.p2_peak_time * np.array([1])
            + self.p2_peak_season * np.array([1])
        )

        # make calculations needed for logit model
        sum_xu = p1_xu + p2_xu
        p1_prob = p1_xu / sum_xu
        p2_prob = p2_xu / sum_xu

        scale_factor = np.array([0.3126567])
        ex_scale_log_sum = np.exp(scale_factor * np.log(sum_xu))
        participation_rate = ex_scale_log_sum / (ex_scale_log_sum + np.exp(-1 * pc_data))

        # calculate plan rates by segment
        p1_rates_by_segment = np.multiply(p1_prob, participation_rate)
        p2_rates_by_segment = np.multiply(p2_prob, participation_rate)

        # Give plan rates by segment titles
        p1_rates_by_segment_column = ['plan 1 rate']
        p2_rates_by_segment_column = ['plan 2 rate']

        lp1_rate_by_segment = pd.DataFrame(p1_rates_by_segment, index=pc_labels, columns=p1_rates_by_segment_column)
        lp2_rate_by_segment = pd.DataFrame(p2_rates_by_segment, index=pc_labels, columns=p2_rates_by_segment_column)

        return lp1_rate_by_segment, lp2_rate_by_segment

import pandas as pd
import numpy as np

from .constants import *
from pathlib import Path


class Model:

    def __init__(self):
        self.p1_peak = np.array([0.34])
        self.p1_off_peak = np.array([0.08])
        self.p1_peak_time = BASE['two_to_five']
        self.p1_peak_season = SEASONS['summer']

        self.p2_peak = np.array([0.27])
        self.p2_off_peak = np.array([0.09])
        self.p2_peak_time = BASE['two_to_six']
        self.p2_peak_season = SEASONS['summer']

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

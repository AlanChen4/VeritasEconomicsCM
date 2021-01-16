import pandas as pd
import numpy as np

from .constants import *
from pathlib import Path


def main():
    tn_data_path = Path(__file__).parent / '../data/TNdata.csv'
    tn_df = pd.read_csv(tn_data_path)
    tn_df = tn_df.drop(tn_df.columns[[0]], axis=1)

    # data without 1st column and headers
    tn_data = tn_df.values

    participation_coeff_path = Path(__file__).parent / '../data/PartCoeff.csv'
    pc_df = pd.read_csv(participation_coeff_path)

    pc_labels = pc_df.values[:, [0]]
    pc_data = pc_df.values[:, [1]].astype(float)

    # Plan one test with peak rate set as 2-5 summer only
    p1_xu = np.exp(
        BASE['peak'] * PLAN_ONE_PEAK
        + BASE['off_peak'] * PLAN_ONE_OFF_PEAK
        + BASE['two_to_five'] * np.array([1])
        + SEASONS['summer'] * np.array([1])
    )

    # Plan two test with peak rate set as 2-6 summer only
    p2_xu = np.exp(
        BASE['peak'] * PLAN_TWO_PEAK
        + BASE['off_peak'] * PLAN_TWO_OFF_PEAK
        + BASE['two_to_six'] * np.array([1])
        + SEASONS['summer'] * np.array([1])
    )

    # Hard-coded calculations
    sum_xu = p1_xu + p2_xu
    p1_prob = p1_xu / sum_xu
    p2_prob = p2_xu / sum_xu

    scale_factor = np.array([0.3126567])
    ex_scale_log_sum = np.exp(scale_factor * np.log(sum_xu))
    part_rate = ex_scale_log_sum / (ex_scale_log_sum + np.exp(-1 * pc_data))

    # Calculate plan rates by segment
    p1_rates_by_segment = np.multiply(p1_prob, part_rate)
    p2_rates_by_segment = np.multiply(p2_prob, part_rate)

    # Give plan rates by segment titles
    p1_rates_by_segment_column = ['plan 1 rate']
    p2_rates_by_segment_column = ['plan 2 rate']

    lp1_rate_by_segment = pd.DataFrame(p1_rates_by_segment, index=pc_labels, columns=p1_rates_by_segment_column)
    lp2_rate_by_segment = pd.DataFrame(p2_rates_by_segment, index=pc_labels, columns=p2_rates_by_segment_column)

    p1_num_by_segment_block = np.multiply(p1_rates_by_segment, tn_data)
    p2_num_by_segment_block = np.multiply(p2_rates_by_segment, tn_data)

    p1_num_by_segment = p1_num_by_segment_block.sum(axis=1)
    p2_num_by_segment = p2_num_by_segment_block.sum(axis=1)

    p1_num_by_segment_columns = ['Plan 1 Number']
    p2_num_by_segment_columns = ['Plan 2 Number']

    lp1_num_by_segment = pd.DataFrame(p1_num_by_segment, index=pc_labels, columns=p1_num_by_segment_columns)
    lp2_num_by_segment = pd.DataFrame(p2_num_by_segment, index=pc_labels, columns=p2_num_by_segment_columns)

    print(lp1_num_by_segment)


if __name__ == '__main__':
    main()

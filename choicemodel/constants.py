import numpy as np


# Base coefficients
BASE = {
    'peak': np.array([-8.76]),
    'off_peak': np.array([-1.5064]),
    '(3 hours) 2PM to 5PM': np.array([0.2482]),
    '(4 hours) 2PM to 6PM': np.array([0.3314]),
    '(6 hours) 2PM to 8PM': np.array([0]),
    '(3 hours) 3PM to 6PM': np.array([0.2726]),
    '(3 hours) 4PM to 7PM': np.array([0.1905]),
    '(2 hours) 5PM to 7PM': np.array([0.2247])
}

# Summer and winter coefficients
SEASONS = {
    'Summer': np.array([-0.2002]),
    'Summer and Winter': np.array([0])
}

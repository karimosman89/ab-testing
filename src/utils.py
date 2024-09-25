import pandas as pd
from scipy import stats

def load_data(file_path):
    return pd.read_csv(file_path)

def perform_t_test(control, treatment):
    t_stat, p_value = stats.ttest_ind(control, treatment)
    return t_stat, p_value

def interpret_results(p_value, alpha=0.05):
    if p_value < alpha:
        return "Statistically significant difference between groups."
    else:
        return "No statistically significant difference."

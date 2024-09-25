from utils import load_data, perform_t_test, interpret_results

data = load_data('data/ab_test_results.csv')
control = data[data['group'] == 'control']['conversion_rate']
treatment = data[data['group'] == 'treatment']['conversion_rate']

t_stat, p_value = perform_t_test(control, treatment)
print(f"T-Statistic: {t_stat}, P-Value: {p_value}")
print(interpret_results(p_value))

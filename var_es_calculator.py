import numpy as np

def calculate_var_es(simulated_returns, confidence_level=0.95):
    var_threshold = np.percentile(simulated_returns, (1 - confidence_level) * 100)
    expected_shortfall = np.mean(simulated_returns[simulated_returns <= var_threshold])
    return var_threshold, expected_shortfall
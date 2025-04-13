import numpy as np

def monte_carlo_simulation(mean, cov_matrix, num_simulations=10000):
    cholesky_matrix = np.linalg.cholesky(cov_matrix)
    uncorrelated_randoms = np.random.normal(size=(num_simulations, len(mean)))

    correlated_randoms = uncorrelated_randoms @ cholesky_matrix.T
    return mean + correlated_randoms
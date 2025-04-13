import numpy as np
import yfinance as yf
from monte_carlo import monte_carlo_simulation
from var_es_calculator import calculate_var_es
import datetime as dt

end_date = dt.datetime.now()
end_date_str = str.ftime("%Y-%m-%d")

start_date = "2020-01-01"
def fetch_data(tickers, start_date=start_date,end_date=end_date_str):
    # Fetch historical data from yfinance
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

def main():
    # Define your portfolio
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

    # Fetch data
    historical_data = fetch_data(tickers)

    # Calculate daily returns
    returns = historical_data.pct_change().dropna()

    # Calculate mean and covariance matrix for the simulations
    mean = returns.mean().values
    cov_matrix = returns.cov().values

    # Perform Monte Carlo simulations
    simulated_returns = monte_carlo_simulation(mean, cov_matrix, num_simulations=10000)

    # Calculate VaR and Expected Shortfall
    var, es = calculate_var_es(simulated_returns)
    
    # Display results
    print(f"Value at Risk (VaR): {var}")
    print(f"Expected Shortfall (ES): {es}")

if __name__ == "__main__":
    main()
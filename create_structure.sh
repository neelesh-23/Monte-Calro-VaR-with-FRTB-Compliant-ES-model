# Create directory structure
mkdir -p frtb_capital_model/{src,tests,docs}

# Create key files
touch frtb_capital_model/src/{monte_carlo.py,cholesky.py,var_es_calculator.py,main.py}
touch frtb_capital_model/tests/{test_var_es_calculator.py,test_monte_carlo.py}
touch frtb_capital_model/README.md
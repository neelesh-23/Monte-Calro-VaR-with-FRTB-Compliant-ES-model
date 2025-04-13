# Basel III/FRTB-Compliant Capital Model

This repository implements a Basel III/FRTB-compliant capital model using Monte Carlo simulations, Cholesky decomposition, and calculations for Value at Risk (VaR) and Expected Shortfall (ES).

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Methodology](#methodology)
  - [Monte Carlo Simulations](#monte-carlo-simulations)
  - [Cholesky Decomposition](#cholesky-decomposition)
  - [VaR and ES Calculations](#var-and-es-calculations)
- [Testing](#testing)

## Introduction

The implemented model aligns with the key components of FRTB regulations, providing tools for regulatory capital calculations through sophisticated risk modeling techniques.

## Installation

Clone this repository and install the necessary dependencies:

```bash
git clone https://github.com/yourusername/frtb-capital-model.git
cd frtb-capital-model
pip install -r requirements.txt
```

## Usage

To perform simulations and calculations:

```bash
python src/main.py
```

## Methodology

### Monte Carlo Simulations

Use Monte Carlo techniques to simulate potential future states of a portfolio incorporating correlated risk factors.

### Cholesky Decomposition

Employed to model correlations between risk factors, aiding in more accurate risk aggregation.

### VaR and ES Calculations

The module calculates both Value at Risk and Expected Shortfall to meet regulatory requirements.

## Testing

Test scripts are included to verify the integrity of calculations and simulations.

```bash
pytest tests/
```

For further details, explore the [docs](docs/) directory.
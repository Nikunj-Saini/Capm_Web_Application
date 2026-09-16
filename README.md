# CAPM Web Application

A comprehensive **Streamlit-based financial analytics platform** that combines **CAPM analysis, stock analysis, technical indicators, portfolio analytics, risk analysis, Monte Carlo simulation, and machine-learning-based stock price prediction** into an interactive dashboard.

---

## Project Overview

The **CAPM Web Application** is a quantitative finance and stock analytics platform built with Python and Streamlit.

It uses historical market data to calculate financial metrics, visualize stock performance, analyze risk and returns, perform portfolio analysis, and generate machine-learning-based price forecasts.

The application is designed for **financial analysis, quantitative research, and educational purposes**.

---

## Key Features

### 1. CAPM Return Analysis

The CAPM module analyzes expected returns and systematic risk.

It provides metrics such as:

* Beta
* Expected annual return
* Annual volatility
* Alpha / excess return
* Market-relative performance
* Growth of capital
* Portfolio-level analytics

CAPM is calculated using:

```text
Expected Return = Risk-Free Rate + Beta × (Market Return − Risk-Free Rate)
```

---

### 2. Stock Analysis

Analyze individual stocks using historical market data.

Users can select:

* Stock ticker
* Start date
* End date

The module provides:

* Historical price data
* Stock performance
* Company information
* Financial information
* Interactive charts
* Market analysis

Example tickers:

```text
AAPL
TSLA
MSFT
NVDA
```

---

### 3. AI Stock Price Prediction

The application includes a machine-learning module for stock price forecasting.

Users can configure:

* Stock ticker
* Historical training period
* Forecast horizon
* Machine-learning model

Currently supported model:

* Random Forest Regression

The prediction module can display:

* Current price
* Predicted price
* Percentage change
* Mean Absolute Error (MAE)
* R² Score
* Historical price trajectory
* Forecast visualization

> Machine-learning predictions are estimates based on historical data and should not be interpreted as guaranteed future prices.

---

### 4. Technical Analysis

The technical analysis module helps analyze historical price behavior and market trends.

It can be used for:

* Price trend analysis
* Moving averages
* Momentum analysis
* Volatility analysis
* Technical indicators
* Historical market behavior

---

### 5. Portfolio Analysis

Analyze multiple stocks as a portfolio.

Users can select multiple assets and configure the historical analysis period.

Portfolio analysis can include:

* Portfolio returns
* Portfolio risk
* Asset allocation
* Correlation
* Diversification
* Risk-adjusted performance

Example portfolio:

```text
AAPL
TSLA
MSFT
NVDA
```

---

### 6. Risk Analysis

The application provides visual analysis of the relationship between risk and expected return.

The risk analysis module can be used to examine:

* Expected return
* Volatility
* Systematic risk
* Asset-level risk
* Portfolio risk
* Risk-return relationships

---

### 7. Monte Carlo Simulation

The application includes Monte Carlo simulation for generating possible future stock-price paths.

General workflow:

```text
Historical Market Data
        ↓
Return & Volatility Estimation
        ↓
Random Simulation
        ↓
Multiple Future Price Paths
        ↓
Future Price Distribution
```

Instead of producing one deterministic outcome, Monte Carlo simulation generates multiple possible scenarios based on the assumptions used by the model.

---

## Technology Stack

### Programming Language

* Python

### Framework

* Streamlit

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Plotly

### Financial Data

* yfinance

### Machine Learning

* Scikit-learn
* Random Forest Regression

### Financial Models

* Capital Asset Pricing Model (CAPM)
* Portfolio Analysis
* Technical Analysis
* Risk Analysis
* Monte Carlo Simulation

---

## Project Structure

```text
Capm_Web_Application/
│
├── app.py
├── CAPM_functions.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── pages/
│   ├── capm_return.py
│   ├── stock_analysis.py
│   ├── stock_prediction.py
│   └── trading_app.py
│
├── assets/
│   └── ...
│
└── ...
```

> The exact structure may vary depending on the current version of the project.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Nikunj-Saini/Capm_Web_Application.git
```

Navigate to the project directory:

```bash
cd Capm_Web_Application
```

---

### 2. Create a Virtual Environment

#### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install streamlit pandas numpy scikit-learn plotly yfinance
```

---

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will normally open at:

```text
http://localhost:8501
```

---

## How to Use

### Step 1 — Select a Module

Use the application navigation to select the required analysis module.

Available modules may include:

```text
CAPM Return
Stock Analysis
Stock Prediction
Trading App
```

### Step 2 — Select Assets

Enter stock tickers such as:

```text
AAPL
TSLA
MSFT
NVDA
```

### Step 3 — Configure Parameters

Depending on the selected module, configure:

* Historical period
* Start date
* End date
* Forecast horizon
* Training period
* Portfolio assets
* Machine-learning model

### Step 4 — Analyze

Run the selected analysis to generate financial metrics, visualizations, simulations, and forecasts.

---

## Important Financial Metrics

### Beta

Beta measures an asset's sensitivity to movements in the broader market.

```text
β > 1  → Higher market sensitivity
β = 1  → Approximately market-level sensitivity
β < 1  → Lower market sensitivity
```

### Alpha

Alpha represents excess return relative to a specified benchmark or model-implied return, depending on the calculation used.

### Volatility

Volatility measures the variability of historical returns and is commonly used as an indicator of market risk.

### Mean Absolute Error

MAE measures the average absolute difference between predicted and actual values.

```text
MAE = Average(|Actual − Predicted|)
```

Lower MAE generally indicates smaller prediction errors on the evaluated dataset.

### R² Score

R² measures the proportion of variance in the target variable explained by the model on the evaluated dataset.

---

## Machine Learning Pipeline

The stock prediction module follows a general workflow:

```text
Historical Market Data
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Train / Test Data
        ↓
Random Forest Regression
        ↓
Model Evaluation
        ↓
Future Forecast
        ↓
Interactive Visualization
```

Model performance can vary depending on:

* Stock selected
* Historical period
* Market conditions
* Forecast horizon
* Feature selection
* Data quality

---

## Visualizations

The application uses interactive Plotly visualizations for financial analysis.

Visualizations may include:

* Historical stock prices
* Forecast trajectories
* Relative performance
* Growth of capital
* Portfolio metrics
* Risk-return relationships
* Monte Carlo simulations
* Technical indicators

Plotly provides interactive features such as:

* Zoom
* Pan
* Hover information
* Range selection

---

## Data Source

Historical market data is retrieved using **Yahoo Finance through the `yfinance` Python library**.

Market data availability and historical values may change over time.

---

## Disclaimer

This project is intended for **educational, research, and analytical purposes only**.

The financial calculations, simulations, metrics, and machine-learning predictions generated by this application should **not be considered financial, investment, or trading advice**.

Machine-learning models and financial models rely on historical data, statistical relationships, and assumptions. Past performance does not guarantee future results.

Users should conduct their own research and consult an appropriately qualified financial professional before making investment decisions.

---

## Future Improvements

Potential future enhancements include:

* Additional machine-learning models
* LSTM-based forecasting
* Transformer-based forecasting
* Advanced portfolio optimization
* Real-time market data
* Options analytics
* Value at Risk (VaR)
* Conditional VaR / Expected Shortfall
* Sharpe Ratio
* Sortino Ratio
* Efficient Frontier
* Portfolio rebalancing
* Advanced backtesting
* User authentication
* Cloud deployment
* Downloadable financial reports

---

## Author

**Nikunj Saini**

B.Tech in Artificial Intelligence and Data Science

GitHub:
https://github.com/Nikunj-Saini

---

## Contributing

Contributions, suggestions, and improvements are welcome.

Create a feature branch:

```bash
git checkout -b feature/new-feature
```

Add your changes:

```bash
git add .
```

Commit your changes:

```bash
git commit -m "Add new feature"
```

Push the branch:

```bash
git push origin feature/new-feature
```

Then create a Pull Request.

---

## License

This project is intended for educational and research purposes.

If an open-source license is added to the repository, its terms will apply to the project.

---

## Project Highlights

**An end-to-end quantitative finance dashboard combining CAPM analysis, stock analytics, portfolio analysis, technical analysis, risk analytics, Monte Carlo simulation, and machine-learning-based stock forecasting.**

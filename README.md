# FinSight — Financial Analytics & Portfolio Intelligence Platform

**FinSight** is an interactive financial analytics platform built with **Python and Streamlit** that combines stock market analysis, **CAPM**, technical indicators, portfolio analytics, risk analysis, Monte Carlo simulation, and interactive visualizations into a single dashboard.

## Live Demo

**FinSight:**
https://capm-dashboard-nikunj.streamlit.app/

## Overview

FinSight provides an interactive environment for analyzing stocks and understanding the relationship between **risk, return, market performance, and portfolio behavior**.

The platform fetches historical market data and transforms it into actionable financial insights through statistical calculations, financial models, technical indicators, and interactive visualizations.

## Features

### CAPM Analysis

* Calculate expected stock returns using CAPM
* Calculate and analyze Beta
* Analyze risk-free rate and market return
* Understand systematic risk
* Compare expected and historical returns

### Stock Market Analysis

* Historical stock price analysis
* Daily return analysis
* Trading volume analysis
* Stock performance visualization
* Multiple stock comparison
* Historical market data retrieval

### Technical Indicators

FinSight provides technical analysis using indicators such as:

* **SMA — Simple Moving Average**
* **RSI — Relative Strength Index**
* Moving-average trend analysis
* Price and volume analysis

### Portfolio Analysis

* Analyze multiple stocks
* Compare stock performance
* Analyze portfolio returns
* Compare risk and return
* Interactive portfolio visualizations

### Risk Analysis

FinSight provides multiple risk-related metrics and visualizations, including:

* Volatility
* Beta
* Historical returns
* Risk-return analysis
* Market relationship analysis

### Monte Carlo Simulation

FinSight uses **Monte Carlo simulation** to generate possible future stock-price scenarios.

The simulation can be used to visualize:

* Possible future price paths
* Distribution of simulated prices
* Potential returns
* Investment uncertainty
* Risk scenarios

### Interactive Visualizations

The dashboard uses **Plotly** to provide interactive financial charts.

Users can explore:

* Stock prices
* Returns
* Trading volume
* Technical indicators
* Portfolio performance
* Risk metrics
* Monte Carlo simulations

## Technology Stack

| Category           | Technologies                       |
| ------------------ | ---------------------------------- |
| Language           | Python                             |
| Framework          | Streamlit                          |
| Data Analysis      | Pandas, NumPy                      |
| Financial Data     | yFinance                           |
| Visualization      | Plotly                             |
| Financial Models   | CAPM, Beta, Monte Carlo Simulation |
| Technical Analysis | RSI, SMA                           |

## Project Architecture

```text
FinSight
│
├── app.py
├── CAPM_functions.py
├── requirements.txt
├── README.md
└── other project files
```

## Application Workflow

```text
        Stock Selection
              ↓
      Historical Market Data
              ↓
       Data Processing
              ↓
    ┌─────────┴─────────┐
    ↓                   ↓
CAPM Analysis     Technical Analysis
    ↓                   ↓
    └─────────┬─────────┘
              ↓
       Risk & Portfolio
           Analysis
              ↓
      Monte Carlo Simulation
              ↓
     Interactive Dashboard
```

## CAPM Model

FinSight implements the standard Capital Asset Pricing Model:

```text
Expected Return = Risk-Free Rate + Beta × (Market Return - Risk-Free Rate)
```

### Parameters

**Risk-Free Rate**

The theoretical return of an investment with negligible risk.

**Beta**

Measures the sensitivity of a stock's returns relative to the overall market.

**Market Return**

Represents the return of the broader market.

## Data Source

FinSight retrieves historical stock-market data using the **yFinance** Python library.

The availability of historical market data depends on the underlying data provider.

## Installation

Clone the repository:

```bash
git clone https://github.com/Nikunj-Saini/CAPM-Web-Application.git
```

Navigate to the project directory:

```bash
cd CAPM-Web-Application
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## Deployment

FinSight is deployed using **Streamlit Community Cloud**.

**Live Application:**

https://capm-dashboard-nikunj.streamlit.app/

## Future Enhancements

* Portfolio optimization
* Efficient Frontier analysis
* Sharpe Ratio
* Sortino Ratio
* Advanced risk metrics
* Additional technical indicators
* Machine-learning-based price prediction
* Portfolio backtesting
* Database integration
* User portfolio management
* Real-time market data integration

## Disclaimer

FinSight is developed for **educational and analytical purposes only**. The information and calculations provided by the application should not be considered financial advice or an investment recommendation.

## Author

**Nikunj Saini**

B.Tech — Artificial Intelligence & Data Science

**GitHub:**
https://github.com/Nikunj-Saini

**Portfolio:**
https://nikunjsaini.netlify.app/

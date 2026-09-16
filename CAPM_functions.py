import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

def interactive_plot(df, title="Stock Prices"):
    df = df.copy()
    if 'Date' not in df.columns:
        df = df.reset_index()

    fig = go.Figure()
    for col in df.columns:
        if col != 'Date':
            fig.add_trace(go.Scatter(x=df['Date'], y=df[col], name=col, mode='lines'))
    
    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Value",
        template="plotly_dark",
        hovermode="x unified",
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig


def normalize(df):
    df = df.copy()
    return df / df.iloc[0]



def daily_return(df):
    return df.pct_change() * 100


def calculate_beta(df, stock):
    x = df['sp500']
    y = df[stock]
    beta, alpha = np.polyfit(x, y, 1)
    return beta, alpha

def get_correlation(df):
    return df.corr()

def calculate_volatility(df):
    return df.std() * np.sqrt(252)

def calculate_cumulative_return(df):
    return (1 + df/100).cumprod() - 1


def add_technical_indicators(df, stock):
    data = pd.DataFrame(df[stock])
    data['SMA_20'] = data[stock].rolling(window=20).mean()
    data['SMA_50'] = data[stock].rolling(window=50).mean()
    
  
    delta = data[stock].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    
    return data

def optimize_portfolio(returns_df):
    stocks = [c for c in returns_df.columns if c != 'sp500']
    num_portfolios = 2000
    all_weights = np.zeros((num_portfolios, len(stocks)))
    ret_arr = np.zeros(num_portfolios)
    vol_arr = np.zeros(num_portfolios)
    sharpe_arr = np.zeros(num_portfolios)

    for i in range(num_portfolios):
        weights = np.random.random(len(stocks))
        weights /= np.sum(weights)
        all_weights[i,:] = weights
        
        # Expected Return
        ret_arr[i] = np.sum((returns_df[stocks].mean() * weights) * 252)
        # Volatility
        vol_arr[i] = np.sqrt(np.dot(weights.T, np.dot(returns_df[stocks].cov() * 252, weights)))
        # Sharpe Ratio (Assuming RF=0 for simplicity here)
        sharpe_arr[i] = ret_arr[i] / vol_arr[i]

    max_sharpe_idx = sharpe_arr.argmax()
    return stocks, all_weights[max_sharpe_idx, :], ret_arr[max_sharpe_idx], vol_arr[max_sharpe_idx]
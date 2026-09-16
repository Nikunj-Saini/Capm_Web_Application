import streamlit as st
import pandas as pd 
import yfinance as yf 
import plotly.graph_objects as go
import datetime
import ta 

from pages.utils.plotly_figure import plotly_table

# Setting the page config
st.set_page_config(
    page_title="FinSight | Stock Analysis",
    page_icon="📈",
    layout="wide"
)

st.title('Stock Analysis')

col1, col2, col3 = st.columns(3)
today = datetime.date.today()
with col1:
    ticker = st.text_input("Stock Ticker", "TSLA")

with col2:
    start_date = st.date_input("Choose Start Date", datetime.date(today.year - 1, today.month, today.day))

with col3:
    end_date = st.date_input("Choose End Date", today)

if ticker:
    try:
        st.subheader(f"Analyzing: {ticker.upper()}")
        
        stock = yf.Ticker(ticker)
        info = stock.info
        
        with st.expander("Company Profile", expanded=True):
            st.write(info.get('longBusinessSummary', 'No summary available.'))
            col_prof1, col_prof2, col_prof3 = st.columns(3)
            col_prof1.write(f"**Sector:** {info.get('sector', 'N/A')}")
            col_prof2.write(f"**Full Time Employees:** {info.get('fullTimeEmployees', 'N/A')}")
            col_prof3.write(f"**Website:** {info.get('website', 'N/A')}")
        
        st.markdown("---")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("### Key Metrics")
            df_info = pd.DataFrame(index=("Market Cap", 'Beta', 'EPS', 'PE Ratio'))
            
            # Format numbers properly
            market_cap = info.get("marketCap", "N/A")
            if isinstance(market_cap, (int, float)):
                market_cap = f"${market_cap:,.0f}"
                
            df_info['Value'] = [
                market_cap, 
                info.get("beta", "N/A"), 
                info.get("trailingEps", "N/A"), 
                info.get("trailingPE", "N/A")
            ]
            fig_table = plotly_table(df_info)
            st.plotly_chart(fig_table, use_container_width=True)
            
        with col2:
            st.markdown("### Price Chart")
            data = stock.history(start=start_date, end=end_date)
            
            if not data.empty:
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=data.index,
                                open=data['Open'],
                                high=data['High'],
                                low=data['Low'],
                                close=data['Close'],
                                name='Price'))
                fig.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0), xaxis_rangeslider_visible=False)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No price data available for the selected dates.")
                
        st.markdown("---")
        
        if not data.empty:
            st.markdown("### Technical Indicators")
            
            # Calculate Indicators
            data['SMA_20'] = ta.trend.sma_indicator(data['Close'], window=20)
            data['SMA_50'] = ta.trend.sma_indicator(data['Close'], window=50)
            data['RSI'] = ta.momentum.rsi(data['Close'], window=14)
            data['MACD'] = ta.trend.macd(data['Close'])
            data['MACD_Signal'] = ta.trend.macd_signal(data['Close'])
            
            tab1, tab2, tab3 = st.tabs(["Moving Averages", "RSI", "MACD"])
            
            with tab1:
                fig_ma = go.Figure()
                fig_ma.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))
                fig_ma.add_trace(go.Scatter(x=data.index, y=data['SMA_20'], mode='lines', name='SMA 20', line=dict(color='orange')))
                fig_ma.add_trace(go.Scatter(x=data.index, y=data['SMA_50'], mode='lines', name='SMA 50', line=dict(color='red')))
                fig_ma.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
                st.plotly_chart(fig_ma, use_container_width=True)
                
            with tab2:
                fig_rsi = go.Figure()
                fig_rsi.add_trace(go.Scatter(x=data.index, y=data['RSI'], mode='lines', name='RSI', line=dict(color='purple')))
                fig_rsi.add_hline(y=70, line_dash="dash", line_color="red", annotation_text="Overbought")
                fig_rsi.add_hline(y=30, line_dash="dash", line_color="green", annotation_text="Oversold")
                fig_rsi.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0), yaxis_title="RSI Value")
                st.plotly_chart(fig_rsi, use_container_width=True)
                
            with tab3:
                fig_macd = go.Figure()
                fig_macd.add_trace(go.Scatter(x=data.index, y=data['MACD'], mode='lines', name='MACD', line=dict(color='blue')))
                fig_macd.add_trace(go.Scatter(x=data.index, y=data['MACD_Signal'], mode='lines', name='Signal', line=dict(color='orange')))
                fig_macd.add_trace(go.Bar(x=data.index, y=data['MACD'] - data['MACD_Signal'], name='Histogram', marker_color='gray'))
                fig_macd.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0), yaxis_title="MACD Value")
                st.plotly_chart(fig_macd, use_container_width=True)
                
    except Exception as e:
        st.error(f"Error fetching data for ticker {ticker}: {e}")

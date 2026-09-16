import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
import CAPM_functions
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# PAGE CONFIG
st.set_page_config(page_title="FinSight | CAPM & Portfolio Pro", page_icon="📈", layout="wide")

# ADVANCED CSS FOR PREMIUM UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    div[data-testid="stMetric"] {
        background-color: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    div[data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        border-color: #3b82f6;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: rgba(30, 41, 59, 0.5);
        border-radius: 10px 10px 0px 0px;
        color: #94a3b8;
        font-weight: 600;
        padding: 10px 20px;
        border: none;
    }

    .stTabs [aria-selected="true"] {
        background-color: #3b82f6 !important;
        color: white !important;
    }
    
    .card {
        background-color: rgba(30, 41, 59, 0.7);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }
    
    h1 {
        background: linear-gradient(90deg, #3b82f6, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        letter-spacing: -1px;
    }
    
    /* Hide Streamlit header anchor links */
    .stApp a.header-anchor {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# HEADER
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.markdown("<h1>FinSight</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:1.2rem;'>Advanced CAPM & Portfolio Intelligence Dashboard</p>", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2620/2620582.png", width=80)
    st.header("Config Engine")
    
    default_stocks = ['AAPL', 'TSLA', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'META', 'NFLX']
    stocks_selection = st.multiselect("Active Portfolio", default_stocks, ['AAPL', 'TSLA', 'MSFT', 'NVDA'])
    
    custom_tickers = st.text_input("Add Custom Tickers", "").upper()
    if custom_tickers:
        additional_stocks = [x.strip() for x in custom_tickers.split(',')]
        stocks_list = list(set(stocks_selection + additional_stocks))
    else:
        stocks_list = stocks_selection
        
    year = st.slider('Lookback Horizon (Years)', 1, 10, 2)
    rf_rate = st.number_input('Risk-Free Rate (%)', 0.0, 10.0, 4.2) / 100
    
    st.markdown("---")
    st.caption("v2.0 Premium | Built by Antigravity")

if not stocks_list:
    st.warning("Please select at least one stock to begin analysis.")
    st.stop()

try:
    with st.spinner('Synchronizing market data...'):
        end = datetime.date.today()
        start = end - datetime.timedelta(days=365 * year)
        
        # Download data
        all_tickers = stocks_list + ['^GSPC']
        raw_data = yf.download(all_tickers, start=start, end=end, auto_adjust=True, progress=False)
        
        if raw_data.empty:
            st.error("Data retrieval failed. Check tickers.")
            st.stop()
            
        # Data Extraction
        if isinstance(raw_data.columns, pd.MultiIndex):
            stocks_df = raw_data['Close'].copy()
        else:
            stocks_df = pd.DataFrame(raw_data['Close'])
            stocks_df.columns = stocks_list + ['^GSPC']
            
        stocks_df.rename(columns={'^GSPC': 'sp500'}, inplace=True)
        stocks_df = stocks_df.ffill().dropna()
        returns_df = CAPM_functions.daily_return(stocks_df).dropna()

    # --- MAIN ENGINE ---
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Performance", 
        "CAPM Analytics", 
        "Technicals", 
        "Portfolio Opt", 
        "Risk Cloud"
    ])

    with tab1:
        st.markdown("### Market Momentum")
        c1, c2 = st.columns([2, 1])
        with c1:
            norm_df = CAPM_functions.normalize(stocks_df)
            st.plotly_chart(CAPM_functions.interactive_plot(norm_df, "Relative Performance (Normalized)"), width='stretch')
        with c2:
            cum_rets = CAPM_functions.calculate_cumulative_return(returns_df) * 100
            st.plotly_chart(CAPM_functions.interactive_plot(cum_rets, "Growth of Capital (%)"), width='stretch')

    with tab2:
        st.markdown("### CAPM Expected Yields")
        
        # Calculations
        beta, alpha, vol = {}, {}, {}
        for s in stocks_list:
            b, a = CAPM_functions.calculate_beta(returns_df, s)
            beta[s], alpha[s] = b, a
            vol[s] = returns_df[s].std() * (252**0.5)
            
        rm = returns_df['sp500'].mean() * 252 / 100
        
        # Metrics Display
        cols = st.columns(min(len(stocks_list), 4))
        for i, s in enumerate(stocks_list):
            with cols[i % 4]:
                exp_ret = rf_rate + (beta[s] * (rm - rf_rate))
                st.metric(s, f"{exp_ret*100:.2f}%", f"β: {beta[s]:.2f}")

        # Summary Table
        res_data = []
        for s in stocks_list:
            res_data.append({
                "Asset": s,
                "Beta (Systematic Risk)": round(beta[s], 3),
                "Expected Annual Return": f"{round((rf_rate + beta[s]*(rm-rf_rate))*100, 2)}%",
                "Annual Volatility": f"{round(vol[s], 2)}%",
                "Alpha (Excess Return)": round(alpha[s], 4)
            })
        st.dataframe(pd.DataFrame(res_data), use_container_width=True, hide_index=True)

    with tab3:
        st.markdown("### Technical Intelligence")
        selected_tech_stock = st.selectbox("Select Asset for Deep Dive", stocks_list)
        tech_data = CAPM_functions.add_technical_indicators(stocks_df, selected_tech_stock)
        
        fig_tech = go.Figure()
        fig_tech.add_trace(go.Scatter(x=tech_data.index, y=tech_data[selected_tech_stock], name="Price", line=dict(color='#3b82f6')))
        fig_tech.add_trace(go.Scatter(x=tech_data.index, y=tech_data['SMA_20'], name="SMA 20", line=dict(dash='dash', color='#10b981')))
        fig_tech.add_trace(go.Scatter(x=tech_data.index, y=tech_data['SMA_50'], name="SMA 50", line=dict(dash='dot', color='#f59e0b')))
        
        fig_tech.update_layout(title=f"{selected_tech_stock} Technical Indicators", template="plotly_dark", height=500)
        st.plotly_chart(fig_tech, use_container_width=True)
        
        st.markdown(f"#### Relative Strength Index (RSI): **{tech_data['RSI'].iloc[-1]:.2f}**")
        st.progress(min(max(float(tech_data['RSI'].iloc[-1])/100, 0.0), 1.0))

    with tab4:
        st.markdown("### Portfolio Weight Optimization")
        st.info("Calculating Maximum Sharpe Ratio portfolio using Monte Carlo simulation (2000 paths)...")
        
        stocks, weights, p_ret, p_vol = CAPM_functions.optimize_portfolio(returns_df)
        
        c1, c2 = st.columns([1, 2])
        with c1:
            st.markdown("#### Optimal Allocation")
            weight_df = pd.DataFrame({'Asset': stocks, 'Weight': weights})
            fig_pie = px.pie(weight_df, values='Weight', names='Asset', hole=0.4, 
                           color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with c2:
            st.markdown("#### Portfolio Metrics")
            st.write(f"**Target Return:** {p_ret*100:.2f}%")
            st.write(f"**Expected Risk:** {p_vol:.2f}%")
            st.write(f"**Sharpe Ratio:** {p_ret/p_vol:.2f}")
            
            st.dataframe(weight_df.sort_values(by='Weight', ascending=False), use_container_width=True, hide_index=True)

    with tab5:
        st.markdown("### Market Risk Cloud")
        c1, c2 = st.columns(2)
        with c1:
            corr = CAPM_functions.get_correlation(returns_df)
            fig_corr = px.imshow(corr, text_auto=True, color_continuous_scale='Viridis', title="Correlation Heatmap")
            st.plotly_chart(fig_corr, width='stretch')
        with c2:
            fig_scat = px.scatter(pd.DataFrame(res_data), x="Annual Volatility", y="Beta (Systematic Risk)", 
                                 text="Asset", size=[10]*len(stocks_list), color="Asset", 
                                 title="Risk Topology (Volatility vs Beta)")
            st.plotly_chart(fig_scat, width='stretch')

    # ADDING A HIDDEN FEATURE: PRICE PREDICTION (EXTRA TAB)
    with st.expander("Advanced: Monte Carlo Price Projection (Next 30 Days)"):
        selected_pred = st.selectbox("Select Asset for Prediction", stocks_list)
        last_price = stocks_df[selected_pred].iloc[-1]
        daily_vol = returns_df[selected_pred].std() / 100
        
        simulations = 100
        days = 30
        results = np.zeros((days, simulations))
        
        for i in range(simulations):
            prices = [last_price]
            for d in range(days-1):
                prices.append(prices[-1] * (1 + np.random.normal(0, daily_vol)))
            results[:, i] = prices
            
        fig_pred = go.Figure()
        for i in range(min(simulations, 20)): # Show only 20 paths for clarity
            fig_pred.add_trace(go.Scatter(y=results[:, i], mode='lines', line=dict(width=1), opacity=0.3, showlegend=False))
        
        fig_pred.add_trace(go.Scatter(y=results.mean(axis=1), mode='lines', line=dict(color='yellow', width=3), name="Average Path"))
        fig_pred.update_layout(title=f"30-Day Monte Carlo Projection for {selected_pred}", template="plotly_dark")
        st.plotly_chart(fig_pred, width='stretch')

except Exception as e:
    st.error(f"Simulation Error: {e}")
    st.info("Check ticker symbols and internet connection.")

st.markdown("---")
st.caption("FinSight | Data powered by Yahoo Finance API")
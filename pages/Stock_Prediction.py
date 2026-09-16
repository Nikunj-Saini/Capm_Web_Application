import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import plotly.graph_objects as go
try:
    from sklearn.svm import SVR
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.metrics import mean_absolute_error, r2_score
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

# PAGE CONFIG
st.set_page_config(page_title="FinSight | AI Stock Prediction", page_icon="📈", layout="wide")

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
        border-color: #a855f7;
    }

    h1 {
        background: linear-gradient(90deg, #a855f7, #d8b4fe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        letter-spacing: -1px;
    }
    
    /* Hide Streamlit header anchor links */
    .stApp a.header-anchor {
        display: none !important;
    }
    
    .stAlert {
        background-color: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# HEADER
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.markdown("<h1>AI Price Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:1.2rem;'>Advanced Machine Learning Forecasting Engine</p>", unsafe_allow_html=True)

# SIDEBAR CONFIGURATION
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2043/2043248.png", width=80)
    st.header("Prediction Engine")
    
    ticker = st.text_input("Stock Ticker", "AAPL").upper()
    lookback_years = st.slider("Training Data (Years)", 1, 10, 5)
    forecast_out = st.slider("Forecast Horizon (Days)", 1, 90, 30)
    
    if SKLEARN_AVAILABLE:
        model_choice = st.selectbox("AI Model", ["Support Vector Regressor (SVR)", "Random Forest"])
    else:
        model_choice = st.selectbox("Model", ["Polynomial Trend"])
        st.warning("Install scikit-learn for advanced ML models.")
        
    run_prediction = st.button("Run Prediction Analysis", use_container_width=True)

if run_prediction:
    try:
        with st.spinner("Fetching data and training AI model..."):
            end = datetime.date.today()
            start = end - datetime.timedelta(days=365 * lookback_years)
            
            # 1. Fetch Data
            df = yf.download(ticker, start=start, end=end, progress=False)
            if df.empty:
                st.error("Data fetch failed. Check the ticker.")
                st.stop()
            
            if isinstance(df.columns, pd.MultiIndex):
                df = df['Close'].copy()
                df = pd.DataFrame({'Close': df[ticker]})
            else:
                df = df[['Close']]
                
            df.dropna(inplace=True)
            
            # 2. Prepare Data for Prediction
            df['Prediction'] = df[['Close']].shift(-forecast_out)
            
            X = np.array(df.drop(['Prediction'], axis=1))
            X_forecast = X[-forecast_out:] # Data to predict on
            X = X[:-forecast_out] # Training Data
            
            y = np.array(df['Prediction'])
            y = y[:-forecast_out] # Training Labels
            
            # 3. Train Model
            if SKLEARN_AVAILABLE:
                x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                
                if "SVR" in model_choice:
                    model = SVR(kernel='rbf', C=1e3, gamma=0.1)
                else:
                    model = RandomForestRegressor(n_estimators=100, random_state=42)
                    
                model.fit(x_train, y_train)
                
                # Metrics
                y_pred = model.predict(x_test)
                mae = mean_absolute_error(y_test, y_pred)
                r2 = r2_score(y_test, y_pred)
                
                # 4. Predict Future
                forecast_prediction = model.predict(X_forecast)
            else:
                # Fallback to simple numpy polyfit if sklearn is missing
                x_idx = np.arange(len(X)).flatten()
                y_flat = y.flatten()
                z = np.polyfit(x_idx, y_flat, 3)
                p = np.poly1d(z)
                
                mae = np.mean(np.abs(y_flat - p(x_idx)))
                r2 = 0.0 # dummy
                
                future_x = np.arange(len(X), len(X) + forecast_out)
                forecast_prediction = p(future_x)
            
            # 5. Build Result Dataframe
            last_date = df.index[-1]
            future_dates = pd.date_range(last_date + pd.Timedelta(days=1), periods=forecast_out)
            
            forecast_df = pd.DataFrame(index=future_dates, columns=['Forecast'])
            forecast_df['Forecast'] = forecast_prediction
            
            # Ensure continuity for the plot
            forecast_df.loc[last_date] = [df['Close'].iloc[-1]]
            forecast_df = forecast_df.sort_index()

        # --- RESULTS UI ---
        st.success("AI Analysis Complete!")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Current Price", f"${df['Close'].iloc[-1]:.2f}")
        with c2:
            st.metric(f"Predicted Price (in {forecast_out} days)", f"${forecast_prediction[-1]:.2f}", 
                      f"{(forecast_prediction[-1] - df['Close'].iloc[-1])/df['Close'].iloc[-1]*100:.2f}%")
        with c3:
            st.metric("Model Mean Absolute Error", f"${mae:.2f}", f"R² Score: {r2:.2f}" if SKLEARN_AVAILABLE else "")

        st.markdown("### Price Trajectory & AI Forecast")
        
        # Plotly Chart
        fig = go.Figure()
        
        # Historical Data
        fig.add_trace(go.Scatter(
            x=df.index[-252:], # Last 1 year of historical
            y=df['Close'][-252:], 
            name="Historical Data", 
            line=dict(color='#3b82f6', width=2)
        ))
        
        # Forecast Data
        fig.add_trace(go.Scatter(
            x=forecast_df.index, 
            y=forecast_df['Forecast'], 
            name="AI Forecast", 
            line=dict(color='#a855f7', width=3, dash='dot')
        ))
        
        # Styling
        fig.update_layout(
            template="plotly_dark",
            hovermode="x unified",
            margin=dict(l=20, r=20, t=30, b=20),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            xaxis_title="Date",
            yaxis_title="Price ($)",
            height=600,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)

        # Tabular Data Expanders
        with st.expander("View Detailed Forecast Data"):
            st.dataframe(forecast_df.style.format("{:.2f}"), use_container_width=True)
            
    except Exception as e:
        st.error(f"Prediction Error: {e}")
        st.info("Try adjusting the parameters or check the ticker symbol.")
else:
    st.info("Please enter a stock ticker and click 'Run Prediction Analysis' from the sidebar to begin.")

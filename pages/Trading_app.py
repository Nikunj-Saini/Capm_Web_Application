import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="FinSight | Trading App",
    page_icon="📈",
    layout="wide"
)

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
    
    .card {
        background-color: rgba(30, 41, 59, 0.7);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
        height: 100%;
    }
    
    .card:hover {
        transform: translateY(-5px);
        border-color: #3b82f6;
    }
    
    h1 {
        background: linear-gradient(90deg, #3b82f6, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        letter-spacing: -1px;
    }
    
    h3 {
        color: #e2e8f0;
        font-weight: 600;
        margin-top: 0;
    }
    
    p {
        color: #94a3b8;
        line-height: 1.6;
    }
    
    .feature-number {
        display: inline-block;
        background: rgba(59, 130, 246, 0.2);
        color: #60a5fa;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        text-align: center;
        line-height: 30px;
        font-weight: bold;
        margin-right: 10px;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

# HEADER
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.markdown("<h1>FinSight Trading Guide</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:1.2rem;'>We provide the greatest platform for you to collect all information prior to investing in stocks.</p>", unsafe_allow_html=True)

st.markdown("---")

# HERO IMAGE
try:
    st.image("trading image.webp", use_container_width=True)
except Exception:
    pass

st.markdown("---")
st.markdown("## Our Premium Services")
st.write("Navigate through our dashboard using the sidebar to access these powerful tools:")

# SERVICES CARDS
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3><span class="feature-number">1</span> Stock Information & Analysis</h3>
        <p>Through the <b>Stock Analysis</b> page, you can see comprehensive information about any stock. Get an in-depth look at company profiles, key metrics, and interactive historical price charts with technical indicators.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h3><span class="feature-number">3</span> CAPM Analytics</h3>
        <p>Discover how the <b>Capital Asset Pricing Model (CAPM)</b> calculates the expected return of different stock assets based on market risk (Beta) and overall market performance benchmarks.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3><span class="feature-number">2</span> AI Stock Prediction</h3>
        <p>You can explore predicted closing prices for the next 30 days based on historical stock data and advanced machine learning forecasting models. Use this tool to gain valuable insights into market trends and make informed decisions.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h3><span class="feature-number">4</span> Portfolio Optimization</h3>
        <p>Build and analyze an active portfolio of stocks. We calculate the optimal weighting of assets to maximize your Sharpe Ratio using Monte Carlo simulations, helping you balance risk and reward.</p>
    </div>
    """, unsafe_allow_html=True)
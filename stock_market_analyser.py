import yfinance as yf
import streamlit as st
import pandas as pd
import datetime
import plotly.graph_objs as go

# App Title
st.title("📊 Stock Market Analyzer (Powered by yFinance)")

# Sidebar info
st.sidebar.markdown("### Enter stock symbol and date range")

# --- Input Fields ---
ticker_symbol = st.sidebar.text_input("Ticker Symbol (e.g. AAPL, GOOGL, TSLA)", "AAPL")
start_date = st.sidebar.date_input("Start Date", datetime.date(2019, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date(2022, 12, 31))

# Fetch Data
ticker_data = yf.Ticker(ticker_symbol)
df = ticker_data.history(start=start_date, end=end_date)

# Display Data
st.subheader(f"Showing data for: {ticker_symbol}")
st.write(f"From **{start_date}** to **{end_date}**")
st.dataframe(df.tail())

# Download Option
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv().encode('utf-8')

csv = convert_df_to_csv(df)
st.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name=f'{ticker_symbol}_data.csv',
    mime='text/csv',
)

# --- Info Panel ---
st.subheader("Company Info")
info = ticker_data.info
st.markdown(f"""
- **Company**: {info.get('longName', 'N/A')}
- **Industry**: {info.get('industry', 'N/A')}
- **Market Cap**: {info.get('marketCap', 'N/A')}
- **Sector**: {info.get('sector', 'N/A')}
- **Website**: [{info.get('website', '')}]({info.get('website', '')})
""")

# --- Statistics ---
st.subheader("📈 Summary Statistics")
st.write(df.describe())

# --- Charts ---
st.subheader("📊 Stock Charts")

chart_option = st.multiselect(
    "Select chart(s) to view:",
    ['Closing Price', 'Volume', 'Candlestick Chart', 'Moving Averages'],
    default=['Closing Price']
)

# --- Closing Price Line Chart ---
if 'Closing Price' in chart_option:
    st.write("### 📉 Closing Price Over Time")
    st.line_chart(df['Close'])

# --- Volume Chart ---
if 'Volume' in chart_option:
    st.write("### 📊 Volume Over Time")
    st.line_chart(df['Volume'])

# --- Candlestick Chart ---
if 'Candlestick Chart' in chart_option:
    st.write("### 🕯️ Candlestick Chart")
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name='Candlestick'
    )])
    fig.update_layout(xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)

# --- Moving Averages ---
if 'Moving Averages' in chart_option:
    st.write("### 📐 Moving Averages (SMA & EMA)")

    sma_window = st.slider("SMA Window (days)", 5, 100, 20)
    ema_window = st.slider("EMA Window (days)", 5, 100, 20)

    df['SMA'] = df['Close'].rolling(window=sma_window).mean()
    df['EMA'] = df['Close'].ewm(span=ema_window, adjust=False).mean()

    st.line_chart(df[['Close', 'SMA', 'EMA']])

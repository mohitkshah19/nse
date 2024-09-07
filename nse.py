import streamlit as st
import yfinance as yf

# Title for the app
st.title('NSE Stock Price & Fundamental Analysis')

# Sidebar for user input
st.sidebar.header('User Input')

# Get stock symbol from user input
stock_symbol = st.sidebar.text_input('Enter NSE Stock Symbol', 'RELIANCE')

# Fetch stock price and fundamental data from Yahoo Finance
def get_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol + '.NS')
        stock_info = stock.info
        return stock_info
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

# Display stock price
if st.sidebar.button('Get Stock Price'):
    stock_data = get_stock_data(stock_symbol)
    if stock_data:
        st.write(f"### {stock_symbol} Latest Price: ₹{stock_data.get('regularMarketPrice', 'N/A')}")

# Display stock fundamentals
if st.sidebar.button('Get Fundamental Analysis'):
    stock_data = get_stock_data(stock_symbol)
    if stock_data:
        st.write('### Fundamental Analysis:')
        st.write(f"**Market Cap:** ₹{stock_data.get('marketCap', 'N/A')}")
        st.write(f"**PE Ratio:** {stock_data.get('trailingPE', 'N/A')}")
        st.write(f"**Dividend Yield:** {stock_data.get('dividendYield', 'N/A')}")
        st.write(f"**52-Week High:** ₹{stock_data.get('fiftyTwoWeekHigh', 'N/A')}")
        st.write(f"**52-Week Low:** ₹{stock_data.get('fiftyTwoWeekLow', 'N/A')}")
        st.write(f"**Total Revenue:** ₹{stock_data.get('totalRevenue', 'N/A')}")
        st.write(f"**Free Cashflow:** ₹{stock_data.get('freeCashflow', 'N/A')}")

# Option to display complete financials
if st.sidebar.checkbox('Show Full Financial Data'):
    stock = yf.Ticker(stock_symbol + '.NS')
    st.write("### Balance Sheet")
    st.write(stock.balance_sheet)
    st.write("### Cash Flow")
    st.write(stock.cashflow)
    st.write("### Income Statement")
    st.write(stock.financials)

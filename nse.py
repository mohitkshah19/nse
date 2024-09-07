import streamlit as st
from nsetools import Nse
import yfinance as yf
import pandas as pd

# Initialize NSE object
nse = Nse()

# Title for the app
st.title('NSE Stock Price & Fundamental Analysis')

# Sidebar for user input
st.sidebar.header('User Input')

# Get stock symbol from user input
stock_symbol = st.sidebar.text_input('Enter NSE Stock Symbol', 'RELIANCE')

# Fetch stock price from NSE
def get_stock_price(symbol):
    try:
        stock_data = nse.get_quote(symbol.lower())
        return stock_data['lastPrice']
    except Exception as e:
        st.error("Error fetching data from NSE.")
        return None

# Fetch stock fundamental data from Yahoo Finance
def get_fundamentals(symbol):
    stock = yf.Ticker(symbol + '.NS')
    stock_info = stock.info
    return stock_info

# Display stock price
if st.sidebar.button('Get Stock Price'):
    price = get_stock_price(stock_symbol)
    if price:
        st.write(f'### {stock_symbol} Latest Price: ₹{price}')

# Display stock fundamentals
if st.sidebar.button('Get Fundamental Analysis'):
    fundamentals = get_fundamentals(stock_symbol)
    if fundamentals:
        st.write('### Fundamental Analysis:')
        st.write(f"**Market Cap:** ₹{fundamentals.get('marketCap', 'N/A')}")
        st.write(f"**PE Ratio:** {fundamentals.get('trailingPE', 'N/A')}")
        st.write(f"**Dividend Yield:** {fundamentals.get('dividendYield', 'N/A')}")
        st.write(f"**52-Week High:** ₹{fundamentals.get('fiftyTwoWeekHigh', 'N/A')}")
        st.write(f"**52-Week Low:** ₹{fundamentals.get('fiftyTwoWeekLow', 'N/A')}")
        st.write(f"**Total Revenue:** ₹{fundamentals.get('totalRevenue', 'N/A')}")
        st.write(f"**Free Cashflow:** ₹{fundamentals.get('freeCashflow', 'N/A')}")

# Option to display complete financials
if st.sidebar.checkbox('Show Full Financial Data'):
    stock = yf.Ticker(stock_symbol + '.NS')
    st.write("### Balance Sheet")
    st.write(stock.balance_sheet)
    st.write("### Cash Flow")
    st.write(stock.cashflow)
    st.write("### Income Statement")
    st.write(stock.financials)

import streamlit as st
import pandas as pd
import yfinance as yf

# Function to get stock data
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")
    return hist

# Function to display stock recommendations
def display_recommendations():
    st.title("Stock Recommendation App")
    
    st.sidebar.header("User Input")
    ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL")
    
    if ticker:
        data = get_stock_data(ticker)
        st.write(f"Stock data for {ticker}")
        st.line_chart(data['Close'])
        
        # Simple recommendation logic (for demonstration purposes)
        if data['Close'][-1] > data['Close'].mean():
            st.success(f"Recommendation: Buy {ticker}")
        else:
            st.warning(f"Recommendation: Sell {ticker}")

# Main function
if __name__ == "__main__":
    display_recommendations()

import streamlit as st
import yfinance as yf
from datetime import datetime
import openai  
import requests

st.title('Interactive Financial Stock Market Comparative Analysis Tool')

# Secure OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to fetch stock data
@st.cache_data
def get_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Sidebar for user inputs
st.sidebar.header('User Input Options')

# Stock tickers
selected_stock = st.sidebar.text_input('Enter Stock Ticker 1', 'AAPL').upper()
selected_stock2 = st.sidebar.text_input('Enter Stock Ticker 2', 'GOOGL').upper()

# Date range selection
start_date = st.sidebar.date_input('Start Date', datetime(2024, 9, 1))
end_date = st.sidebar.date_input('End Date', datetime(2024, 9, 30))

# Validate date input
if start_date > end_date:
    st.sidebar.error('Error: End date must fall after start date.')
else:
    # Fetch stock data
    stock_data = get_stock_data(selected_stock, start_date, end_date)
    stock_data2 = get_stock_data(selected_stock2, start_date, end_date)

    col1, col2 = st.columns(2)

    # Display stock data and charts
    with col1:
        st.subheader(f"Displaying data for: {selected_stock}")
        st.write(stock_data)
        chart_type = st.sidebar.selectbox(
            f'Select Chart Type for {selected_stock}', ['Line', 'Bar']
        )
        if chart_type == 'Line':
            st.line_chart(stock_data['Close'])
        elif chart_type == 'Bar':
            st.bar_chart(stock_data['Close'])

    with col2:
        st.subheader(f"Displaying data for: {selected_stock2}")
        st.write(stock_data2)
        chart_type2 = st.sidebar.selectbox(
            f'Select Chart Type for {selected_stock2}', ['Line', 'Bar']
        )
        if chart_type2 == 'Line':
            st.line_chart(stock_data2['Close'])
        elif chart_type2 == 'Bar':
            st.bar_chart(stock_data2['Close'])

    # OpenAI Analysis
    if st.button('Comparative Performance'):
        # Prepare a concise summary to stay within token limits
        stock_summary = stock_data['Close'].describe().to_dict()
        stock_summary2 = stock_data2['Close'].describe().to_dict()

        # Create a prompt with the summaries
        prompt = (
            f"Analyze and compare the performance of {selected_stock} and {selected_stock2} stocks "
            f"from {start_date} to {end_date}. "
            f"Here are the summary statistics for {selected_stock}: {stock_summary}. "
            f"And for {selected_stock2}: {stock_summary2}. "
            f"Provide a detailed comparative analysis with highlights and a conclusion."
        )

        # Prepare the messages for chat completion
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a financial analyst who provides detailed comparative analyses "
                    "of stock performance based on summary statistics. Your output should be "
                    "in markdown format."
                )
            },
            {"role": "user", "content": prompt}
        ]

        # Make the API call using the 'requests' library
        import json

        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {openai.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-4o-mini",
            "messages": messages,
            "max_tokens": 1024,
            "temperature": 0.7
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            # Access and display the analysis
            generated_text = result["choices"][0]["message"]["content"]
            st.markdown(generated_text)
        else:
            st.error(f"Request failed with status code {response.status_code}: {response.text}")

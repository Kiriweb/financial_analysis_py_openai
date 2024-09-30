# Interactive Financial Stock Market Comparative Analysis Tool

This repository contains an interactive financial analysis application built with **Streamlit**, **yfinance**, and the **OpenAI API**. The tool enables users to compare and analyze the performance of two stocks over a customizable date range, providing both visualizations and AI-generated comparative reports.

## Features

- **Customizable Date Range**: Select any start and end dates to analyze stock performance over specific periods.
- **Stock Comparison**: Input two stock tickers to compare their historical data side by side.
- **Interactive Charts**: Choose between line and bar charts to visualize closing prices for each stock.
- **AI-Powered Analysis**: Generate detailed comparative analyses using OpenAI's GPT-3.5-turbo model, highlighting key performance metrics and providing a comprehensive conclusion.
- **Secure API Integration**: Handles OpenAI API keys securely using Streamlit's secrets management to protect sensitive information.

## Technologies Used

- **Python 3**
- **Streamlit**
- **yfinance**
- **OpenAI API**
- **Requests Library**

## Getting Started

### Prerequisites

- **Python 3.x** installed on your system.
- An **OpenAI API key**. You can obtain one by signing up on the [OpenAI website](https://openai.com/).

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your_username/financial_analysis_yp_openai.git
   cd financial_analysis_yp_openai
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key**

   - Create a `.streamlit` directory in the root of your project:

     ```bash
     mkdir .streamlit
     ```

   - Inside `.streamlit`, create a `secrets.toml` file:

     ```bash
     echo "OPENAI_API_KEY = 'your_openai_api_key_here'" > .streamlit/secrets.toml
     ```

   - **Important**: Replace `'your_openai_api_key_here'` with your actual OpenAI API key.

### Running the Application

```bash
streamlit run Financial-Analysis-Tool.py
```

## Usage

1. **Select Stock Tickers**

   - Enter two stock ticker symbols in the sidebar (e.g., `AAPL` for Apple, `GOOGL` for Alphabet Inc.).

2. **Choose Date Range**

   - Select the start and end dates for your analysis.

3. **Customize Charts**

   - Choose the type of chart (Line or Bar) for each stock to visualize their closing prices.

4. **Generate AI Analysis**

   - Click on the **Comparative Performance** button to generate an AI-powered comparative analysis of the two stocks.


## Acknowledgments

- Inspired by financial analysts and data scientists who make complex data accessible.
- Thanks to the developers of Streamlit, yfinance, and OpenAI for their powerful tools.

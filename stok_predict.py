import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2014-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Prediksi Harga Saham')

stocks = ('BBRI.JK', 'BBCA.JK', 'BBNI.JK', 'BMRI.JK', 'BRIS.JK')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 5)
period = n_years * 365

@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

# Raw data column
raw_data_col, forecast_col = st.columns(2)

with raw_data_col:
    st.subheader('Raw data')
    st.write(data.tail())
    # Plot raw data
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

# Forecast column
with forecast_col:
    st.subheader('Forecast data')
    st.write(forecast.tail())
    
    st.write(f'Forecast plot for {n_years} years')
    fig1 = plot_plotly(m, forecast)
    # Adjust plot dimensions for mobile
    fig1.update_layout(height=400, width=600)
    st.plotly_chart(fig1)

    st.write("Forecast components")
    fig2 = m.plot_components(forecast)
    # Adjust plot dimensions for mobile

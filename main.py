import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

st.title('Weather Forecasdt for the Next Days')

place = st.text_input('Place:', key='text')
days = st.slider('Forecast Days', min_value=1, max_value=5, help='Select the number of days', key='value')

options = st.selectbox('Select data to view', ['Temperature', 'Sky'], key='box')

if place:
    st.subheader(f'{options} for the next {days} days in {place}')
    figure = px.line(x=['a', 'b', 'c'], y=[9, 10, 12], labels={'x': 'Date', 'y': 'Temperature(C)'})
    st.plotly_chart(figure)

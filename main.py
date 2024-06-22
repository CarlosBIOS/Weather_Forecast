import streamlit as st
import plotly.express as px
from backend import get_data
from glob import glob

st.set_page_config(layout='wide')

st.title('Weather Forecast for the Next Days')

place: str = st.text_input('Place:', key='text', help='Escreve uma cidade válida')
days: str = st.slider('Forecast Days', min_value=1, max_value=7, help='Select the number of days', key='value')

options: str = st.selectbox('Select data to view', ['Temperature', 'Sky'], key='box')

try:
    if place:
        st.subheader(f'{options} for the next {days} days in {place}')
        data_list: list = get_data(place, days, options)
        if options == 'Temperature':
            figure = px.line(x=data_list[1], y=data_list[0], labels={'x': 'Date', 'y': 'Temperature(C)'})
            st.plotly_chart(figure)
        else:
            images_list: list = glob('*.png')
            image_path = [f'{sky.casefold()}.png' for sky in data_list[0]]
            st.image(image_path, width=115)
except TypeError:
    st.write('Por favor, escreve uma cidade válida!')

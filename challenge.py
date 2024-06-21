import pandas
import streamlit as st
import plotly.express as px

data = pandas.read_csv('happy.csv')

st.title('In Search for Happiness')

x = st.selectbox('Select the data for the x axis', ['GDP', 'Happiness', 'Generosity'])
y = st.selectbox('Select the data for the y axis', ['GDP', 'Happiness', 'Generosity'])
print(type(x))

st.subheader(f'{x} and {y}')
figure = px.scatter(x=data[x.casefold()], y=data[y.casefold()], labels={'x': x, 'y': y})
st.plotly_chart(figure)

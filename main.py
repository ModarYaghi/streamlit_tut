import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Super Simple Title")
st.header("This a Header")
st.subheader("Subheader")
st.caption("small text")

code_render = """"
def my_func(name):
    print('Hello', name)
"""
st.code(code_render, language="python")

st.divider()
st.image(os.path.join(os.getcwd(), "static", "Modar_Arc.png"), width=100)
st.divider()

pressed = st.button("Press me")
print(pressed)

st.divider()

# Title
st.title("Streamlit Charts Demo")

# Generate sample data
chart_data = pd.DataFrame(
   np.random.randn(20, 3),
   columns = ['A', 'B', 'C']
)
# st.dataframe(chart_data)
st.data_editor(chart_data)
st.subheader("Static Table")
st.table(chart_data)
# Area Chart Section
st.subheader("Area Chart")
st.area_chart(chart_data)

# Bar Chart Section
st.subheader("Bar Chart")
st.bar_chart(chart_data)

# Line Chart Seciton
st.subheader("Line Chart")
st.line_chart(chart_data)

# Scatter Chart Section
st.subheader("Scatter Chart")
scatter_data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})
st.scatter_chart(scatter_data)

# Map Section (displaying random points on map)
st.subheader("Map")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4], # coordinates around SF
    columns=['lat', 'lon']
)
st.map(map_data)

# Pyplot Section
st.subheader("Pyplot Chart")
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label='A')
ax.plot(chart_data['B'], label='B')
ax.plot(chart_data['C'], label='C')
ax.set_title("Pyplot Line Chart")
ax.legend()
st.pyplot(fig)
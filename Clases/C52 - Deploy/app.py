import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(np.random.randn(10, 20),columns=[f'col {i}' for i in range(20)])

st.dataframe(dataframe.style.highlight_max(axis=0))
st.table(dataframe)

map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
st.map(map_data)
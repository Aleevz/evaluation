import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns([3, 1])

# sample data
data = np.random.randn(10, 1)

col1.subheader("Example Chart location")

# change this to pyplot implementation
col1.line_chart(data)

col2.subheader("Which school had the lowest number absences in February?")
col2.write(['School 5', 'School 2', 'School 8', 'School 6'])

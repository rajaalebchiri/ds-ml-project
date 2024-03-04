#!/user/bin/env python

import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import seaborn as sns

st.set_page_config(page_title="SAMPLE WEB APP", page_icon=None, layout="wide")

st.markdown("# First Streamlit UI Web Application")

data = pd.read_csv("./data/population_csv.csv")

data.comuns = data.columns.str.upper()

st.write("### 1. Overview of the Data")

st.dataframe(data, use_container_width=True)

st.write("### 2. Understanding the Data")

selected = st.sidebar.radio("**What do you want to know about the data?**",
                    ["Description", "Data Sample", "Data Head/Tail", "Data Shape"])

if selected == "Description":
    st.dataframe(data.describe(), use_container_width=True)

elif selected == "Data Sample":
    st.dataframe(data.sample(10), use_container_width=True)

elif selected == "Data Head/Tail":
    st.dataframe(data.head(), use_container_width=True)

else:
    st.write('###### The shape of the data is :', data.shape)

tab1, tab2 = st.tabs(["PANDAS PROFILE ANALYSIS", "SWEETVIZ ANALYSIS"])
import streamlit as st,numpy as np,pandas as pd

file = st.file_uploader("upload",type=["csv"])

if file:
    df = pd.read_csv("BostonHousing.csv")
    st.dataframe(df)
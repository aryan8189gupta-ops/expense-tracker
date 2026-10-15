import streamlit as st,numpy as np,pandas as pd

file = st.file_uploader("upload your csv files",type=["csv"])
if file:
    st.subheader(f"table : {file.name}")
    df = pd.read_csv(file)
    st.dataframe(df,use_container_width=True)
   
    cities = df["Spending_Score"].unique()
    selected_city = st.selectbox("Filter by cities",cities)
    filtered_data = df[df["Spending_Score"] == selected_city]
    st.dataframe(filtered_data)
    
  
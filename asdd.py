import streamlit as st,pandas as pd, numpy as np 
st.title("chai taste Poll")
col1,col2 = st.columns(2)

with col1:
    st.header("masala chai !!")
    vote1 = st.button("vote masala chai")  
      
with col2:
    st.header("Adrak chai!!")
    vote2 = st.button("vote adrak chai")
    
if vote1:
    st.success("fegg")

if vote2:
    st.success("berberhrth")
    
with st.expander("show chai making instructions"):
    st.write("""
      1. boil water with tea leaves
      2. errgrgg
      3. rgrggrgg
      4. ergrgggggggg
      5. gergergergergegerg
             
    
    
""")
             
        
   
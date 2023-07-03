import streamlit as st

sample_data = [3.12, -4.31, 6.76, -9.88, 1.09]
col1, col2 = st.columns([2,5]) # Structured display of items

col1.subheader("Line Chart")
col1.line_chart(sample_data)

col2.subheader("Area Chart")
col2.area_chart(sample_data)
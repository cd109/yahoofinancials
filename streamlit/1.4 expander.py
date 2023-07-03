import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({"Mammal": ["Sea Lion", "Seal", "Walrus"], "Count": [3, 5, 2]})

st.dataframe(df)
with st.expander("Click to see a bar graph of the above data"): #exandler is similar to checkbox to control what’s displayed to users
    fig, ax = plt.subplots()
    ax.set_title("Mammal Count")
    ax = sns.barplot(x="Mammal", y="Count", data=df)
    st.pyplot(fig)

import streamlit as st
import pandas as pd

df1 = pd.DataFrame({"Cats": ["Lion", "Tiger", "Leopard"],
               "Raptors": ["Eagle", "Falcon", "Hawk"],
               "Snakes": ["Viper", "Anaconda", "Python"]})

df2 = pd.DataFrame({"Cats": ["Jaguar", "Panther"],
               "Raptors": ["Osprey", "Kite"],
               "Snakes": ["Cobra", "Boomslang"]})

st.dataframe(df1)
st.dataframe(df2)

df = st.dataframe(df1)
df.add_rows(df2) #add_rows() method allows us to do this through a process called mutation. 

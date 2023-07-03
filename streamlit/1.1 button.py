import streamlit as st
import pandas as pd

st.button("Click button") #On its own, the button widget isn’t that useful 

sample_data = {"Mammals": ["Cat", "Dog", "Bat", "Fox", "Pig"],
               "Birds": ["Parrot", "Eagle", "Duck", "Pegeon", "Vulture"]}
df = pd.DataFrame(sample_data)

st.dataframe(df)

if st.button("Click to show only mammals"): #Activate actions  to make our web application interactive 
    st.dataframe(df["Mammals"])
	
if st.button("Click to show only birds"): #usefulness of the button widget when combined with other actions. 
    st.dataframe(df["Birds"])

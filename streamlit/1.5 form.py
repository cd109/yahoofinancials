import streamlit as st

with st.form("Order Form"): #Form to collect the details of a purchase order 
    st.write("Order Details")
    fruit = st.select_slider("Select a fruit",
                             ["Banana", "Pawpaw", "Guava", "Mango"])

    quantity = st.number_input("Select the number of fruits", min_value=0)

    city = st.text_input("Type in your city")

    submitted = st.form_submit_button("Submit") #Each form has its own button—st.form_submit_button()— that transmits the data once it’s clicked 

    if submitted:
        st.write("You have ordered {} {}(s) to be picked up at the {} branch"
                 .format(quantity, fruit, city))

st.write("These values, {}, {}, and {}, that were set inside the form are\
         accessible outside the form".format(quantity, fruit, city))
import streamlit as st


integer_number = st.number_input("Enter an integer",
                                 min_value=-10,
                                 max_value=10,
                                 value=0)  #st.number: This widget enables users to type in the numbers directly. we can set it up to accept integers or floats, depending on how we specify the input parameters.
st.write(integer_number, type(integer_number))

float_number = st.number_input("Enter a float",
                               min_value=-1.0,
                               max_value=1.0,
                               value=0.0)
st.write(float_number, type(float_number)) # It also has “+” and “-” keys to increment and decrement values. The change happens in terms of the steps specified. If none is specified, the step is 1 for integers and 0.01 for floats.
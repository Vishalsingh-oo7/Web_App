
import streamlit as st

st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.write("This is the coolest webapp!")
st.badge("Web App!")

# New header for Vishal
st.header("_Dear Vishal - You are So Strong! :blue[cool] :sunglasses:")
st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

# Now we will read the CSV file
import pandas as pd

# this is the path to your CSV file
df = pd.read_csv(r"C:\Users\LENOVO\Desktop\MLOps\Web_App\cars24-car-price (3).csv")

# It just prints the text as normal output
st.write("Here is the data from the CSV file:")

# You can also use st.table(df) to display it as a table 
#Specifically designed to display data tables
st.dataframe(df)

#https://docs.streamlit.io/develop/api-reference/widgets

agree = st.checkbox("Am I Awesome?")

if agree:
    st.write("You have a good taste!")
# Button adding to the app
st.button("Reset", type="primary")
# Button with a callback function
if st.button("Say hello"):
    st.write("You clicked on the button")
else:
    st.write("Button is untouched")

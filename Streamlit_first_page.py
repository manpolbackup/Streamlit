import streamlit as st
import mymodel as m

st.title("My First Streamlit Web Page")
st.header("Welcome to my app")
st.text("This is a simple web page built with Streamlit.")

st.button("Click Me")

st.slider("Pick a number", 0, 100)

st.radio("Choose an option", ["A", "B", "C"])

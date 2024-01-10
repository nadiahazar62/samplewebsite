import streamlit as st

def show_about_us():
    st.header("About Us")
    st.write("We are an awesome company doing amazing things.")
    st.image("your_about_us_image.jpg", caption="Company Image", use_column_width=True)

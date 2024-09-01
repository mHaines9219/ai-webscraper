import streamlit as st


st.title("AI Web Scraper")

url = st.text_input("Enter the URL")

if st.button("Scrape"):
    st.write("Scraping the URL")
else:
    st.write("Please enter the URL")

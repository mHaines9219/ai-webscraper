import streamlit as st
from scrape import (
    scrape_website,
    extract_body,
    clean_body,
    split_dom_content,
)


st.title("AI Web Scraper")

url = st.text_input("Enter the URL")

if st.button("Scrape"):
    st.write("Scraping the URL")
    result = scrape_website(url)
    body_content = extract_body(result)
    cleaned_content = clean_body(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("Show content"):
        st.text_area("DOM Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing content")

            dom_chunks = split_dom_content(st.session_state.dom_content)

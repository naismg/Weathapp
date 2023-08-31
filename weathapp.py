import streamlit as st

#config de la page
st.set_page_config(
    layout="wide"
)

st.map()

col1, col2 = st.columns(2, gap="large")
with col1 :
    city_name = st.text_input("Your City")
    search_button = st.button("Search")

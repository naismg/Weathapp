import streamlit as st

#config de la page
st.set_page_config(
    layout="wide"
)

# Functions
## To show map with a dataframe in input
def show_map(data_map) :
    st.map(data_map)

## To show temperature with fancy front-end
def show_temperature(temperature) :
    st.metric("Temperature",temperature)

## To show wind strenght with fancy front-end
def show_wind(wind) :
    st.metric("Wind",wind)

def show_humidity(humidity) :
    st.metric("Humidity",humidity)

def button(text_button):
    st.button(text_button)

# Front-end
col1, col2 = st.columns(2, gap="large")

with col1 :
    show_map()
    city_name = st.text_input("Your City")
    button(text_button="Search")

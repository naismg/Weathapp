import pytest

def test_show_map(mocker):
    data_map = {'latitude': [37.76], 'longitude': [-122.4]}
    mocker.patch('streamlit.map')
    show_map(data_map)
    st.map.assert_called_once_with(data_map)

def test_show_temperature(mocker):
    temperature = 25
    mocker.patch('streamlit.metric')
    show_temperature(temperature)
    st.metric.assert_called_once_with("Temperature", temperature)

def test_show_wind(mocker):
    wind = 10
    mocker.patch('streamlit.metric')
    show_wind(wind)
    st.metric.assert_called_once_with("Wind", wind)

def test_show_humidity(mocker):
    humidity = 50
    mocker.patch('streamlit.metric')
    show_humidity(humidity)
    st.metric.assert_called_once_with("Humidity", humidity)

def test_button(mocker):
    text_button = "Click me"
    mocker.patch('streamlit.button')
    button(text_button)
    st.button.assert_called_once_with(text_button)

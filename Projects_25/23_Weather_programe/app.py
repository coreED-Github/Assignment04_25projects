import streamlit as st
import requests
import matplotlib.pyplot as plt
import time
from datetime import datetime

# Set Streamlit page config
st.set_page_config(
    page_title="Weather Forecast App",
    page_icon="🌤",
    layout="wide"
)

# API Key and base URL for OpenWeatherMap
api_key = "e7f70be0a280dd041ae7cb1369ecfc3c"  # Replace with your own OpenWeatherMap API key
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Title of the app
st.title("Interactive Weather App")

# Input box to take city name from the user
city = st.text_input("Enter city name", "")

# If city is entered
if city:
    with st.spinner("Fetching weather data..."):
        time.sleep(2)  # Simulating delay for fetching data
        complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
        response = requests.get(complete_url)
        data = response.json()

        if response.status_code == 200 and data.get("cod") == 200:
            main_data = data["main"]
            weather_data = data["weather"][0]
            temp = main_data["temp"]
            pressure = main_data["pressure"]
            humidity = main_data["humidity"]
            description = weather_data["description"]
            icon_code = weather_data["icon"]
            weather_icon = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

            # Displaying weather data
            st.image(weather_icon, width=100)  # Display weather icon
            st.write(f"Temperature: {temp}°C")
            st.write(f"Pressure: {pressure} hPa")
            st.write(f"Humidity: {humidity}%")
            st.write(f"Weather Description: {description.capitalize()}")

            # Change background color based on weather
            if description == "clear sky":
                st.markdown(
                    f"<div style='background-color: #f9e4b7; padding: 20px;'>"
                    f"<h2>{description.capitalize()} in {city}</h2></div>", unsafe_allow_html=True)
            elif "rain" in description:
                st.markdown(
                    f"<div style='background-color: #a0b0c0; padding: 20px;'>"
                    f"<h2>{description.capitalize()} in {city}</h2></div>", unsafe_allow_html=True)
            else:
                st.markdown(
                    f"<div style='background-color: #d0e7f1; padding: 20px;'>"
                    f"<h2>{description.capitalize()} in {city}</h2></div>", unsafe_allow_html=True)

            # Plotting temperature for a week (simulated)
            days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            temperatures = [temp + 2, temp - 1, temp + 3, temp, temp + 1, temp - 2, temp]
            plt.plot(days, temperatures)
            plt.title("Weekly Temperature Forecast")
            plt.xlabel("Day")
            plt.ylabel("Temperature (°C)")
            st.pyplot(plt)

            # Showing the current time and date
            st.write(f"Current Date and Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        else:
            st.error("City not found! Please enter a valid city name.")
else:
    st.info("Please enter a city to get the weather information.")
import tkinter as tk
import requests

API_KEY = "0cb6317fbf6590598a90ac1ffb27d5c8"

def get_weather():
# This function runs when the "Get Weather" button is clicked
    city = city_entry.get()
    # Get the city name typed by the user in the input box

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    # Create the weather API URL using city name and API key

    response = requests.get(url)
    # Send request to OpenWeather website to get weather data
    data = response.json()
    # Convert the response into Python dictionary format
    if data["cod"] == 200:
    # Check if the city exists (200 means success)
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result_label.config(
            text=f"City: {city}\n"
                 f"Temperature: {temperature}°C\n"
                 f"Condition: {condition.title()}\n"
                 f"Humidity: {humidity}%\n"
                 f"Wind Speed: {wind_speed} m/s"
        )
    else:
        result_label.config(text="City not found. Please try again.")

root = tk.Tk()
# root = tk.Tk() create the main application window
root.title("Weather App")
# root.title("Weather App") Sets the title text at the top of the window
root.geometry("300x300")
# root.geometry("300x300") Sets the size of the window to 300x300 pixels / Sets window size

tk.Label(root, text="Enter City Name:", font=("Helvetica", 12)).pack(pady=5)
"""
tk.Label - Creates a text label
root - Tells Python: place this label inside the main window
text="Enter City:" - Text shown to the user
font=("Helvetica", 12) - Font name and size
.pack(pady=5) - Places the label on the screen Adds vertical space above and below (5 pixels)
"""

city_entry = tk.Entry(root, font=("Helvetica", 12))
# It Creates a text input box and user types city name here that is stored in variable city_entry
city_entry.pack(pady=5)
# It Displays the input box in the window that adds vertical spacing ex: [ Islamabad ]

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)
"""
tk.Button - Creates a clickable button
root - Places the button inside the main window
text="Get Weather" - Text shown on the button
command=get_weather - Calls the get_weather function when clicked / When clicked → run get_weather() function
.pack(pady=10) - Places button on screen and Adds spacing
"""

result_label = tk.Label(root, text="", font=("Helvetica, 12"), justify="left")
# It Creates a label to show weather the results. It Starts empty (text=""). The justify="left" aligns text to left.
# This is where weather data appears later.
result_label.pack(pady=10)
# It displays result label in window and adds spacing

root.mainloop()
# root.mainloop() Starts the Tkinter event loop / Keeps the window open and waits for user interaction
# Without this line, the window would close immediately after opening

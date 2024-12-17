# Import necessary libraries
from tkinter import ttk  # For advanced widgets like Combobox
import tkinter as tk  # For basic GUI elements
import requests  # For making HTTP requests to the API


# Define the function to fetch and display weather data
def data_fetch():
    """
    Fetches weather data from the OpenWeatherMap API and displays it in the GUI.
    """
    city = city_name.get()  # Get the city name entered by the user
    # Make API request - Note: Replace 'YOUR_API_KEY' with your actual API key
    data = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=a6a329b7764f2c0636eb4ccb95d2eab2"
    ).json()

    # Update labels with fetched data.  The API returns data in Kelvin, so we convert to Celsius.
    climate_labe2.config(text=data["weather"][0]["main"])  # Display main weather condition (e.g., "Clouds")
    desc_label2.config(text=data["weather"][0]["description"])  # Display weather description (e.g., "scattered clouds")
    temp_label2.config(text=str(int(data["main"]["temp"] - 273.15)) + "°C")  # Display temperature in Celsius
    pres_label2.config(text=str(data["main"]["pressure"]))  # Display atmospheric pressure



# Create main application window
root = tk.Tk()
root.title("Shahbaz Weather App")  # Set window title
root.configure(background="light blue")  # Set background color


# Create and place main label
msg_label = tk.Label(root, text="Shahbaz Weather App", width=50, font=("Arial", 18))  # Main app label
msg_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)  # Position the label


# Create and place the city selection combobox
city_name = tk.StringVar()  # Variable to store the selected city
list_name = [
    "Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
    "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
    "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh",
    "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"
]
combo = ttk.Combobox(root, width=50, font=("bold", 18), values=list_name, textvariable=city_name) # Create the combobox
combo.grid(row=1, column=0, columnspan=2, padx=10, pady=10)  # Position the combobox


# Create and place labels for displaying weather information
climate_label = tk.Label(root, text="Weather Climate", font=("bold", 15), width=25)
climate_label.grid(row=4, column=0, pady=10)

climate_labe2 = tk.Label(root, text="", font=("bold", 15), width=25)  # Label to display climate data
climate_labe2.grid(row=4, column=1, pady=10)


desc_label = tk.Label(root, text="Weather Description", font=("bold", 15), width=25)
desc_label.grid(row=5, column=0, pady=10)

desc_label2 = tk.Label(root, text="", font=("bold", 15), width=25) # Label to display description data
desc_label2.grid(row=5, column=1, pady=10)


temp_label = tk.Label(root, text="Temperature", font=("bold", 15), width=25)
temp_label.grid(row=6, column=0, pady=10)

temp_label2 = tk.Label(root, text="", font=("bold", 15), width=25) # Label to display temperature data
temp_label2.grid(row=6, column=1, pady=10)


pres_label = tk.Label(root, text="Pressure", font=("bold", 15), width=25)
pres_label.grid(row=7, column=0)

pres_label2 = tk.Label(root, text="", font=("bold", 15), width=25) # Label to display pressure data
pres_label2.grid(row=7, column=1, pady=10)


# Create and place the "Done" button
btn = tk.Button(root, text="Done", font=("bold", 15), width=25, command=data_fetch)  # Button to trigger data fetching
btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


# Start the Tkinter main loop
root.mainloop()

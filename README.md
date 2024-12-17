# Simple Weather App using Tkinter and OpenWeatherMap API

This project is a simple weather application built using Python, Tkinter, and the OpenWeatherMap API. It was created as a learning exercise to explore GUI development with Tkinter and API integration.

## Project Overview

This application allows users to input a city name and retrieve current weather information for that city.  It displays the main weather condition, a brief description, the temperature (in Celsius), and the atmospheric pressure.

## Features

* **User-friendly GUI:** Simple and intuitive interface built with Tkinter.
* **Real-time weather data:** Fetches current weather data using the OpenWeatherMap API.
* **Clear display:** Presents weather information in an easy-to-read format.
* **City Selection:** Provides a combobox to choose from a list of Indian states and union territories.

## Learning Experience

This project provided valuable experience in several areas:

* **Tkinter:**  I learned how to create basic GUI elements like labels, buttons, and comboboxes using Tkinter.  I also gained experience with layout management using the `grid` system.
* **API Integration:** I learned how to make HTTP requests to an external API (OpenWeatherMap) using the `requests` library. This involved understanding how to construct API requests, handle responses, and parse JSON data.
* **Data Handling and Display:** I practiced working with dictionaries and extracting specific data points from the API response. I also learned how to update Tkinter widgets dynamically to display the fetched data.
* **Error Handling:** Although not fully implemented in this version, the project highlighted the importance of robust error handling when dealing with external APIs and user input.

## Future Improvements

* **Improved Error Handling:** Implement more comprehensive error handling to gracefully handle API errors (e.g., invalid city names, network issues).
* **More Detailed Weather Information:** Include additional weather details such as humidity, wind speed, and sunrise/sunset times.
* **Enhanced GUI:**  Improve the visual design and layout of the application.
* **Location-Based Search:**  Add functionality to automatically detect the user's location.
* **Unit Conversion:** Allow users to choose between Celsius and Fahrenheit.

## How to Run

1. **Install Required Libraries:**  Ensure you have `tkinter` and `requests` installed. You can install them using pip:
   ```bash
   pip install requests
2. **Get an OpenWeatherMap API Key:** You'll need a free API key from OpenWeatherMap. Replace `"a6a329b7764f2c0636eb"` with your actual key.
3. **Run the script:** Execute the Python script (`test1.py`).

## Conclusion
This simple weather app project was a fantastic learning experience. It provided a practical introduction to GUI development with Tkinter and API interaction. While the project is basic, it serves as a solid foundation for building more complex applications in the future.
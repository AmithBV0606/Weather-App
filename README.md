# Weather App

This is a Python-based Weather App that retrieves and displays the current temperature in Celsius and Fahrenheit for a city entered by the user. It uses the WeatherAPI service to obtain real-time weather data.

## Project Overview

This project utilizes the `requests` library to make API requests and retrieve weather information in JSON format. Users can enter the name of any city and receive the current temperature.

## Prerequisites

1. **Python 3.6 or higher**: Make sure you have Python installed on your system.
2. **`requests` library**: This library is required to make API requests.
3. **API Key from WeatherAPI**: You need an API key from WeatherAPI to access the weather data.

## Getting an API Key

1. Go to [WeatherAPI's website](https://www.weatherapi.com).
2. Sign up for a free account if you don’t already have one.
3. After logging in, go to the "My Account" section and find the "API Key" tab.
4. Copy the API key provided.

## Setting Up the Project

### 1. Clone the Repository (optional)

If you have the code in a repository, you can clone it. Otherwise, download the code directly.

```bash
git clone <repository-url>
```

### 2. Install Required Libraries

Open a terminal, navigate to the project directory, and install the required libraries with:

```bash
pip install requests python-dotenv
```

### 3. Set Up Environment Variables
- Create a .env file in the root directory of your project.

- Inside .env, add your API key:

```bash
API_KEY=your_api_key_here
```

**NOTE :** Replace your_api_key_here with the actual API key from WeatherAPI.

### 4. Run the Application

Now you’re ready to run the Python script. Start the app using:

```bash
python main.py
```

## Usage

1. The application will prompt you to enter the name of a city.

2. After entering the city name, the app will display:
    - Temperature in Celsius
    - Temperature in Fahrenheit

### Example Interaction

```bash
Enter city's name: London
Celsius: 15.0
Fahrenheit: 59.0
```

### Enjoy using your Python Weather App!

```javascript
Replace `<repository-url>` with your actual repository URL if you have one. This README includes everything needed to install, configure, and run the project locally.
```
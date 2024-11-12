import os
import requests
import json
from dotenv import load_dotenv, dotenv_values

# To accept the city's name from the user : 
city = input("Enter city's name : ")

# API : 
load_dotenv()
apiKey = os.getenv("API_KEY")
url = f"https://api.weatherapi.com/v1/current.json?key={apiKey}&q={city}"

# To receive the response from the API
res = requests.get(url) # res will be a string
data = json.loads(res.text) # converts to json(dictionary)
print("Celsius : ", data["current"]["temp_c"])
print("Fahrenheit : ", data["current"]["temp_f"])
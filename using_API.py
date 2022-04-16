
# Create Account on OpenWeatherMap & get the API 
# Using this API we can fetch the weather of any city  
# API_Key = '40274e8a50ea2afe0365228e9c448929'

import requests

api_key = '40274e8a50ea2afe0365228e9c448929'
city_name = input('Enter a city Name : ')
country_name = input('Enter your country name : ')
weather_address = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_name}&appid={api_key}'

url = weather_address 
response = requests.get(url)
# print(response.text) 
json_data = response.json()
print(json_data, '\n')
formated_data = json_data['weather'][0]['description']
print(formated_data)

# for key, value  in formated_data.items():
    # print( key , ':', value)
    

# Using wttr.in 
import requests

City_name = input('Please enter the city name whose weather you want to know : ')
print(City_name)

print(f'Displaying the weather report for : {City_name}')

url = f'https://wttr.in/{City_name}'
response = requests.get(url)

print(response.text)
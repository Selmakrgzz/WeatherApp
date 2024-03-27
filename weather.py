import requests
from dotenv import load_dotenv
import os
from pprint import pprint #Pretty print

load_dotenv()

#Uses API to get the weather information for the given city name
#Weather_data stores the weather information as a json
#This method returns the weather information as a json
def get_current_weather(city="Oslo"):
    requests_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    weather_data=requests.get(requests_url).json()

    return weather_data

#This will help us to run the weather app in the terminal
if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')
    
    city = input('\n Please enter a city name: ')

    #Check for emty strings or string with only spaces

    if not bool(city.strip()):
        city="Konya Province"
        
    #Calls the get_current_weather method and sends in the city name from user input
    weather_data=get_current_weather(city)

    print("\n")
    pprint(weather_data) #Prints the output in a readable format

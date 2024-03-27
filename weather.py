import requests
from dotenv import load_dotenv
import os
from pprint import pprint #Pretty print

load_dotenv()

def get_current_weather(city="Oslo"):
    requests_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    weather_data=requests.get(requests_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')
    
    city = input('\n Please enter a city name: ')

    #Check for emty strings or string with only spaces

    if not bool(city.strip()):
        city="Konya Province"
        


    weather_data=get_current_weather(city)

    print("\n")
    pprint(weather_data)

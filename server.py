from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

#Using Flask as framework for this project
app=Flask(__name__)

#When someone is entering the root address "/" or "/index"
#the flask application will return the index.html page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#When someone is entering the root address "/weather"
#the flask application will do the following
@app.route('/weather')
def get_weather():
    #Get's the city parameter from the url
    city=request.args.get('city')

    #Check for emty strings or string with only spaces
    #It will set city to konya province by default
    if not bool(city.strip()):
        city="Konya Province"
    
    #Retrives the weather information using the get_current_weather 
    #method from the weather.py file.
    #This variable will now store the weather information as a json
    weather_data=get_current_weather(city)

    #City is not found by API
    if not weather_data['cod'] == 200:
        #Returning the city not found html page where the user
        #get's the opurtunity to try again
        return render_template('city-not-found.html')

    #Returning the weather page to the user
    #title,status etc goes back to the weather html page
    #to be displayed for the user
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)

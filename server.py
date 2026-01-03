from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
     return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        # You could render "City not found." instead like below
        #city = "Fairfield"
        return render_template('missing.html')

    weather_data = get_current_weather(city)


    # City is not found by the API
    if not weather_data['cod'] == 200:
        return render_template('missing.html')
    
    #if not bool(weather_data['wind']['gust']):
    # return render_template(
    #     "weather1.html",
    #     title=weather_data["name"],
    #     status=weather_data["weather"][0]["description"].capitalize(),
    #     temp=f"{weather_data['main']['temp']:.1f}",
    #     feels_like=f"{weather_data['main']['feels_like']:.1f}",
    #     humidity=f"{weather_data['main']['humidity']:2.0f}",
    #     pressure=f"{weather_data['main']['pressure']:4.0f}",
    #     wind_speed=f"{weather_data['wind']['speed']:.1f}"
    #     )
    # else:    
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        humidity=f"{weather_data['main']['humidity']:2.0f}",
        pressure=f"{weather_data['main']['pressure']:4.0f}",
        wind_speed=f"{weather_data['wind']['speed']:.1f}",
        #wind_gust=f"{weather_data['wind']['gust']:.1f}"
        )
    

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)

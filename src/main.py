from flask import Flask, render_template, request
import datetime
import logging
import requests
import os

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
  
API_KEY = os.getenv("WEATHER_API_KEY")

LOCATIONS = {
    "Polska": ["Warszawa", "Kraków", "Gdańsk"],
    "Niemcy": ["Berlin", "Monachium", "Hamburg"],
    "Francja": ["Paryż", "Lyon", "Marsylia"]
}

@app.route("/", methods=["GET", "POST"])
def index():
    weather_info = None
    if request.method == "POST":
        country = request.form.get("country")
        city = request.form.get("city")
        if city:
            weather_info = get_weather(city)
    return render_template("index.html", locations=LOCATIONS, weather=weather_info)

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pl"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    else:
        return None

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    logger.info(f"Data uruchomienia: {datetime.datetime.now()}")
    logger.info("Autor: Yauheni Ivus")
    logger.info(f"Aplikacja nasłuchuje na porcie {port}")
    app.run(host="0.0.0.0", port=port)

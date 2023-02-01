from flask import Flask, render_template, request
import weather_app

app = Flask(__name__)

@app.route("/")
def index():
    location = None
    weather = None
    error = None
    return render_template("weather.html")

@app.route("/weather", methods=["POST"])
def weather():
    location = None
    weather = None
    error = None
    location = request.form["location"]
    weather = weather_app.get_weather(location)
    if weather:
        return render_template("weather.html", location=location, weather=weather)
    else:
        return render_template("weather.html", error="Sorry, no data available at this time")

if __name__ == "__main__":
    app.run()

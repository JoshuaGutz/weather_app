from flask import Flask, render_template
import weather_app

app = Flask(__name__)

@app.route("/")
def index():
    location = "London,UK"
    weather = weather_app.get_weather(location)
    return render_template("weather.html", location=location, weather=weather)

if __name__ == "__main__":
    app.run()

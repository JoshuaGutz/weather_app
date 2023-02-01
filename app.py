from flask import Flask, render_template, request
import weather_app

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    location = None
    weather = None
    error = None
    if request.method == "POST":
        location = request.form.get("location")
        try:
            weather = weather_app.get_weather(location)
        except Exception as e:
            error = "Sorry, no data available at this time"
    return render_template("weather.html", location=location, weather=weather, error=error)

if __name__ == "__main__":
    app.run()

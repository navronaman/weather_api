from flask import Flask, render_template
import pandas as pd

app = Flask("Website")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def page(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}

app.run(debug=True)

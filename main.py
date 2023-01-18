from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def page(station, date):
    if int(station) <= 100:
        station = str(station).zfill(6)
        df = pd.read_csv(f"data_small/TG_STAID{station}.txt", skiprows=20, parse_dates=["    DATE"])
        print(df)
        temp = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
        print(temp)
        return {"station": station,
                "date": date,
                "temperature": temp}
    elif int(station) >= 100:
        temperature = 23
        return {"message": "Error!"}
    else:
        return {"message": "Main andar se toot chuka hoon"}


if __name__ == "__main__":
    app.run(debug=True)

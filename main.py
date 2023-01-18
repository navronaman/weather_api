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
    if int(station) <= 100000:
        station = str(station).zfill(6)
        df = pd.read_csv(f"data/TG_STAID{station}.txt", skiprows=20, parse_dates=["    DATE"])

        if len(date) == 10:
            temp = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
            return {"station": station, "date": date, "temperature": temp}

        elif len(date) == 4:
            df["    DATE"] = df["    DATE"].astype(str)
            result = df[df["    DATE"].str.startswith(str(date))]
            print(result)

            return result.to_dict(orient="index")

    elif int(station) >= 100000:
        temperature = 23
        return {"message": "Error!"}
    else:
        return {"message": "Main andar se toot chuka hoon"}


@app.route("/api/v1/<station>")
def all_data(station):
    if int(station) <= 100000:
        station = str(station).zfill(6)
        df = pd.read_csv(f"data/TG_STAID{station}.txt", skiprows=20)
        result = df.to_dict(orient="index")
        return result
    elif int(station) >= 100000:
        return {"message": "Error!"}
    else:
        return {"message": "Main andar se toot chuka hoon"}


@app.route("/api/v1/<station>/<year>")
def year_data(station, year):
    if int(station) <= 100000:
        station = str(station).zfill(6)
        df = pd.read_csv(f"data/TG_STAID{station}.txt", skiprows=20)
        result = df.to_dict(orient="index")
        return result
    elif int(station) >= 100000:
        return {"message": "Error!"}
    else:
        return {"message": "Main andar se toot chuka hoon"}


if __name__ == "__main__":
    app.run(debug=True)

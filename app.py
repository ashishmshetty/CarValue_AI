from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
@app.template_filter('inr')
def inr_format(value):
    number = str(int(round(value)))

    if len(number) <= 3:
        return number

    last_three = number[-3:]
    remaining = number[:-3]

    groups = []

    while remaining:
        groups.insert(0, remaining[-2:])
        remaining = remaining[:-2]

    return ",".join(groups + [last_three])

# Load trained machine learning model
model = joblib.load("models/car_price_model.pkl")


@app.route("/")
def home():
    return render_template("index.html", prediction=None, error=None)


@app.route("/predict", methods=["POST"])
def predict():

    try:
        car_data = {
            "car_name": request.form["car_name"],
            "brand": request.form["brand"],
            "model": request.form["model"],
            "seats": int(request.form["seats"]),
            "vehicle_age": int(request.form["vehicle_age"]),
            "km_driven": int(request.form["km_driven"]),
            "seller_type": request.form["seller_type"],
            "fuel_type": request.form["fuel_type"],
            "transmission_type": request.form["transmission_type"],
            "mileage": float(request.form["mileage"]),
            "engine": int(request.form["engine"]),
            "max_power": float(request.form["max_power"]),
        }

        input_data = pd.DataFrame([car_data])

        predicted_price = model.predict(input_data)[0]

        return render_template(
            "index.html",
            prediction=round(predicted_price, 2)
        )

    except (ValueError, KeyError) as error:
        return render_template(
            "index.html",
            error="Please enter valid values for all car details."
        )


if __name__ == "__main__":
    app.run()
from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime

app = Flask(__name__)

# Home page with form and meal history
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        meal = request.form["meal"]
        calories = int(request.form["calories"])
        protein = float(request.form["protein"])
        carbs = float(request.form["carbs"])
        fats = float(request.form["fats"])
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("data.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, meal, calories, protein, carbs, fats])
        return redirect("/")

    meals = []
    try:
        with open("data.csv", mode="r") as file:
            reader = csv.reader(file)
            meals = list(reader)
    except FileNotFoundError:
        pass

    return render_template("index.html", meals=meals)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

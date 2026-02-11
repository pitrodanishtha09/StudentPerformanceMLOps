from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import logging

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initialize Flask app
application = Flask(__name__)
app = application

# Basic logging (production-friendly)
logging.basicConfig(level=logging.INFO)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html")

    try:
        # Collect and validate inputs
        reading_score = float(request.form.get("reading_score"))
        writing_score = float(request.form.get("writing_score"))

        if not (0 <= reading_score <= 100 and 0 <= writing_score <= 100):
            return render_template("home.html", results="Scores must be between 0 and 100")

        data = CustomData(
            gender=request.form.get("gender"),
            race_ethnicity=request.form.get("race_ethnicity"),
            parental_level_of_education=request.form.get("parental_level_of_education"),
            lunch=request.form.get("lunch"),
            test_preparation_course=request.form.get("test_preparation_course"),
            reading_score=reading_score,
            writing_score=writing_score,
        )

        pred_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # Round prediction to 2 decimal places
        final_result = round(results[0], 2)

        return render_template(
            "home.html",
            results=f"Predicted Maths Score: {final_result}"
        )

    except Exception as e:
        logging.error(f"Prediction error: {str(e)}")
        return render_template("home.html", results="Something went wrong. Please try again.")


if __name__ == "__main__":
    # Debug should be False in production
    app.run(host="0.0.0.0", port=5000, debug=False)

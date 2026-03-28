from flask import Flask, request, render_template
import logging
import traceback

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initialize Flask app
application = Flask(__name__)
app = application

# Logging setup
logging.basicConfig(level=logging.INFO)


# Home route
@app.route("/")
def home():
    return render_template("home.html")


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect inputs
        reading_score = float(request.form.get("reading_score"))
        writing_score = float(request.form.get("writing_score"))

        # Validate inputs
        if not (0 <= reading_score <= 100 and 0 <= writing_score <= 100):
            return render_template(
                "home.html",
                results="Scores must be between 0 and 100"
            )

        # Create data object
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

        # Prediction
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        final_result = round(results[0], 2)

        logging.info(f"Prediction successful: {final_result}")

        return render_template(
            "home.html",
            results=f"Predicted Maths Score: {final_result}"
        )

    except Exception as e:
        # Log full error (Render logs)
        logging.error("===== ERROR START =====")
        logging.error(str(e))
        logging.error(traceback.format_exc())
        logging.error("===== ERROR END =====")

        # Show actual error on UI (temporary for debugging)
        return render_template(
            "home.html",
            results=f"Error: {str(e)}"
        )


# Health check route
@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

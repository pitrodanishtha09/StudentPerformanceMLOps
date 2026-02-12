🎓 Student Exam Performance Predictor
🚀 Production-Deployed Machine Learning System

An end-to-end Machine Learning application that predicts a student’s Mathematics score using demographic and academic inputs — fully deployed on AWS with automated CI/CD.

This project demonstrates the complete ML lifecycle:

Data → Model Training → Evaluation → Serialization → Web App → Cloud Deployment → CI/CD Automation

🔗 Live Demo

👉 Try it here:
[Live Application ](http://studentperformance-env.eba-bcbjf3bp.eu-north-1.elasticbeanstalk.com/)

✨ Why This Project Stands Out

This is not just a Jupyter notebook model.

It is a fully deployed, production-style ML system that includes:

✔ Model training with hyperparameter tuning

✔ Evaluation on unseen test data

✔ Model serialization

✔ Dynamic prediction pipeline

✔ Modern responsive UI

✔ AWS Elastic Beanstalk deployment

✔ CI/CD automation with CodePipeline

✔ Nginx + Gunicorn production stack

It reflects real-world engineering beyond academic implementation.

🧠 Machine Learning Overview
📊 Problem Type

Regression — Predicting Maths Score

📥 Input Features

Gender

Race / Ethnicity

Parental Education Level

Lunch Type

Test Preparation Course

Reading Score

Writing Score

🎯 Target Variable

Maths Score (0–100)

⚙️ Model

Scikit-learn Regression Model

Hyperparameter tuning via Grid Search

Serialized using pickle / dill

Loaded dynamically in Flask prediction pipeline

📈 Model Performance (Test Data)
Metric	Score

R² Score	0.8804

MAE	4.21

RMSE	5.39

🔍 Interpretation

Model explains 88% of variance in student Maths scores.

Average prediction error ≈ 4 marks.

Most predictions fall within ±5–6 marks.

This indicates strong generalization on unseen data.

🏗️ System Architecture

🔁 Application Flow

User → Flask Web App → Prediction Pipeline → Serialized Model → Response

☁️ Deployment Flow

GitHub
   ↓
AWS CodePipeline (CI/CD)
   ↓
Elastic Beanstalk
   ↓
EC2 + Nginx + Gunicorn

⚙️ Tech Stack

🧩 Backend

Python

Flask

Scikit-learn

Pandas

NumPy

🎨 Frontend

HTML5

Bootstrap 5

Custom CSS Animations

Responsive Design

☁️ Cloud & DevOps

AWS Elastic Beanstalk

AWS CodePipeline

AWS IAM

Nginx (Reverse Proxy)

Gunicorn (WSGI Server)

🔄 CI/CD Automation

Deployment pipeline:

Push code to GitHub

CodePipeline detects changes

Builds deployment artifact

Updates Elastic Beanstalk environment

Application redeploys automatically

✔ No manual server intervention
✔ Repeatable deployment
✔ Production-style workflow

📂 Project Structure

MLPROJECT/
│
├── application.py          # Flask entry point
├── requirements.txt        # Dependencies
├── Procfile                # Gunicorn configuration
├── src/
│   ├── components/         # Data ingestion, transformation, training
│   ├── pipeline/           # Prediction pipeline
│   ├── utils.py
│   └── ...
├── templates/              # Frontend
│   └── home.html
├── artifacts/
│   └── model.pkl           # Trained model
└── README.md

🧪 Run Locally

git clone <repo-url>
cd MLPROJECT

python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt
python application.py


Open in browser:

http://127.0.0.1:5000/

🔐 Production Highlights

Gunicorn-based production server

Nginx reverse proxy

Modular ML pipeline

Structured logging

Test-based evaluation

CI/CD enabled deployment

Public cloud hosting

🚀 Future Enhancements

REST API endpoint (/api/predict)

Feature importance visualization

Docker containerization

Model versioning

Monitoring dashboard

Authentication layer

👩‍💻 Author

Nishtha Pitroda
Machine Learning & AI Enthusiast
Focused on building production-ready ML systems.


🎓 Student Exam Performance Predictor
Production-Deployed ML Web Application

An end-to-end machine learning system that predicts a student’s Maths score using academic and demographic inputs.

Deployed on AWS Elastic Beanstalk with automated CI/CD via AWS CodePipeline.

🔗 Live Demo

👉 [Try the Application](http://studentperformance-env.eba-bcbjf3bp.eu-north-1.elasticbeanstalk.com/)

🧠 Model Overview

Problem Type: Regression
Target: Maths Score (0–100)

Performance (Test Data)

R²: 0.8804

MAE: 4.21

RMSE: 5.39

Model explains 88% variance with ~4 mark average error.

⚙️ Tech Stack

Backend: Python, Flask, Scikit-learn
Frontend: HTML, Bootstrap
Deployment: AWS Elastic Beanstalk
CI/CD: AWS CodePipeline
Server Stack: Nginx + Gunicorn

🏗 Architecture
User → Flask App → Prediction Pipeline → Model (.pkl)

GitHub → CodePipeline → Elastic Beanstalk → EC2

🚀 Run Locally
git clone <repo-url>
cd MLPROJECT
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python application.py


Open:
http://127.0.0.1:5000/

👩‍💻 Author

Nishtha Pitroda
Machine Learning & AI Enthusiast
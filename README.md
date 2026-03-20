# 🎓 Student Exam Performance Predictor
## 🚀 Production-Deployed ML Web Application

An end-to-end machine learning system that predicts a student’s **Maths score** using academic and demographic inputs.

Deployed on **Render**

---

## 🔗 Live Demo

👉 https://studentperformancemlops.onrender.com
Use the form to enter student details and predict the maths score using the trained ML model.

⚠️ Note: The app is hosted on Render (free tier), so it may take 30–60 seconds to load on first open due to server cold start.

---

## 🧠 Model Overview

**Problem Type:** Regression  
**Target:** Maths Score (0–100)

### 📊 Performance (Test Data)

- **R² Score:** 0.8804  
- **MAE:** 4.21  
- **RMSE:** 5.39  

The model explains **88% of variance** with ~4 mark average prediction error.

---

## ⚙️ Tech Stack

- **Backend:** Python, Flask, Scikit-learn  
- **Frontend:** HTML, Bootstrap  
- **Deployment:** AWS Elastic Beanstalk  
- **CI/CD:** AWS CodePipeline  
- **Server Stack:** Nginx + Gunicorn  

---

## 🏗 Architecture

### Application Flow
User → Flask App → Prediction Pipeline → Model (.pkl)

### Deployment Flow
GitHub → CodePipeline → Elastic Beanstalk → EC2

## 🚀 Run Locally

```bash
git clone https://github.com/pitrodanishtha09/StudentPerformanceMLOps.git
cd student-performance-mlops

conda create -p ./venv python=3.9
conda activate ./venv

pip install -r requirements.txt
python application.py

```

Open in browser:  
http://127.0.0.1:5000/

---

## 👩‍💻 Author

**Nishtha Pitroda**  
Machine Learning & AI Enthusiast


# Rock-vs-Mine
🚢 Sonar Rock vs Mine Prediction
This is a Flask-based web application that predicts whether a given set of sonar readings correspond to a Rock or Mine using a Logistic Regression model.

📌 Overview
Uses the Sonar dataset from the UCI Machine Learning Repository.
Trained with Logistic Regression for classification.
Provides a web interface to enter sonar readings and get predictions.
Built with Flask, Joblib (for model saving/loading), and Scikit-learn.
📂 Project Structure
🚀 How to Run the Project
1️⃣ Install Dependencies
Make sure you have Python (3.8 or later) installed. Then, install the required libraries: pip install -r requirements.txt 2️⃣ Run the Flask App python app.py After running, open http://127.0.0.1:5000/ in your browser. 🛠 Training the Model (Optional) If you want to retrain the model, modify app.py and run: python app.py 📌 Dataset Information Source: UCI Sonar Dataset Contains 208 instances (60 features each). Labeled as Rock (R) or Mine (M). ⭐ If you like this project, give it a star on GitHub! ⭐

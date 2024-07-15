# Multiple Disease Prediction System

This project aims to provide a machine learning-based system for predicting diabetes and heart disease. Using Streamlit, this web application offers an easy-to-use interface for users to input relevant health data and receive predictions on their health status.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [License](#license)
- [Contributors](#contributors)

## Project Overview
This application uses machine learning models to predict the likelihood of diabetes and heart disease based on user-provided health metrics. The system is built using Python and Streamlit for the front end, making it accessible and user-friendly.

## Features
- **Home Page**: Introduction to the application.
- **Diabetes Prediction**: Predicts the likelihood of diabetes based on user inputs.
- **Heart Disease Prediction**: Predicts the likelihood of heart disease based on user inputs.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/aadiaditya/multiple-disease-prediction.git
    cd multiple-disease-prediction
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure you have the saved models (`diabetes_model.sav` and `heart_disease_model.sav`) in the same directory.

## Usage
Run the Streamlit application:
```bash
streamlit run app.py
```

Navigate to the web application:
Open your web browser and go to [http://localhost:8501](http://localhost:8501)

Use the sidebar to navigate between the Home Page, Diabetes Prediction, and Heart Disease Prediction sections.

## Models
- **Diabetes Model**: Predicts the likelihood of diabetes based on features such as pregnancies, glucose levels, blood pressure, skin thickness, insulin levels, BMI, diabetes pedigree function, and age.
- **Heart Disease Model**: Predicts the likelihood of heart disease based on features such as age, sex, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, resting electrocardiographic results, maximum heart rate achieved, exercise-induced angina, ST depression induced by exercise, slope of the peak exercise ST segment, major vessels colored by fluoroscopy, and thalassemia.

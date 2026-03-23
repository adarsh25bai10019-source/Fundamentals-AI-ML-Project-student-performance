# Fundamentals-AI-ML-Project-student-performance

## 📌 Overview : 

This project is a Machine Learning application that predicts a student's final score based on:

* Study Hours
* Attendance (%)
* Previous Marks
  
It uses Linear Regression to model the relationship between these factors and academic performance.

<br>

## 🎯 Objective :

The objective of this project is to:

* Predict student performance in advance
* Help students identify areas of improvement
* Demonstrate the practical use of AI/ML in education

<br>

## 🧠 Machine Learning Model : 
* Algorithm Used: Linear Regression
* Type: Supervised Learning
* Evaluation Metric: R² Score (Accuracy)
<br>

## 📊 Dataset

The dataset is stored in a CSV file:
<br>
customstudentdataset.csv
<br>

To view the CSV file click on the link 👉 [Click here](https://github.com/adarsh25bai10019-source/Fundamentals-AI-ML-Project-student-performance/blob/main/customstudentdataset.csv)

### Features:

| Column Name     | Description                          |
|-----------------|--------------------------------------|
| Study_Hours     | Hours studied per day                |
| Attendance      | Attendance percentage (%)            |
| Previous_Marks  | Previous exam marks                  |
| Final_Score     | Target variable (predicted output)   |

__Note__ : This CSV file has been manually made by me for practical purposes and have simple values.  


<br>

## 🛠️ Technologies Used :
* Python
* Pandas
* Scikit-learn
* Matplotlib

<br>

## ⚙️ Installation & Setup

1. Install the student-performance python file : 
[Download](https://github.com/adarsh25bai10019-source/Fundamentals-AI-ML-Project-student-performance/blob/main/student-performance.py)
2. Install Required Libraries
* `pip install pandas`
* `pip install scikit-learn`
* `pip install matplotlib`
<br>

## ▶️ How to Run the Project

Run the Python script:

student-performance.py
<br>
<br>

## 📈 How It Works
1. The dataset is loaded using Pandas
2. Features (Study_Hours, Attendance, Previous_Marks) are selected
3. Data is split into training and testing sets
4. A Linear Regression model is trained
5. Predictions are made on test data
6. Model accuracy is calculated using R² score
7. A graph is plotted to visualize the relationship

<br>

## 🧪 Example Output
Predictions: [57.91, 79.25] <br>
Actual: [58, 78]

Predicted Final Score: 73.81 <br>
Model Accuracy (R2 Score): 0.97

<br>

## 📈 Visualization

The project generates a scatter plot showing:

X-axis → Study Hours <br>
Y-axis → Final Score <br>

This helps in understanding how study time affects performance.

from sklearn.metrics import r2_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("customstudentdataset.csv")

# Step 2 : 

X = df[['Study_Hours', 'Attendance', 'Previous_Marks']]
y = df['Final_Score']

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

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Step 4: Train Model

model = LinearRegression()
model.fit(X_train, y_train)


# Step 5: Predictions

predictions = model.predict(X_test)
print("Predictions:", predictions)
print("Actual:", list(y_test))

# Step 6: Test with Custom Input

custom_input = [[6, 80, 70]]
predicted_score = model.predict(custom_input)
print("\nPredicted Final Score:", predicted_score[0])

# Step 7: Visualization

plt.scatter(df['Study_Hours'], df['Final_Score'])
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")
plt.show()


# Step 8 : Accuracy check

accuracy = r2_score(y_test, predictions)
print("Model Accuracy (R2 Score):", accuracy)


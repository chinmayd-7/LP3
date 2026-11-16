
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# 1. Load Dataset
df = pd.read_csv("uber.csv")

print("First 5 Records:")
print(df.head())

# 2. Data Preprocessing
df = df.drop_duplicates()
df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna(subset=["fare_amount"])

# Remove invalid values
df = df[df["fare_amount"] > 0]
df = df[df["passenger_count"].between(1, 6)]

print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values
df = df.fillna(df.median(numeric_only=True))

# 3. Identify Outliers using IQR
Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)
IQR = Q3 - Q1

df = df[
    (df["fare_amount"] >= Q1 - 1.5 * IQR) &
    (df["fare_amount"] <= Q3 + 1.5 * IQR)
]

print("\nDataset after removing outliers:", df.shape)

# Display outliers using boxplot
sns.boxplot(x=df["fare_amount"])
plt.title("Fare Outlier Detection")
plt.show()

# 4. Correlation Analysis
plt.figure(figsize=(8, 5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 5. Select Features and Target
X = df[[
    "pickup_longitude",
    "pickup_latitude",
    "dropoff_longitude",
    "dropoff_latitude",
    "passenger_count"
]]

y = df["fare_amount"]

# 6. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7. Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

# 8. Random Forest Regression
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

# 9. Model Evaluation
print("\nMODEL EVALUATION")

print("\nLinear Regression:")
print("R2 Score:", round(r2_score(y_test, lr_pred), 3))
print("RMSE:", round(np.sqrt(mean_squared_error(y_test, lr_pred)), 3))
print("MAE:", round(mean_absolute_error(y_test, lr_pred), 3))

print("\nRandom Forest:")
print("R2 Score:", round(r2_score(y_test, rf_pred), 3))
print("RMSE:", round(np.sqrt(mean_squared_error(y_test, rf_pred)), 3))
print("MAE:", round(mean_absolute_error(y_test, rf_pred), 3))

# 10. Predict Fare for a New Ride
new_ride = pd.DataFrame({
    "pickup_longitude": [-73.99],
    "pickup_latitude": [40.75],
    "dropoff_longitude": [-73.98],
    "dropoff_latitude": [40.76],
    "passenger_count": [2]
})

print("\nPredicted Uber Fare:")
print("Linear Regression:", round(lr.predict(new_ride)[0], 2))
print("Random Forest:", round(rf.predict(new_ride)[0], 2))

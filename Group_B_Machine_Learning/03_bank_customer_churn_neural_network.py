
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Dataset
df = pd.read_csv("bank.csv")

# 2. Preprocessing
df = df.dropna()

# Convert categorical columns into numbers
df = pd.get_dummies(df, drop_first=True)

# Separate features and target
target = "Exited" if "Exited" in df.columns else "churn"

X = df.drop(target, axis=1)
y = df[target]

# 3. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Feature Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. Create Neural Network
model = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    max_iter=500,
    random_state=42
)

# 6. Train Model
model.fit(X_train, y_train)

# 7. Predict
y_pred = model.predict(X_test)

# 8. Evaluate Model
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 9. Predict New Customer
new_customer = X_test[0].reshape(1, -1)

result = model.predict(new_customer)

if result[0] == 1:
    print("Customer will leave the bank (CHURN)")
else:
    print("Customer will stay (NOT CHURN)")

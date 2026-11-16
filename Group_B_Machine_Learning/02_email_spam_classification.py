
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Dataset
try:
    df = pd.read_csv("emails.csv")
except FileNotFoundError:
    df = pd.DataFrame({
        "text": [
            "Win a free prize now",
            "Meeting scheduled for tomorrow",
            "Claim your cash reward",
            "Please submit your assignment",
            "You won a lottery",
            "Let's discuss the project",
            "Free gift waiting for you",
            "The class starts at ten"
        ] * 20,
        "label": [
            "spam", "ham", "spam", "ham",
            "spam", "ham", "spam", "ham"
        ] * 20
    })

print("Dataset:")
print(df.head())

# 2. Preprocessing
df = df.dropna()
df["label"] = df["label"].str.lower()

X = df["text"].astype(str)
y = df["label"]

# 3. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 4. KNN Model
knn = make_pipeline(
    TfidfVectorizer(),
    KNeighborsClassifier(n_neighbors=3)
)

knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)

# 5. SVM Model
svm = make_pipeline(
    TfidfVectorizer(),
    LinearSVC()
)

svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)

# 6. Evaluate Models
print("\nKNN Accuracy:", accuracy_score(y_test, knn_pred))
print("\nKNN Report:")
print(classification_report(y_test, knn_pred, zero_division=0))

print("\nSVM Accuracy:", accuracy_score(y_test, svm_pred))
print("\nSVM Report:")
print(classification_report(y_test, svm_pred, zero_division=0))

# 7. Test a New Email
new_email = ["Congratulations! You won a free gift. Claim now!"]

print("\nNew Email Classification:")
print("KNN:", knn.predict(new_email)[0])
print("SVM:", svm.predict(new_email)[0])

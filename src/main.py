from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# Locate data relative to project root
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "student_sleep_patterns.csv"

# Load data
df = pd.read_csv(DATA_PATH)

# Optional: drop identifier columns that shouldn't be used as features
if "Student_ID" in df.columns:
    df = df.drop(columns=["Student_ID"])

target = "Sleep_Quality"
X = df.drop(columns=[target])
y = df[target]

# Separate feature types
categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
numeric_cols = X.select_dtypes(exclude=["object"]).columns.tolist()

# Preprocessing: scale numeric features, one-hot encode categoricals
preprocess = ColumnTransformer([
    ("num", StandardScaler(), numeric_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
])

# Train/test split (stratified to preserve class proportions)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ---- Model 1: Random Forest ----
rf = Pipeline(steps=[("prep", preprocess),
                     ("model", RandomForestClassifier(random_state=42))])
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print("\n=== Random Forest ===")
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

# Save confusion matrix plot
plt.figure()
ConfusionMatrixDisplay.from_predictions(y_test, y_pred_rf)
plt.title("Random Forest - Confusion Matrix")
plt.tight_layout()
(BASE_DIR / "reports").mkdir(exist_ok=True)
plt.savefig(BASE_DIR / "reports" / "confusion_matrix_rf.png", dpi=150)
plt.close()

# ---- Model 2: Logistic Regression ----
lr = Pipeline(steps=[("prep", preprocess),
                    ("model", LogisticRegression(max_iter=1000, multi_class="auto"))])
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

print("\n=== Logistic Regression ===")
print("Accuracy:", accuracy_score(y_test, y_pred_lr))
print(classification_report(y_test, y_pred_lr))

plt.figure()
ConfusionMatrixDisplay.from_predictions(y_test, y_pred_lr)
plt.title("Logistic Regression - Confusion Matrix")
plt.tight_layout()
plt.savefig(BASE_DIR / "reports" / "confusion_matrix_lr.png", dpi=150)
plt.close()

print("\nReports saved to:", BASE_DIR / "reports")

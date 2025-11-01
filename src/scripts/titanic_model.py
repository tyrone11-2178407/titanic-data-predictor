import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("Step 1: Loading data...")

train_df = pd.read_csv("src/data/train.csv")
test_df = pd.read_csv("src/data/test.csv")
gender_baseline = pd.read_csv("src/data/gender_submission.csv")

print(f"train.csv shape: {train_df.shape}")
print(f"test.csv shape: {test_df.shape}")
print(f"gender_submission.csv shape: {gender_baseline.shape}")

print("\nStep 2: Cleaning and feature engineering...")

# Fill missing values
train_df["Age"].fillna(train_df["Age"].median(), inplace=True)
test_df["Age"].fillna(test_df["Age"].median(), inplace=True)
train_df["Embarked"].fillna(train_df["Embarked"].mode()[0], inplace=True)
test_df["Fare"].fillna(test_df["Fare"].median(), inplace=True)

# Encode categorical features
for df in [train_df, test_df]:
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

# Feature selection
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
X = train_df[features]
y = train_df["Survived"]

print("Features used:", features)
print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")

print("\nStep 3: Train/validation split and model training...")

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate training and validation accuracy
y_pred_train = model.predict(X_train)
train_acc = accuracy_score(y_train, y_pred_train)
print(f"Training accuracy: {train_acc:.3f}")

y_pred_val = model.predict(X_val)
val_acc = accuracy_score(y_val, y_pred_val)
print(f"Validation accuracy: {val_acc:.3f}")

print("\nStep 4: Predict on test.csv...")

test_X = test_df[features]
test_pred = model.predict(test_X)

# Save predictions
my_test_pred = pd.DataFrame({
    "PassengerId": test_df["PassengerId"],
    "Survived": test_pred
})

print("Sample predictions:")
print(my_test_pred.head())

print("\nStep 5: Compare to gender_submission.csv (assignment baseline)...")

merged = pd.merge(
    my_test_pred,
    gender_baseline,
    on="PassengerId",
    suffixes=("_model", "_gender")
)

match_acc = (merged["Survived_model"] == merged["Survived_gender"]).mean()
print(f"Match rate vs gender_submission.csv: {match_acc:.3f}")

print("\nNote:")
print(" - Training accuracy shows model performance on labeled data.")
print(" - Validation accuracy measures generalization on unseen data.")
print(" - The gender_submission.csv comparison is used as a test reference for this assignment.")
print("\nStep 6: Saving predictions...")

my_test_pred.to_csv("src/data/titanic_predictions.csv", index=False)
print("Saved: src/data/titanic_predictions.csv")

print("\nScript finished successfully.")

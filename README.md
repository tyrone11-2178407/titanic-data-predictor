<<<<<<< Updated upstream
# titanic-data-predictor
=======
# 🚢 Titanic Data Predictor  
### Northwestern University – MLDS 413: Introduction to Data Engineering  
**Homework 3**

---

## 📘 Overview

This project builds **two reproducible Docker environments** — one in **Python** and one in **R** — to analyze passenger data from the Titanic disaster (April 15, 1912) and predict survival outcomes using logistic regression.

Each Dockerfile runs independently and produces printed outputs directly in the terminal.  
The grader can reproduce results by simply cloning this repository, downloading the dataset, and running two commands per environment.

---

## 📂 Repository Structure

```plaintext
titanic-data-predictor/
├── src/
│   ├── data/                     # contains local CSV files (not committed)
│   │   ├── train.csv
│   │   ├── test.csv
│   │   └── gender_submission.csv
│   ├── scripts/
│   │   └── titanic_model.py
│   └── r/
│       ├── Dockerfile
│       ├── install_package.R
│       └── titanic_model.R
├── requirements.txt
├── Dockerfile                    # Python environment
├── .gitignore
└── README.md

📊 Dataset

The dataset is provided by Kaggle’s Titanic: Machine Learning from Disaster
 competition.

Required files

After downloading from Kaggle, you’ll have:

train.csv

test.csv

gender_submission.csv

Before building your Docker images, make sure these files are placed correctly:

1️⃣ Create the data folder (if it doesn’t exist):

mkdir -p src/data


2️⃣ Move the CSV files into that folder:

src/data/train.csv
src/data/test.csv
src/data/gender_submission.csv


🐍 Python Container
🧩 Purpose

Builds a Python environment that reads Titanic data, cleans missing values, trains a logistic regression model, and evaluates accuracy on both train and test datasets.

🪜 Steps to Run

1️⃣ Build the Docker image

docker build -t titanic-py .


2️⃣ Run the container

docker run titanic-py

🧾 Expected Output
Loading data...
Training logistic regression...
Training accuracy: 0.799
Testing accuracy: 0.768
Predictions saved to src/data/titanic_predictions.csv

🧠 Technical Details

Base image: python:3.12-slim

Dependencies: from requirements.txt

pandas
numpy
scikit-learn
joblib


Model: sklearn.linear_model.LogisticRegression

Output: src/data/titanic_predictions.csv

📈 R Container
🧩 Purpose

Builds an R environment that loads the Titanic dataset, performs data cleaning, trains a logistic regression model, and prints performance metrics.

🪜 Steps to Run

1️⃣ Build the Docker image

docker build -t titanic-r -f src/r/Dockerfile .


2️⃣ Run the container

docker run titanic-r

🧾 Expected Output
Step 1: Loading data...
train.csv shape: 891 rows, 12 columns
test.csv shape: 418 rows, 11 columns
Step 2: Cleaning data...
Step 3: Training logistic regression...
Training accuracy: 0.799
Step 4: Predicting on test.csv...
Match rate vs gender_submission.csv: 0.938
Step 5: Saving predictions...
Saved: src/data/titanic_predictions_r.csv
Script finished successfully.

🧠 Technical Details

Base image: rocker/tidyverse:4.3.2

Includes the full tidyverse (dplyr, ggplot2, readr, tidyr, etc.) pre-installed
for fast, reproducible builds.

Additional package installed:

install.packages("caret", repos="https://packagemanager.posit.co/cran/__linux__/jammy/latest")


Model: glm() logistic regression

Output: src/data/titanic_predictions_r.csv


🧪 Reproducibility Notes

Both Dockerfiles are fully automated.

No manual package installation once the dataset is present.

Outputs print directly in the terminal.

The R image uses rocker/tidyverse for guaranteed dependency stability.



✍️ Author

Tyrone Li
Northwestern University
MLDS 413 – Introduction to Data Engineering
Fall 2025
>>>>>>> Stashed changes

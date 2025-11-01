🚢 Titanic Data Predictor
Northwestern University – MLDS 413: Introduction to Data Engineering

Homework 3

📘 Overview

This project builds two reproducible Docker environments — one in Python and one in R — to analyze passenger data from the Titanic disaster (April 15, 1912) and predict survival outcomes using logistic regression.

Each Dockerfile runs independently and produces printed outputs directly in the terminal.
The grader can reproduce results by simply cloning this repository, downloading the dataset, and running two commands per environment.

📂 Repository Structure
titanic-data-predictor/
├── src/
│   ├── data/
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
├── Dockerfile                # Python environment
├── .gitignore
└── README.md

📊 Dataset

The dataset is provided by Kaggle’s Titanic: Machine Learning from Disaster
 competition.

Required files

After downloading from Kaggle, place these CSVs into your local directory:

src/data/train.csv
src/data/test.csv
src/data/gender_submission.csv


⚠️ Do not include these files in your public repository per assignment requirements.
Your grader should download them directly from Kaggle.

🧰 Prerequisites

Docker Desktop
 installed and running

Internet connection for installing dependencies on first build

Kaggle Titanic CSV files placed in src/data/

🐍 Python Container
🧩 Purpose

Builds a Python environment that reads Titanic data, cleans missing values, trains a logistic regression model, and evaluates accuracy on both train and test datasets.

🪜 Steps to Run

1️⃣ Build the Docker image

docker build -t titanic-py .


2️⃣ Run the container

docker run titanic-py

🧾 Expected Console Output
Loading data...
Training logistic regression...
Training accuracy: 0.799
Testing accuracy: 0.768
Predictions saved to src/data/titanic_predictions.csv

🧠 Technical Details

Base image: python:3.12-slim

Dependencies: Installed via requirements.txt

pandas
numpy
scikit-learn
joblib


Model: Logistic Regression (sklearn.linear_model.LogisticRegression)

Output file: src/data/titanic_predictions.csv

📈 R Container
🧩 Purpose

Builds an R environment that loads the same Titanic dataset, performs data cleaning, trains a logistic regression model, and prints performance metrics in the console.

🪜 Steps to Run

1️⃣ Build the Docker image

docker build -t titanic-r -f src/r/Dockerfile .


2️⃣ Run the container

docker run titanic-r

🧾 Expected Console Output
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

This image includes the full tidyverse (dplyr, ggplot2, readr, tidyr, etc.) preinstalled
ensuring fast, reproducible builds with zero dependency errors.

Additional package installed:

install.packages("caret", repos = "https://packagemanager.posit.co/cran/__linux__/jammy/latest")


Model: glm() logistic regression

Output file: src/data/titanic_predictions_r.csv

🧪 Reproducibility Notes

Both Dockerfiles are fully automated.

No data or manual package installation is required once the dataset is placed in src/data/.

All model outputs print directly in the terminal for easy grading.

The R environment uses rocker/tidyverse to guarantee compatibility on all systems.

🧾 Example Grader Workflow

Once cloned and dataset is added, the grader can run:

# Python container
docker build -t titanic-py .
docker run titanic-py

# R container
docker build -t titanic-r -f src/r/Dockerfile .
docker run titanic-r


✅ Both containers will execute end-to-end and print outputs.

📦 Expected Deliverables
File	Description
Dockerfile	Python environment with logistic regression
src/scripts/titanic_model.py	Python ML script
src/r/Dockerfile	R environment using rocker/tidyverse
src/r/titanic_model.R	R ML script
README.md	Detailed build and run instructions
✍️ Author

Tyrone Li
Northwestern University
MLDS 413: Introduction to Data Engineering
Fall 2025
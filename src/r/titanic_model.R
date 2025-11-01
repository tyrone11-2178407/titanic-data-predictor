library(dplyr)
library(ggplot2)
library(readr)
library(tidyr)
library(caret)


cat("Step 1: Loading data...\n")

train <- read.csv("src/data/train.csv")
test  <- read.csv("src/data/test.csv")
gender <- read.csv("src/data/gender_submission.csv")

cat(paste("train.csv shape:", dim(train)[1], "rows,", dim(train)[2], "columns\n"))
cat(paste("test.csv shape:", dim(test)[1], "rows,", dim(test)[2], "columns\n"))

cat("\nStep 2: Cleaning data...\n")

# Fill missing values
train$Age[is.na(train$Age)] <- median(train$Age, na.rm = TRUE)
test$Age[is.na(test$Age)] <- median(test$Age, na.rm = TRUE)
train$Embarked[train$Embarked == ""] <- "S"
test$Fare[is.na(test$Fare)] <- median(test$Fare, na.rm = TRUE)

# Encode categorical variables
train$Sex <- ifelse(train$Sex == "male", 0, 1)
test$Sex  <- ifelse(test$Sex == "male", 0, 1)
train$Embarked <- recode(train$Embarked, "S" = 0, "C" = 1, "Q" = 2)
test$Embarked  <- recode(test$Embarked, "S" = 0, "C" = 1, "Q" = 2)

# Select features
features <- c("Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked")

cat("\nStep 3: Training logistic regression...\n")

# Build logistic regression model
formula <- as.formula(paste("Survived ~", paste(features, collapse = " + ")))
model <- glm(formula, data = train, family = binomial())

# Predict on training set
train$pred_train <- ifelse(predict(model, train, type = "response") > 0.5, 1, 0)
train_acc <- mean(train$pred_train == train$Survived)
cat(paste("Training accuracy:", round(train_acc, 3), "\n"))

cat("\nStep 4: Predicting on test.csv...\n")

test$Survived <- ifelse(predict(model, test, type = "response") > 0.5, 1, 0)

# Compare to gender_submission.csv
merged <- merge(test[, c("PassengerId", "Survived")], gender, by = "PassengerId")
match_acc <- mean(merged$Survived.x == merged$Survived.y)
cat(paste("Match rate vs gender_submission.csv:", round(match_acc, 3), "\n"))

cat("\nStep 5: Saving predictions...\n")
write.csv(test[, c("PassengerId", "Survived")], "src/data/titanic_predictions_r.csv", row.names = FALSE)
cat("Saved: src/data/titanic_predictions_r.csv\n")

cat("\nScript finished successfully.\n")

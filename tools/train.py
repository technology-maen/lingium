import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
import joblib

# Load the training dataset
df = pd.read_excel("training_data_100.xlsx")

# Initialize label encoders for categorical data
le_goal = LabelEncoder()
le_cert = LabelEncoder()
le_mode = LabelEncoder()
le_focus = LabelEncoder()
le_server = LabelEncoder()

# Encode categorical columns
df['Goal'] = le_goal.fit_transform(df['Goal'])
df['CertSupport'] = le_cert.fit_transform(df['CertSupport'])
df['Mode'] = le_mode.fit_transform(df['Mode'])
df['Focus'] = le_focus.fit_transform(df['Focus'])
df['RecommendedServer'] = le_server.fit_transform(df['RecommendedServer'])

# Define features and target variable
X = df[['Age', 'Goal', 'CertSupport', 'Mode', 'Focus']]
y = df['RecommendedServer']

# Define hyperparameters for decision tree tuning
param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Perform grid search with cross-validation
grid_search = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X, y)

# Use the best model from grid search
model = grid_search.best_estimator_

# Save the trained model to a file
joblib.dump(model, 'decision_tree_model.pkl')

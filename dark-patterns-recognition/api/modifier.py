from joblib import load, dump
from sklearn.ensemble import RandomForestClassifier

# Load the Joblib file containing a RandomForestClassifier
category_classifier = load('category_classifier.joblib')
print(category_classifier)
# Modify the model parameters
# model.n_estimators = 100  # Update the number of estimators

# # Save the modified model back to a new Joblib file
# dump(model, 'modified_model.joblib')

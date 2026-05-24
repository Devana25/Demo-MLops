import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
file_path = 'data/train.csv'

data = pd.read_csv(file_path)

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Feature Engineering
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day
data['Weekday'] = data['Date'].dt.weekday

# Features and target
X = data[['Store', 'Year', 'Month', 'Day', 'Weekday']]
y = data['Sales']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model Training Completed")
print(f"MAE: {mae}")
print(f"R2 Score: {r2}")

# Save model
model_path = 'models/sales_model.pkl'

with open(model_path, 'wb') as file:
    pickle.dump(model, file)

print("Model saved successfully!")
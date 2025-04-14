import pandas as pd
import os
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns
import joblib  

start_time = time.time()

data_path = 'ev_charging_data'

df = pd.read_csv(os.path.join(data_path, 'ev_charging_dataset.csv'))
location_df = pd.read_csv(os.path.join(data_path, 'location_dataset.csv'))

print("EV Charging Dataset:")
print(df.head())

df.rename(columns={'Date_Time': 'timestamp'}, inplace=True)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.ffill(inplace=True)

df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.dayofweek

label_encoders = {}
categorical_col = 'Weather_Conditions'
le = LabelEncoder()
df[categorical_col] = le.fit_transform(df[categorical_col].astype(str))
label_encoders[categorical_col] = le

selected_features = [
    'Battery_Capacity_kWh',
    'State_of_Charge_%',
    'Energy_Consumption_Rate_kWh/km',
    'Distance_to_Destination_km',
    'Charging_Rate_kW',
    'Station_Capacity_EV',
    'Temperature_C',
    'hour',
    'day_of_week',
    'Weather_Conditions'
]

X = df[selected_features]
y = df['Charging_Load_kW']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

gb_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
gb_model.fit(X_train, y_train)

xgb_model = xgb.XGBRegressor(n_estimators=100, random_state=42)
xgb_model.fit(X_train, y_train)

# Evaluate models
def evaluate_model(model, X_test, y_test, name):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"{name} - MSE: {mse}, R^2: {r2}, MAE: {mae}")
    return {'Model': name, 'MSE': mse, 'R^2': r2, 'MAE': mae}

results = []
results.append(evaluate_model(rf_model, X_test, y_test, "Random Forest"))
results.append(evaluate_model(gb_model, X_test, y_test, "Gradient Boosting"))
results.append(evaluate_model(xgb_model, X_test, y_test, "XGBoost"))

comparison_df = pd.DataFrame(results)
print("\nModel Comparison:")
print(comparison_df)


sns.barplot(x='Model', y='MSE', data=comparison_df, palette='Blues')
plt.title('Model MSE Comparison')
plt.show()

joblib.dump(xgb_model, 'model.pkl')
joblib.dump(label_encoders['Weather_Conditions'], 'weather_encoder.pkl')
print("\nModel and encoder saved as model.pkl and weather_encoder.pkl")

end_time = time.time()
print(f"\nTotal Runtime: {round(end_time - start_time, 2)} seconds")

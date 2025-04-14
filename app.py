from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and encoder
model = joblib.load('model.pkl')
weather_encoder = joblib.load('weather_encoder.pkl')

# Step 1: Home page
@app.route('/')
def home():
    return render_template('home.html')  # Shows landing page with button to input form

# Step 2: Form input page
@app.route('/predict-form')
def predict_form():
    return render_template('input.html')  # Input form is here

# Step 3: Prediction logic
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs
        battery_capacity = float(request.form['Battery_Capacity_kWh'])
        soc = float(request.form['State_of_Charge_%'])
        energy_rate = float(request.form['Energy_Consumption_Rate_kWh_per_km'])
        distance = float(request.form['Distance_to_Destination_km'])
        charging_rate = float(request.form['Charging_Rate_kW'])
        station_capacity = float(request.form['Station_Capacity_EV'])
        temperature = float(request.form['Temperature_C'])
        hour = int(request.form['hour'])
        day = int(request.form['day_of_week'])
        weather = request.form['Weather_Conditions']

        # Encode weather
        weather_encoded = weather_encoder.transform([weather])[0]

        input_data = np.array([[battery_capacity, soc, energy_rate, distance,
                                charging_rate, station_capacity, temperature,
                                hour, day, weather_encoded]])

        prediction = model.predict(input_data)[0]

        # Return the prediction result page
        return render_template('output.html', prediction=prediction)

    except Exception as e:
        return render_template('output.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)

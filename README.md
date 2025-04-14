# Electric Vehicle Charging Station Demand Prediction

This project aims to predict the demand for electric vehicle (EV) charging stations based on various input parameters. The goal is to forecast the load that a charging station will experience, helping optimize resource allocation and planning for electric vehicle infrastructure.

The project uses machine learning to predict charging load based on parameters such as battery capacity, state of charge, energy consumption rate, temperature, time of day, day of the week, and weather conditions. A trained model is used for making predictions.

---

## 🚀 Project Features

- **Predictive Model**: A machine learning model predicts EV charging station load using multiple input features.
- **Web Interface**: A user-friendly Flask-based web application that takes input data and displays the predicted charging load.
- **Interactive UI**: The application allows users to enter real-world parameters and get predictions on demand.

---

## 🧠 Technologies Used

- **Flask**: A lightweight web framework for building the web app.
- **scikit-learn**: For machine learning and model training.
- **Joblib**: To save and load the trained model.
- **Bootstrap 5**: For styling and layout of the web application.
- **Python**: For data processing and model development.

---

## ⚙️ Installation

### Prerequisites
To run this project locally, ensure that you have Python 3.6 or above installed. You will also need `git` to clone the repository.

### Steps to Set Up

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Mizbain-Fathima/Electric-vehicle-charging-station-demand-prediction.git
   ```

2. **Navigate to the Project Directory**:
   cd Electric-vehicle-charging-station-demand-prediction
  
3. **Create a Virtual Environment**:
   python -m venv venv
  
4. **Activate the Virtual Environment**:
   - On **Windows**:
     venv\Scripts\activate
     
   - On **macOS/Linux**:
     source venv/bin/activate
     
5. **Install Required Dependencies**:
   pip install -r requirements.txt

6. **Run the Flask Application**:
   python app.py

7. **Access the Application**:
   Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to use the EV charging demand predictor.

---

## 🔍 How to Use

1. **Start the Application**: Once the server is running, open a web browser and navigate to `http://127.0.0.1:5000`.

2. **Input Form**: On the landing page, click the "Start Prediction" button to go to the input form. Here, you will need to provide values for the following fields:
   - **Battery Capacity (kWh)**
   - **State of Charge (%)**
   - **Energy Consumption Rate (kWh/km)**
   - **Distance to Destination (km)**
   - **Charging Rate (kW)**
   - **Station Capacity (EV)**
   - **Temperature (°C)**
   - **Hour of Day**
   - **Day of Week (0 = Monday, 6 = Sunday)**
   - **Weather Condition**

3. **View Prediction**: After filling in the form and submitting it, the application will display the predicted charging load in kilowatts (kW).

---

## 🗂️ Files Structure

- `app.py`: The main Flask application that runs the web server and handles the logic for prediction.
- `model.pkl`: The trained machine learning model for predicting the charging load.
- `weather_encoder.pkl`: The encoder for weather conditions used in the model.
- `input.html`: HTML form where users input data.
- `home.html`: Landing page with a "Start Prediction" button.
- `output.html`: Displays the prediction result after form submission.
- `templates/`: Folder containing HTML templates for rendering the pages.
- `static/`: Folder containing CSS (optional styling files).
- `.gitignore`: Git ignore file to skip tracking `venv/`, `*.pkl`, and data folders.

---

## 📊 Model Description

- The model predicts the demand for electric vehicle charging based on input features like battery capacity, energy consumption, distance, weather, and other parameters.
- It was trained using historical data from a real-world EV charging station dataset.
- The trained model is saved as a `model.pkl` file and loaded during runtime for making predictions.

---

## 📥 Sample Input

To try out the app, you can use the following sample values:

| Field                          | Sample Value |
|-------------------------------|--------------|
| Battery Capacity (kWh)        | 75           |
| State of Charge (%)           | 35           |
| Energy Consumption Rate       | 0.22         |
| Distance to Destination (km)  | 30           |
| Charging Rate (kW)            | 50           |
| Station Capacity (EV)         | 10           |
| Temperature (°C)              | 28.5         |
| Hour of Day                   | 16           |
| Day of Week (0 = Monday)      | 2            |
| Weather Condition             | Clear        |

✅ This will output a predicted charging demand value in kW.

---

## 🤝 Contributing

If you would like to contribute to this project, feel free to fork the repository and submit pull requests. Please ensure that any changes or improvements are properly tested before submitting.

---

## 🪪 License

This project is open-source and available under the [MIT License](LICENSE).
```

Let me know if you want this as a downloadable file or want to include images/screenshots or deployment instructions next!

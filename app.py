from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the models and scaler
with open(r'energyefficiency.pkl', 'rb') as file:
    data = pickle.load(file)
model_heating = data['heating_load_model']  # Heating Load Model
model_cooling = data['cooling_load_model']  # Cooling Load Model
scaler = data['scaler']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        features = request.form['features']
        prediction_type = request.form['type']
        
        # Convert input features to a list of floats
        features = list(map(float, features.split(',')))

        # Validate feature length
        if len(features) != scaler.n_features_in_:
            return render_template('index.html', prediction="Invalid input. Incorrect number of features.", type=prediction_type)

        # Scale the input features
        features_scaled = scaler.transform([features])

        # Predict using the appropriate model
        if prediction_type.lower() == 'heating':
            prediction = model_heating.predict(features_scaled)
        elif prediction_type.lower() == 'cooling':
            prediction = model_cooling.predict(features_scaled)
        else:
            return render_template('index.html', prediction="Invalid type.", type=prediction_type)

        # Render the result
        return render_template('index.html', prediction=f"{prediction[0]:.2f}", type=prediction_type)

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}", type="Unknown")


if __name__ == '__main__':
    app.run(debug=True)

from django.shortcuts import render
import joblib
import numpy as np
import os
from datetime import datetime

model_path = os.path.join(os.path.dirname(__file__), 'flight_price_model.pkl')
model = joblib.load(model_path)


airline_encoding = {
    'Jet Airways': 0, 'IndiGo': 1, 'Air India': 2, 'Multiple carriers': 3, 
    'SpiceJet': 4, 'Vistara': 5, 'GoAir': 6, 'Multiple carriers Premium economy': 7, 
    'Trujet': 8
}
destination_encoding = {
    'Cochin': 0, 'Banglore': 1, 'Delhi': 2, 'New Delhi': 3, 'Hyderabad': 4, 'Kolkata': 5
}

def home(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == "POST":
        try:
          
            journey_date = request.POST['dep_date']
            dep_time = request.POST['dep_time']
            arrival_time = request.POST['arrival_time']
            source = request.POST['source']
            destination = request.POST['destination']
            airline = request.POST['airline']
            total_stops = int(request.POST['stops'].split()[0])  # Extract number from "0 - Non-Stop"

          
            today = datetime.today().date()

           
            journey_datetime = datetime.strptime(journey_date, '%Y-%m-%d').date()

            if journey_datetime < today:
                raise ValueError("Prediction can only be made for future dates.")

            if journey_datetime.year not in [2025, 2026]:
                raise ValueError("Prediction is only available for the years 2025 and 2026.")

           
            if source == destination:
                raise ValueError("Source and Destination cannot be the same.")

    
            airline_encoded = airline_encoding.get(airline, -1)
            destination_encoded = destination_encoding.get(destination, -1)

            journey_day = journey_datetime.day
            journey_month = journey_datetime.month

            
            dep_datetime_str = journey_date + ' ' + dep_time
            arrival_datetime_str = journey_date + ' ' + arrival_time

            dep_datetime = datetime.strptime(dep_datetime_str, '%Y-%m-%d %H:%M')
            arrival_datetime = datetime.strptime(arrival_datetime_str, '%Y-%m-%d %H:%M')

           
            if arrival_datetime < dep_datetime:
                raise ValueError("Arrival time cannot be earlier than departure time.")

            duration = arrival_datetime - dep_datetime
            duration_hours = duration.seconds // 3600
            duration_mins = (duration.seconds // 60) % 60

            source_mapping = {
                'Delhi': [1, 0, 0, 0], 'Kolkata': [0, 1, 0, 0], 
                'Mumbai': [0, 0, 1, 0], 'Chennai': [0, 0, 0, 1]
            }
            source_encoded = source_mapping.get(source, [0, 0, 0, 0])

            
            if airline_encoded == -1 or destination_encoded == -1:
                raise ValueError("Invalid airline or destination selected.")

            features = [
                airline_encoded, destination_encoded, total_stops, journey_day, journey_month,
                dep_datetime.hour, dep_datetime.minute, arrival_datetime.hour, arrival_datetime.minute,
                duration_hours, duration_mins, *source_encoded
            ]

           
            features_array = np.array(features).reshape(1, -1)

            prediction = model.predict(features_array)[0]

            return render(request, 'predict.html', {'price': round(prediction, 2)})

        except Exception as e:
            return render(request, 'predict.html', {'error': f"Error in prediction: {str(e)}"})

    return render(request, 'predict.html')

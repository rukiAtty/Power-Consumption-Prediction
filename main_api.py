from fastapi import FastAPI
from pydantic import BaseModel   ## format of inputs the model using
import joblib
import json
import pandas as pd

app = FastAPI()

class ModelInput(BaseModel):
    hour: int
    weekday_input: bool
    temperature: float
    cloudiness: float
    irradiation: float
    holiday_input: bool

model_loaded = joblib.load('voting_regressor_model.pkl')

@app.post('/prediction')
def model_pred(input_parameters: ModelInput):
    # Convert input to dictionary
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    # Convert boolean values to 0 or 1
    weekday = 1 if input_dictionary['weekday_input'] else 0
    holiday = 1 if input_dictionary['holiday_input'] else 0

    # Create new column 'Working_Day'
    if weekday == 1:
        if holiday == 1:
            working_day = 0
        else:
            working_day = 1
    else:
        working_day = 0

    # Prepare the final input for the model
    data = {
    
    'Temperature': [input_parameters.temperature],
    'Cloudiness': [input_parameters.cloudiness],
    'Irradiation': [input_parameters.irradiation],
    'Hour': [input_parameters.hour],
    'Working_Day': [working_day]  # Include the Working_Day column
}

# Create a DataFrame
    df = pd.DataFrame(data)

# Pass this DataFrame to your model for prediction
    predictions = model_loaded.predict(df)
    
    # Return the prediction as a response
    return {"predicted_load": predictions[0]}

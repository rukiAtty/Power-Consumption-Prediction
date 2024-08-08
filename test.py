import json
import requests

#url="http://127.0.0.1:8000/prediction" # testing locally
url = 'http://loadpredictionapi.eastus.azurecontainer.io/prediction'

input_data_for_model = {
    
    'hour' : 5,
    'weekday_input' : True,
    'temperature' : 72,

    'cloudiness' : 1.2,
    'irradiation' : 0.5,
    'holiday_input' : False,
    
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)
print(response.text)
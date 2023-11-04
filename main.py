# Workout tracker that takes in user input and accesses nutritionix api to generate data based on input
# writes to google sheet using sheetly

import requests
from datetime import datetime
import os

GENDER = 'male'
WEIGHT_KG = 70.31
HEIGHT_CM = 177.8
AGE = 21
TODAY = datetime.now()

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']
APP_ID = os.environ['APP_ID']
APP_KEY = os.environ['APP_KEY']

exercise_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
exercise_text = input('What excerise(s) did you do?: ')

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}

exercise_params = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
}

response = requests.post(url=exercise_url, json=exercise_params, headers=headers)
result = response.json()

sheetly_url = os.environ['sheetly_url']

basic_headers = {
    'Authorization': f'Basic {os.environ["TOKEN"]}'
}

for exercise in result['exercises']:
    sheetly_params = {
        'workout': {
            'date': TODAY.strftime('%x'),
            'time': TODAY.strftime('%X'),
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheetly_post = requests.post(url=sheetly_url, json=sheetly_params, headers=basic_headers)

    print(sheetly_post.text)


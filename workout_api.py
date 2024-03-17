import requests
import json
import pandas as pd


def process_response(response):
    response_dict = json.loads(response)

    df_mon = pd.json_normalize(response_dict[0]['monday'])
    df_tues = pd.json_normalize(response_dict[0]['tuesday'])
    df_wed = pd.json_normalize(response_dict[0]['wednesday'])
    df_thurs = pd.json_normalize(response_dict[0]['thursday'])
    df_fri = pd.json_normalize(response_dict[0]['friday'])
    df_sat = pd.json_normalize(response_dict[0]['saturday'])
    df_sun = pd.json_normalize(response_dict[0]['sunday'])

    week_set = {"monday": df_mon, "tuesday": df_tues, "wednesday": df_wed, "thursday": df_thurs, "friday": df_fri,
                "saturday": df_sat, "sunday": df_sun
                }

    return week_set


def request_workout_info(level):
    url = ''
    if level == "Hybrid":
        url = "https://fitjournal-api-ca964984ffd7.herokuapp.com/getWorkoutProgram?programName=Hybrid"
    elif level == "Endurance":
        url = "https://fitjournal-api-ca964984ffd7.herokuapp.com/getWorkoutProgram?programName=Endurance"
    elif level == "Build Muscle":
        url = "https://fitjournal-api-ca964984ffd7.herokuapp.com/getWorkoutProgram?programName=Build%20Muscle"

    response = requests.request("GET", url)

    processed_response = process_response(response.text)

    return processed_response

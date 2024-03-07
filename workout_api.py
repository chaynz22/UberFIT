import requests
import json


def process_response(response):
    response_dict = json.loads(response)
    print(response_dict)

    required_data_dict = {"monday": response_dict[0]['monday'][1]['exercise'],
                          "tuesday": response_dict[0]["tuesday"][1]["exercise"],
                          "wednesday": response_dict[0]["wednesday"],
                          "thursday": response_dict[0]["thursday"][0]["exercise"],
                          "friday": response_dict[0]["friday"][0]["exercise"],
                          "saturday": response_dict[0]["saturday"],
                          "sunday": response_dict[0]["sunday"]}

    return required_data_dict


def request_workout_info(level):
    url = ''
    if level == "Hybrid":
        url = "https://fitjournal-api-ca964984ffd7.herokuapp.com/getWorkoutProgram?programName=Hybrid"
    elif level == "Cardio":
        url = "https://fitjournal-api-ca964984ffd7.herokuapp.com/getWorkoutProgram?programName=Cardio"

    response = requests.request("GET", url)

    processed_response = process_response(response.text)

    return processed_response


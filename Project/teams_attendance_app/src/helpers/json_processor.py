"""
1. Genenerates JSON from in-memory object
2. Writes in-memory object into JSON file
"""
from datetime import date, timedelta
import json

def calculate_date(start_date, end_date, arguments):
        m1, d1, y1 = [int(x) for x in start_date[0].split("/")]
        b1 = date(y1, m1, d1)
        m1_1, d1_1, y1_1 = [int(x) for x in end_date[0].split("/")]
        b1_1 = date(y1_1, m1_1, d1_1)
        m2, d2, y2 = [int(x) for x in arguments.get("start_date").split("/")]
        b2 = date(y2, m2, d2) 
        m2_1, d2_1, y2_1 = [int(x) for x in arguments.get("end_date").split("/")]
        b2_1 = date(y2_1, m2_1, d2_1)
        return (b1, b1_1, b2, b2_1)


def calculate_hours(start_date, end_date):
    print(start_date, " ", end_date)
    start_time = start_date[1].replace('AM','').replace('PM','').split(":")
    time_1 = timedelta(hours= int(start_time[0]) , minutes=int(start_time[1]), seconds=int(start_time[2]))
    end_time = end_date[1].replace('AM','').replace('PM','').split(":")
    time_2 = timedelta(hours= int(end_time[0]), minutes=int(end_time[1]), seconds=int(end_time[2]))
    duration = time_2 - time_1
    return duration


def validate_questions(values, dates, start_date, end_date, question):
    all_data_json = {}
    if dates[0] >= dates[1] and dates[2] <= dates[3]:
            all_data_json["date"] = start_date[0]
            if question == 'Number of Participants':
                all_data_json["participants"] = values.get("Total Number of Participants")
            if question == 'Meeting Duration':
                duration = calculate_hours(start_date, end_date)
                all_data_json["meeting_duration"] = duration.total_seconds() 
    return all_data_json


def generate_json(data, arguments, question):
    data_json = {}
    data_json["meeting_title"] = data[0].get("Meeting Title")
    data_json["data"] = {}
    contador = 0
    print(question)
    for key, values in data.items():
        start_date = values.get("Meeting Start Time").split("-")
        end_date = values.get("Meeting End Time").split("-")
        dates = calculate_date(start_date, end_date, arguments)
        all_data_json = validate_questions(values, dates, start_date, end_date, question)            
        data_json["data"][contador] = all_data_json
        contador = contador + 1
    final_data = json.dumps(data_json, indent=4, separators=(',', ': '), sort_keys=True)
    print(final_data)



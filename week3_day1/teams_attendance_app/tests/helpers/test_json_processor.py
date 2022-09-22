from src.helpers.json_processor import calculate_date, calculate_hours

def calculate_dates():
    name= "General"
    args = {
        "name": "General",
        "start_date": "9/10/2022",
        "end_date": "9/29/2022"
    }
    expected_result = '2022-09-16 2022-09-16 2022-09-10 2022-09-29'
    start_date = ['9/16/2022 ', ' 5:58:05 PM']
    end_date = ['9/16/2022 ', ' 8:09:20 PM']
    result = calculate_date(start_date, end_date, args)
    message = 'expected result {expected_result}'
    assert expected_result == result, message

def calculate_durations():
    name= "General"
    args = {
        "name": "General",
        "start_date": "9/10/2022",
        "end_date": "9/29/2022"
    }
    expected_result = '2:11:15'
    start_date = ['9/16/2022 ', ' 5:58:05 PM']
    end_date = ['9/16/2022 ', ' 8:09:20 PM']
    result = calculate_hours(start_date, end_date)
    message = 'expected result {expected_result}'
    assert expected_result in result, message
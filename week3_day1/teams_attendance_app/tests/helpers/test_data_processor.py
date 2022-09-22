from src.helpers.data_processor import get_file_path

def file_path_returns_paths():
    name= "General"
    args = {
        "name": "General",
        "start_date": "9/10/2022",
        "end_date": "9/29/2022"
    }
    expected_result = '"../attendace_reports/09162022/meetingAttendanceReport(General) (1).csv"'
    result = get_file_path(args)
    message = 'expected all routes containing the name = {name}'
    assert expected_result in result, message

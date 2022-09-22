from src.helpers.csv_processor import data_true

def file_to_json_returns_data():
    path = '../attendace_reports/09162022/meetingAttendanceReport(General) (1).csv'
    result = data_true(path)
    assert result, "expected True for path={path}"

def file_to_json_returns_data_empty():
    path = '../attendace_reports/09162022/meetingAttendanceReport(General) (1).csv'
    result = data_true(path)
    assert result, "expected False for path={path}"


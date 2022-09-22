## app entry point
from helpers import data_processor, csv_processor, json_processor

def process_questions():
    ## display questions menu
    print("Welcome, below you can see the possible questions that can be selected")
    print("1. What is the number of Partipants attending General Meeting per date, date filter between 9/12/2022 and 9/16/2022?")
    print("2. What is the Meeting duration of General Meeting per date, date filter between between 9/12/2022 and 9/16/2022?")
    print("Please enter the number for the question you want to ")
    question = input()
    if question != 1 or 2:
        print("You must enter a valid option")
    ## drive "question" selection while not Quit
    selected_question = ''
    if question == '1':
        selected_question = 'Number of Participants'
    if question == '2':
        selected_question = 'Meeting Duration'
    #selected_question = None # TODO define if string or number or dictionary
    return selected_question

def process_question_options(question):
    ## display input to request meeting name, end and start date
    print("Please enter the name of the meeting you want to request")
    meeting_name = input()
    print("Please enter the start date of the meeting you want to request")
    start_date = input()
    print("Please enter the end date of the meeting you want to request")
    end_date = input()
    ## drive "input" aquisition while not Quit
    arguments = {}
    arguments["name"] = meeting_name
    arguments["start_date"] = start_date
    arguments["end_date"] = end_date
    ##arguments = None  # TODO define if string or number or dictionary or tuple
    return arguments

def main():
    print("Teams Attendance App")
    question  = process_questions()
    arguments =  process_question_options(question)
    ## TODO: implement bussiness logic
    files_with_name = data_processor.get_file_path(arguments)
    data = csv_processor.file_to_json(files_with_name)
    json_processor.generate_json(data, arguments, question)
    pass


main()
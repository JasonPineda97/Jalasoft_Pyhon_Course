"""
1. Read CSV files and returns in-memory object
"""
import csv
import re
def file_to_json(paths):
    data = {}
    first_counter = 0
    for path in paths:
        with open(path, 'r') as file_csv:
            data_dict = {}
            lector = csv.reader(x.replace('\0', '') for x in file_csv)
            counter = 0
            for fila in lector:
                if counter<5:
                    separate = re.split(r'\t+', fila[0])
                    if len(separate) >1:
                        data_dict[separate[0]] = separate[1]
                        if len(fila) >1:
                            data_dict[separate[0]] = separate[1]+" -"+fila[1]
                    counter = counter + 1
            data[first_counter] = data_dict
            first_counter = first_counter + 1
    return data

def data_true(paths):
    json = file_to_json(paths)
    result = False
    if not json:
        result = True
    return result
"""
1. Read CSV files and returns in-memory object
"""
import csv
import re
def file_to_json(paths):
    data = {}
    primer_contador = 0
    for path in paths:
        with open(path, 'r') as file_csv:
            data_dict = {}
            lector = csv.reader(x.replace('\0', '') for x in file_csv)
            contador = 0
            for fila in lector:
                if contador<5:
                    separate = re.split(r'\t+', fila[0])
                    if len(separate) >1:
                        data_dict[separate[0]] = separate[1]
                        if len(fila) >1:
                            data_dict[separate[0]] = separate[1]+" -"+fila[1]
                    contador = contador + 1
            data[primer_contador] = data_dict
            primer_contador = primer_contador + 1
    return data

def data_true(paths):
    json = file_to_json(paths)
    result = False
    if not json:
        result = True
    return result
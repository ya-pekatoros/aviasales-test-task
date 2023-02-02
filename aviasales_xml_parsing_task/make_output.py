import os
import json

from aviasales_xml_parsing_task.find_difference import find_data_differences
from aviasales_xml_parsing_task.parser import build_data


def generate_diff(file_name_1, file_name_2, files_dir_path):

    data1 = build_data(file_name_1, files_dir_path)
    data2 = build_data(file_name_2, files_dir_path)

    differences = find_data_differences(data1, data2)

    differences = json.dumps(differences, indent=4)

    current_dir = os.getcwd()
    filename = "differencies_in_requests.json"

    with open(f'{current_dir}/{files_dir_path}/{filename}', "w") as output_file:
        output_file.write(differences)
        print(f"The result of gendiff in located here: {current_dir + files_dir_path + filename}")

    return

import json
import os
from aviasales_xml_parsing_task.make_output import generate_diff
from aviasales_xml_parsing_task import find_data_differences
from aviasales_xml_parsing_task import build_data
from aviasales_xml_parsing_task.scripts.flights_parser import parse_args
from tests.fixtures import expected

FIXTURES_PATH = '/tests/fixtures/'


def get_data(file_path):
    data = json.load(open(file_path))
    return data


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_build_data():
    assert build_data('data_sample_1.xml', FIXTURES_PATH) == expected.PARSING_RESULT_1
    assert build_data('data_sample_2.xml', FIXTURES_PATH) == expected.PARSING_RESULT_2


def test_find_data_differences():
    data1 = build_data('data_sample_1.xml', FIXTURES_PATH)
    data2 = build_data('data_sample_2.xml', FIXTURES_PATH)
    difference = find_data_differences(data1, data2)
    assert difference == expected.COMPARISON_RESULT


def test_generate_diff():
    generate_diff('data_sample_1.xml', 'data_sample_2.xml', FIXTURES_PATH)
    current_dir = os.getcwd()
    file_path = current_dir + FIXTURES_PATH + "differencies_in_requests.json"
    data_from_output_file = get_data(file_path)
    data1 = build_data('data_sample_1.xml', FIXTURES_PATH)
    data2 = build_data('data_sample_2.xml', FIXTURES_PATH)
    difference = find_data_differences(data1, data2)
    assert data_from_output_file == difference
    os.remove(file_path)


def test_parser():
    file_1 = 'data_sample_1.xml'
    file_2 = 'data_sample_2.xml'
    flight_parser = parse_args(request=[file_1, file_2, FIXTURES_PATH])
    assert flight_parser.first_file == file_1
    assert flight_parser.second_file == file_2

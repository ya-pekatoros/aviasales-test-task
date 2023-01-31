#  import os
#  from aviasales_xml_parsing_task import make_output
from aviasales_xml_parsing_task import find_data_differences
from aviasales_xml_parsing_task import build_data
import json
# from aviasales_xml_parsing_task.scripts.flights_parser import   # parse_args
from tests.fixtures import expected

FIXTURES_PATH = '/tests/fixtures/'


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
    print(json.dumps(difference, indent=4))
    assert difference == expected.COMPARISON_RESULT


# def test_parser():
#     path1 = os.getcwd() + '/' + 'tests/fixtures/file1.yml'
#     path2 = os.getcwd() + '/' + 'tests/fixtures/file2.yml'
#     parser = parse_args(request=['-fplain', path1, path2])
#     assert parser.first_file == path1
#     assert parser.second_file == path2
#     assert parser.format == 'plain'


#   assert generate_diff(get_fixture_path('nested_file1.yaml'),
# get_fixture_path('nested_file2.yaml'), 'json') == CONS_OUT_EXPECT[3]

# def test_main_ouput_json():
#     data1 = get_data(get_fixture_path('nested_file1.json'))
#     data2 = get_data(get_fixture_path('nested_file2.json'))
#     differences = find_data_differences(data1, data2)
#     output_path = os.getcwd()+'/gendiff_output.json'
#     form_output(request=['-fjson', get_fixture_path('nested_file1.json'), get_fixture_path('nested_file2.json')])
#     data_from_output_file = get_data(output_path)
#     assert data_from_output_file == differences
#     os.remove(output_path)

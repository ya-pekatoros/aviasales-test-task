from aviasales_xml_parsing_task.parser import build_data
from tests.fixtures import expected


def test_build_data():
    assert build_data('data_sample_1.xml', file_dir_path='/tests/fixtures/') == expected.data_1

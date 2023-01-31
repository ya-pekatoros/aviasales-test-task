#! /usr/bin/env python3
import argparse
import sys
from aviasales_xml_parsing_task import generate_diff


def parse_args(request):

    parser = argparse.ArgumentParser(description="Compares two XML files with flights and generate differences")

    parser.add_argument(
        "first_file",
        type=str
    )
    parser.add_argument(
        "second_file",
        type=str
    )
    parser.add_argument(
        "dir_relative_path",
        type=str
    )

    args = parser.parse_args(request)
    return args


def main():
    parser = parse_args(sys.argv[1:])
    diff = generate_diff(parser.first_file, parser.second_file, parser.dir_relative_path)
    return diff


if __name__ == '__main__':
    main()

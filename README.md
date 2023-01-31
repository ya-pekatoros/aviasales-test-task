
[![Maintainability](https://api.codeclimate.com/v1/badges/6caea2c9b61148e0c866/maintainability)](https://codeclimate.com/github/ya-pekatoros/aviasales-test-task/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/6caea2c9b61148e0c866/test_coverage)](https://codeclimate.com/github/ya-pekatoros/aviasales-test-task/test_coverage)

# Description

Hello!

This package contains the result of an archive test task for a Python developer position at https://aviasales.com.

The Text of the Original Task
There are two XML files, the results of requests to the API of our partner, via.com.

The task is to parse these files and present a list of differences (in JSON format) between the results of the two requests by the tag Flights. The differences should include:

Which flights make up a trip
The start and end time of a trip
The price of a trip
Differences in trip conditions
Any new trips
The language of implementation for the task is Python 3. You may use any libraries and tools."


# Requirenments

* Linux OS
* python = "^3.10"
* bs4 = "^0.0.1"
* lxml = "^4.9.2"

# Installation

### You can use pip and install package from git:

    pip install --user git+https://github.com/ya-pekatoros/aviasales-test-task

### Or you can clone rep and use poetry (python package management tool). Some shortcats to do it:

    git clone https://github.com/ya-pekatoros/aviasales-test-task.git
    cd aviasales-test-task
    make install
    make build
    package-install

# Commands and demonstrations

gendiff file-1-path file-2-path
    gendiff --h

The format of output is JSON file. Below you can find some demonstations of how it looks like.

### Demonstration of works:

[![Maintainability](https://api.codeclimate.com/v1/badges/6caea2c9b61148e0c866/maintainability)](https://codeclimate.com/github/ya-pekatoros/aviasales-test-task/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/6caea2c9b61148e0c866/test_coverage)](https://codeclimate.com/github/ya-pekatoros/aviasales-test-task/test_coverage)

# Description

Hello!

This package contains the result of an archive test task for a Python developer position at https://aviasales.com.

The Text of the Original Task
There are two XML files, the results of requests to the API of our partner, via.com.

The task is to parse these files and present a list of differences (in JSON format) between the results of the two requests by the tag Flights. 

The differences should include:
* which flights make up a trip
* the start and end time of a trip
* the price of a trip
* differences in trip conditions
* any new trips

The language of implementation for the task is Python 3. You may use any libraries and tools."

# Assumtions

We assume what all input XML files consists of all needed tags with correct formated data. In otherway we will see it in sonsole output. We do not implement any logic of data checks inside parser, though if we will need it can be implemented.

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

flights_parser file-1-full-name file-2-full-name relative-path-to-dir
    flights_parser --h

The format of input data is XML. Relative-path-to-dit looks like "/your_folder/your_subfolder/"

The format of output is JSON file. Below you can find some demonstations of how it looks like.

In output you will see all information about flights which has differencies between two files.
First you'll see flights with changed parameters like time of departure/arrival or conditions of flight. Second you'll see new flights iptions and after options which currently unavailable.

### Demonstration of works:

The input data and the result you can see in data_folder in these repo.

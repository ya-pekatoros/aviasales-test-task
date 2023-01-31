PARSING_RESULT_1 = {
    "AI-996;AI-332": {
        "single-adult-total-price": 546.80,
        "two-way ticket": True,
        "AI-996": {
            "carrier": "AirIndia",
            "carrier_id": "AI",
            "flight_number": "996",
            "source": "DXB",
            "destination": "DEL",
            "departure_time_stamp": '2018-10-22T0005',
            "arrival_time_stamp": '2018-10-22T0445',
            "class": "G",
            "number_of_stops": 0,
            "warning": None,
            "ticket_type": "E",
        },
        "AI-332": {
            "carrier": "AirIndia",
            "carrier_id": "AI",
            "flight_number": "332",
            "source": "DEL",
            "destination": "BKK",
            "departure_time_stamp": '2018-10-22T1350',
            "arrival_time_stamp": '2018-10-22T1935',
            "class": "G",
            "number_of_stops": 0,
            "warning": None,
            "ticket_type": "E",
        },
    },
    "MH-163;MH-5860": {
        "single-adult-total-price": 623.80,
        "two-way ticket": True,
        "MH-163": {
            "carrier": "Malaysia Airlines",
            "carrier_id": "MH",
            "flight_number": "163",
            "source": "DXB",
            "destination": "KUL",
            "departure_time_stamp": '2018-10-22T1935',
            "arrival_time_stamp": '2018-10-23T0705',
            "class": "N",
            "number_of_stops": 0,
            "warning": None,
            "ticket_type": "E",
        },
        "MH-5860": {
            "carrier": "Malaysia Airlines",
            "carrier_id": "MH",
            "flight_number": "5860",
            "source": "KUL",
            "destination": "BKK",
            "departure_time_stamp": '2018-10-23T1320',
            "arrival_time_stamp": '2018-10-23T1430',
            "class": "L",
            "number_of_stops": 0,
            "warning": None,
            "ticket_type": "E",
        },
    },
}

PARSING_RESULT_2 = {
    "AI-996;AI-332": {
        "single-adult-total-price": 382.70,
        "two-way ticket": False,
        "AI-996": {
            "carrier": "AirIndia",
            "carrier_id": "AI",
            "flight_number": "996",
            "source": "DXB",
            "destination": "DEL",
            "departure_time_stamp": '2018-10-27T0005',
            "arrival_time_stamp": '2018-10-27T0445',
            "class": "G",
            "number_of_stops": 0,
            "warning": None,
            "ticket_type": "E",
        },
        "AI-332": {
            "carrier": "AirIndia",
            "carrier_id": "AI",
            "flight_number": "332",
            "source": "DEL",
            "destination": "BKK",
            "departure_time_stamp": '2018-10-27T1325',
            "arrival_time_stamp": '2018-10-27T1920',
            "class": "G",
            "number_of_stops": 0,
            "warning": None,
            "ticket_type": "E",
        },
    },
    "CZ-384;CZ-3035": {
        "single-adult-total-price": 385.40,
        "two-way ticket": False,
        "CZ-384": {
            "carrier": "China Southern Airlines",
            "carrier_id": "CZ",
            "flight_number": "384",
            "source": "DXB",
            "destination": "CAN",
            "departure_time_stamp": '2018-10-27T0140',
            "arrival_time_stamp": '2018-10-27T1225',
            "class": "T",
            "number_of_stops": 0,
            "warning": None,
            "ticket_type": "E",
        },
        "CZ-3035": {
            "carrier": "China Southern Airlines",
            "carrier_id": "CZ",
            "flight_number": "3035",
            "source": "CAN",
            "destination": "BKK",
            "departure_time_stamp": '2018-10-27T1450',
            "arrival_time_stamp": '2018-10-27T1710',
            "class": "Y",
            "number_of_stops": 0,
            "warning": None,
            "ticket_type": "E",
        },
    },
}

COMPARISON_RESULT = {
    "AI-996;AI-332": {
        "added single-adult-total-price": 382.70,
        "deleted single-adult-total-price": 546.80,
        "added two-way ticket": False,
        "deleted two-way ticket": True,
        "AI-996": {
            "deleted departure_time_stamp": '2018-10-22T0005',
            "added departure_time_stamp": '2018-10-27T0005',
            "Attention! The time of departure was change by": "5 days, 0 hours, 0 minutes",
            "deleted arrival_time_stamp": '2018-10-22T0445',
            "added arrival_time_stamp": '2018-10-27T0445',
            "Attention! The time of arrival was change by": "5 days, 0 hours, 0 minutes"
        },
        "AI-332": {
            "deleted departure_time_stamp": '2018-10-22T1350',
            "added departure_time_stamp": '2018-10-27T1325',
            "Attention! The time of departure was change by": "4 days, 23 hours, 35 minutes",
            "deleted arrival_time_stamp": '2018-10-22T1935',
            "added arrival_time_stamp": '2018-10-27T1920',
            "Attention! The time of arrival was change by": "4 days, 23 hours, 45 minutes"
        },
    },
    "added CZ-384;CZ-3035": {
        "single-adult-total-price": 385.40,
        "two-way ticket": False,
        "CZ-384": {
            "carrier": "China Southern Airlines",
            "carrier_id": "CZ",
            "flight_number": "384",
            "source": "DXB",
            "destination": "CAN",
            "departure_time_stamp": '2018-10-27T0140',
            "arrival_time_stamp": '2018-10-27T1225',
            "class": "T",
            "number_of_stops": 0,
            "warning": None,
            "ticket_type": "E",
        },
        "CZ-3035": {
            "carrier": "China Southern Airlines",
            "carrier_id": "CZ",
            "flight_number": "3035",
            "source": "CAN",
            "destination": "BKK",
            "departure_time_stamp": '2018-10-27T1450',
            "arrival_time_stamp": '2018-10-27T1710',
            "class": "Y",
            "number_of_stops": 0,
            "warning": None,
            "ticket_type": "E",
        },
    },
    "deleted MH-163;MH-5860": {
        "single-adult-total-price": 623.80,
        "two-way ticket": True,
        "MH-163": {
            "carrier": "Malaysia Airlines",
            "carrier_id": "MH",
            "flight_number": "163",
            "source": "DXB",
            "destination": "KUL",
            "departure_time_stamp": '2018-10-22T1935',
            "arrival_time_stamp": '2018-10-23T0705',
            "class": "N",
            "number_of_stops": 0,
            "warning": None,
            "ticket_type": "E",
        },
        "MH-5860": {
            "carrier": "Malaysia Airlines",
            "carrier_id": "MH",
            "flight_number": "5860",
            "source": "KUL",
            "destination": "BKK",
            "departure_time_stamp": '2018-10-23T1320',
            "arrival_time_stamp": '2018-10-23T1430',
            "class": "L",
            "number_of_stops": 0,
            "warning": None,
            "ticket_type": "E",
        },
    },
}

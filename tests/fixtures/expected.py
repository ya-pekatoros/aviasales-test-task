from time import strptime


data_1 = {
    "AI-996;AI-332": {
        "single-adult-total-price": 546.80,
        "two-way ticket": True,
        "AI-996": {
            "carrier": "AirIndia",
            "carrier_id": "AI",
            "flight_number": "996",
            "source": "DXB",
            "destination": "DEL",
            "departure_time_stamp": strptime('2018-10-22T0005', '%Y-%m-%dT%H%M'),
            "arrival_time_stamp": strptime('2018-10-22T0445', '%Y-%m-%dT%H%M'),
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
            "departure_time_stamp": strptime('2018-10-22T1350', '%Y-%m-%dT%H%M'),
            "arrival_time_stamp": strptime('2018-10-22T1935', '%Y-%m-%dT%H%M'),
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
            "departure_time_stamp": strptime('2018-10-22T1935', '%Y-%m-%dT%H%M'),
            "arrival_time_stamp": strptime('2018-10-23T0705', '%Y-%m-%dT%H%M'),
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
            "departure_time_stamp": strptime('2018-10-23T1320', '%Y-%m-%dT%H%M'),
            "arrival_time_stamp": strptime('2018-10-23T1430', '%Y-%m-%dT%H%M'),
            "class": "L",
            "number_of_stops": 0,
            "warning": None,
            "ticket_type": "E",
        },
    },
}
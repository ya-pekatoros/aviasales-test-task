from bs4 import BeautifulSoup
import os
from time import strptime


def build_data(file_name, file_dir_path='/aviasales_xml_parsing_task/data_folder/'):

    current_dir = os.getcwd()
    file_path = current_dir + file_dir_path + file_name

    result_data = {}
    # result of parsing will be stored in dictionary for easy access, manipulate and convert in JSON

    with open(file_path) as file:
        soup = BeautifulSoup(file, "lxml-xml")

    data = soup.find("PricedItineraries")
    ''' all needed data stored inside this tag, also there are the the same tag <Flights> on different
    layers of XML, to extract different flights correct we need to get first the parent <Flight> tag,
    so we should not make recursive response and what's why we need to go down on the level, where needed
    tags are places '''

    for i, option in enumerate(data.find_all("Flights", recursive=False)):  # we get all flight options here
        option_id_data = []
        result_data[i] = {}

        ''' we store all flights options as a dicts, also, we need uniq id for all options the one of the ways
        to day it - to present option as combination of flight numbers like "AI-330;AI-331" for Air India
        flight number 330 and 331 but first we should use temporary id "i" to fill our dicts with data
        and after we get all flights we will replace "i" for combinations of flights numbers'''

        result_data[i]["single-adult-total-price"] = float(option.find(ChargeType="TotalAmount").string)
        result_data[i]["two-way ticket"] = True if option.find("ReturnPricedItinerary") else False
        onward_flights = option.find("OnwardPricedItinerary").find("Flights")

        ''' there are only onward flighs in the second data file in this test case, so we don't need
        return flights'''

        for flight in onward_flights.find_all("Flight"):

            carrier = flight.find("Carrier").string
            carrier_id = flight.find("Carrier").get("id")
            flight_number = flight.find("FlightNumber").string
            flight_id = f'{carrier_id}-{flight_number}'
            option_id_data.append(flight_id)  # the part of building uniq flight option id

            result_data[i][flight_id] = {}  # we store all flight data also in dictionary
            result_data[i][flight_id]["carrier"] = carrier
            result_data[i][flight_id]["carrier_id"] = carrier_id
            result_data[i][flight_id]["flight_number"] = flight_number
            result_data[i][flight_id]["source"] = flight.find("Source").string
            result_data[i][flight_id]["destination"] = flight.find("Destination").string

            result_data[i][flight_id]["departure_time_stamp"] = strptime(
                flight.find("DepartureTimeStamp").string, '%Y-%m-%dT%H%M'
            )

            result_data[i][flight_id]["arrival_time_stamp"] = strptime(
                flight.find("ArrivalTimeStamp").string, '%Y-%m-%dT%H%M'
            )

            result_data[i][flight_id]["class"] = flight.find("Class").string
            result_data[i][flight_id]["number_of_stops"] = int(flight.find("NumberOfStops").string)
            result_data[i][flight_id]["warning"] = flight.find("WarningText").string
            result_data[i][flight_id]["ticket_type"] = flight.find("TicketType").string

        option_id = ';'.join(option_id_data)  # finally we get unique id for all each flight option
        result_data[option_id] = result_data[i]  # and after we replace temporary id
        del result_data[i]

    return result_data

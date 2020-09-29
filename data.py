from random import random
data = (
    ("", "prop", "address", "area", "rent", "serv_charge", 'tenant', 'landlord', 'period', 'status', False, 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet', "Missing Flat title"),
    ("name", "", "address", "area", "rent", "serv_charge", 'tenant', 'landlord', 'period', 'status', False, 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet','Missing Property'),
    ("name", "prop", "", "area", "rent", "serv_charge", 'tenant', 'landlord', 'period', 'status', False, 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet', 'Missing Address'),
    ("name", "prop", "address", "", "rent", "serv_charge", 'tenant', 'landlord', 'period', 'status', False, 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet', 'Missing Area'),
    ("name", "prop", "address", "area", "", "serv_charge", 'tenant', 'landlord', 'period', 'status', False, 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet', 'Missing Flat rent'),
    ("name", "prop", "address", "area", "rent", "", 'tenant', 'landlord', 'period', 'status', False, 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet', 'Missing service charge'),
    ("name", "prop", "address", "area", "rent", "serv_charge", '', 'landlord', 'period', 'status', False, 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet', 'Missing Flat tenant'),
    ("name", "prop", "address", "area", "rent", "serv_charge", 'tenant', '', 'period', 'status', True, 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet', 'Missing Flat landlord'),
    ("name", "prop", "address", "area", "rent", "serv_charge", 'tenant', 'landlord', '', 'status', True, 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet', 'Missing tenancy period'),
    ("name", "prop", "address", "area", "rent", "serv_charge", 'tenant', 'landlord', 'period', '', True, 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet', 'Missing Flat status'),
    ("name", "prop", "address", "area", "rent", "serv_charge", 'tenant', 'landlord', 'period', 'status', '', 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet', 'Missing Furnished'),
    ("name", "prop", "address", "area", "rent", "serv_charge", 'tenant', 'landlord', 'period', 'status', True, '', 'noOfBath', 'noOfPark', 'noOfToilet', 'Missing No. of Bathrooms'),
    ("name", "prop", "address", "area", "rent", "serv_charge", 'tenant', 'landlord', 'period', 'status', True, 'noOfBed', '', 'noOfPark', 'noOfToilet', 'Missing number of bedroom'),
    ("name", "prop", "address", "area", "rent", "serv_charge", 'tenant', 'landlord', 'period', 'status', True, 'noOfBed', 'noOfBath', '', 'noOfToilet', 'Missing number of park'),
    ("name", "prop", "address", "area", "rent", "serv_charge", 'tenant', 'landlord', 'period', 'status', True, 'noOfBed', 'noOfBath', 'noOfPark', '', 'Missing number of toilet'),
)


def get_params():
    start = int(random()*10) % 6

    return data[start:start+6]
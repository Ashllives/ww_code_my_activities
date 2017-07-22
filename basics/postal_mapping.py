postal_mapping = {
    'binondo': 1006,
    'intramuros': 1002,
    'malate': 1004,
    'ermita': 1000,
    'paco': 1007,
    'inagi-shi': 13225,
    'hino-shi': 13212
}

area = input('Hello! What is your area?').lower()

if area in postal_mapping:
    print('Hi! Your postal area is {}.'.format(postal_mapping[area]))
else:
    print('Sorry! The area you provided was not found on our records.')
import csv
import time

from techtest.models.data import Data
from techtest.errors.not_implemented import FileFormatNotImplementedError, \
    DataTypeNotImplementedError


def load_data_from_csv(filename):
    if not filename.endswith('.csv'):
        raise FileFormatNotImplementedError(filename)
    data = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def store_data_to_db(data, data_type):
    grouped_data = {}
    now = time.strftime("%Y-%m-%d %H:%M:%S")

    if data_type == 'csv':
        for elem in data:
            if elem['name'] not in grouped_data.keys():
                grouped_data[elem['name']] = [float(elem['value'])]
            else:
                grouped_data[elem['name']].append(float(elem['value']))
    elif data_type == 'json':
        for count, elem in enumerate(data['name']):
            if elem not in grouped_data.keys():
                grouped_data[elem] = [float(data['value'][count])]
            else:
                grouped_data[elem].append(float(data['value'][count]))
    else:
        raise DataTypeNotImplementedError

    for name, values in grouped_data.items():
        average_value = sum(values) / len(values)
        Data.create(name=name, value=average_value, created_date=now)

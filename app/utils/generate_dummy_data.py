import pandas
from app.settings.settings import TEMP_ROOT
import uuid
import datetime
import time
import random
from string import ascii_letters


DIRECTORY = TEMP_ROOT / 'test_data'
DIRECTORY.mkdir(exist_ok=True)

FILES = 5

COLUMNS = {
    'col1': 'string',
    'col2': 'int',
    'col3': 'datetime',
}


def string_value():
    string = [
        random.choice(ascii_letters) for _ in range(random.randint(3, 255))]
    return ''.join(string)


def int_value():
    return random.randint(0, 9999999)


def date_value():
    d = random.randint(1, int(time.time()))
    return datetime.datetime.fromtimestamp(d).strftime('%Y-%m-%d %H:%M:%S')


def mock_value(data_type):
    data_type_maps = {
        'string': string_value,
        'int': int_value,
        'datetime': date_value,
    }
    return data_type_maps[data_type]()


for i in range(FILES):
    rows = random.randint(10, 100)
    columns = list(COLUMNS)
    data = [
        [mock_value(v) for v in COLUMNS.values()] for _ in range(rows)
    ]
    df = pandas.DataFrame(columns=columns, data=data)

    output_name = DIRECTORY / f'{uuid.uuid4()}.csv'
    df.to_csv(output_name, index=False)


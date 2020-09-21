import os


class DataConfig:
    YEAR = 2019
    API_TOKEN = os.environ.get('API_TOKEN', None)
    PATH = './data'
    FREQ = '1min'

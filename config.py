import configparser
import os

cf = configparser.ConfigParser()

filename = r'conf.ini'

if os.path.exists(filename) is False:
    open(filename, 'w').close()

cf.read(filename)


def init_config():
    secs = cf.sections()
    if 'data' not in secs:
        cf.add_section('data')
        cf.write(open(filename, 'w+'))


init_config()


def load_data():
    _config = {}
    for item in cf.items('data'):
        key, value = item
        _config[key] = value
    return _config


CONFIG = load_data()


def write(item: dict):
    for k, v in item.items():
        CONFIG[k] = v
        cf.set('data', k, v)
    cf.write(open(filename, 'w+'))




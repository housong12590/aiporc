import configparser
import os


class DataConfig(object):

    def __init__(self, path='conf.ini', section='CONFIG'):
        self.conf = configparser.ConfigParser()
        self.path = path
        self.section = section
        self.__check_file()
        self.conf.read(path)

    def __check_file(self):
        if os.path.exists(self.path) is False:
            open(self.path, 'w').close()

    def save(self):
        self.conf.write(open(self.path, 'w+'))

    def put(self, key, value):
        if self.conf.has_section(self.section) is False:
            self.conf.add_section(self.section)
        self.conf.set(self.section, key, value)
        self.save()
        return self

    def get(self, key):
        if self.conf.has_section(self.section):
            if self.conf.has_option(self.section, key):
                return self.conf.get(self.section, key)
        return ''


conf = DataConfig()

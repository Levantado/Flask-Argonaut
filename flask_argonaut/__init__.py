import os
from argon2 import argon2_hash

"""
    A Flask extension providing Argon2 hashing and comparison hash.

    :copyright: (c) 2017 by Anton Oleynick.
    :license: BSD, see LICENSE for more details.
"""

__version__ = '0.21'


class Argonaut(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initializes the application with the extension.
        :param app: The Flask application object.
        """
        self.log_rounds = app.config.get('ARGON_LOG_ROUNDS', 12)

    @staticmethod
    def __checker(raw_data, type_check):
        """
        Checker input of salt on len of string, minimal len 8 chars, and check
        raw_data on empty state, for raising special error
        :param raw_data:
        :param type_check:
        :return:
        """
        if type_check == 'len':
            if len(str(raw_data)) < 8:
                raise ValueError('Too short Salt,'
                                 ' minimal length salt is 8 chars')
        if type_check == 'empty':
            if not raw_data:
                raise ValueError('Empty data import to hashing')

    @staticmethod
    def generate_salt():
        """
        Generation salt from urandom stream of system, default size of salt 20,
        :return: alphanumeric string of salt 20 char len
        """
        return os.urandom(10).hex()

    def generate_hash(self, data, salt=None, hashlen=None):
        """
        Generating hash with special size, if len not set size of hash 254
        Input data it's data, and hashing salt
        :param data: Data for hashing
        :param salt: Salt using for hashing
        :param hashlen: Length of generate hash
        :return:
        """
        self.__checker(data, 'empty')
        if not salt:
            salt = self.generate_salt()
        elif salt:
            self.__checker(salt, 'len')
            salt = str(salt)
        if not hashlen:
            hashlen = 127
        else:
            hashlen = hashlen // 2
        return argon2_hash(t=self.log_rounds,password=data,salt=salt, buflen=hashlen).hex(), salt

    def check_hash(self, hashed_data, data, salt):
        """
        Compare enter data with hashed_data, with using salt.
        :param hashed_data: Hashed data like blueprint for checking
        :param data: data what needed check
        :param salt: salt using for make that hash
        :return: True or False
        """
        temp_hash, _ = self.generate_hash(data, salt)
        return hashed_data == temp_hash

from argon2 import argon2_hash

"""
    flaskext.argonaut
    ---------------

    A Flask extension providing Argon2 hashing and comparison hash.

    :copyright: (c) 2017 by Anton Oleynick.
    :license: BSD, see LICENSE for more details.
"""

__version_info__ = ('0', '1', '4')
__version__ = '.'.join(__version_info__)
__author__ = 'Anton Oleynick'
__license__ = 'BSD'
__copyright__ = '(c) 2017 by Anton Oleynick'
__all__ = ['Argonaut', 'generate_salt', 'generate_hash', 'check_hash']


class Argonaut(object):
    def __init__(self, app=None):
        self.salt = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Initalizes the application with the extension.
        :param app: The Flask application object.
        """
        self.salt = app.config.get('ARGON_SALT')

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
                raise ValueError('Too short Salt, minimal length salt is 8 chars')
        if type_check == 'empty':
            if not raw_data:
                raise ValueError('Empty data import to hashing')

    @staticmethod
    def generate_salt():
        """
        Generation salt from urandom stream of system, default size of salt 20,
        :return: alphanumeric string of salt 20 char len
        """
        with open('/dev/urandom', 'rb') as f:
            return f.read(10).hex()

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
        if (not salt) and (not self.salt):
            salt = self.generate_salt()
        elif self.salt:
            self.__checker(self.salt, 'len')
            salt = str(self.salt)
        elif salt:
            self.__checker(salt, 'len')
            salt = str(salt)
        if not hashlen:
            hashlen = 127
        else:
            hashlen = hashlen // 2
        return argon2_hash(data, salt, buflen=hashlen).hex(), salt

    def check_hash(self, hashed_data, data, salt):
        """
        Compare enter data with hashed_data, with using salt.
        :param hashed_data: Hashed data like bluerprint for checking
        :param data: data what needed check
        :param salt: salt using for make that hash
        :return: True or False
        """
        h_d, _ = self.generate_hash(data, salt)
        if hashed_data == h_d:
            return True
        return False

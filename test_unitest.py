import unittest

from flask import Flask
from flask_argonaut import Argonaut


class TestArgoMethod(unittest.TestCase):
    def setUp(self):
        """
        init Argonaut
        set input salt, hashed data, data
        :return:
        """
        app = Flask(__name__)
        self.argo = Argonaut(app)
        self.data_for_hash = '87LE6jo32h1Cx7o5IqAUmS'

    def test_init(self):
        """
        Test initialize Argonaut
        :return:
        """
        self.assertIsInstance(self.argo, Argonaut)

    def test_get_salt(self):
        """
        Test generate alpha numeral salt
        :return:
        """
        salt = self.argo.generate_salt()
        self.assertTrue(salt.isalnum())

    def test_get_hash(self):
        """
        Test generate alpha numeral hash for data with usage input salt
        :return:
        """
        salt = self.argo.generate_salt()
        hash_data, salt_exit = self.argo.generate_hash(self.data_for_hash, salt)
        self.assertTrue(hash_data.isalnum())
        self.assertEqual(salt, salt_exit)

    def test_compare(self):
        """
        Test checking input hash, with input raw data, with usage input salt
        :return:
        """
        salt = self.argo.generate_salt()
        hash_data, salt_exit = self.argo.generate_hash(self.data_for_hash, salt)
        result = self.argo.check_hash(hash_data, self.data_for_hash, salt)
        self.assertTrue(isinstance(result, bool))
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()

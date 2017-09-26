import unittest

from flask_argonaut import Argonaut


class TestArgoMethod(unittest.TestCase):
    def setUp(self):
        """
        init Argonaut
        set input salt, hashed data, data
        :return:
        """
        self.argo = Argonaut()
        self.salt = '37532b73a29d649e010d'
        self.exit_hash = '42a9738c584c1d4040661d2b80ade701831edcd809b402e83fb0d4bf28d572398c9540a57cdda64d9efd38ee418dca60fa900334561acffc637fd08e6c493748f8aee1bb3e8e0df8d0076b01ff3d7c98a0027b95b64661e725cfb96137a518a7eff91d1ba7f1f3dad08ccef675476168453d18a939c87d8e2cbf21b22b2b73'
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
        hash_data, salt_exit = self.argo.generate_hash(self.data_for_hash, salt=self.salt)
        self.assertTrue(hash_data.isalnum())
        self.assertEqual(hash_data, self.exit_hash)
        self.assertEqual(self.salt, salt_exit)

    def test_compare(self):
        """
        Test checking input hash, with input raw data, with usage input salt
        :return:
        """
        result = self.argo.check_hash(self.exit_hash, self.data_for_hash, self.salt)
        self.assertTrue(isinstance(result, bool))
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()

import pytest
from flask_argonaut import Argonaut

salt = '37532b73a29d649e010d'
exit_hash = '42a9738c584c1d4040661d2b80ade701831edcd809b402e83fb0d4bf28d572398c9540a57cdda64d9efd38ee418dca60fa900334561acffc637fd08e6c493748f8aee1bb3e8e0df8d0076b01ff3d7c98a0027b95b64661e725cfb96137a518a7eff91d1ba7f1f3dad08ccef675476168453d18a939c87d8e2cbf21b22b2b73'
data_for_hash = '87LE6jo32h1Cx7o5IqAUmS'

def init_extension():
    return Argonaut()

def test_init():
    assert isinstance(init_extension(), Argonaut) == True

def test_get_salt():
    salt = init_extension().generate_salt()
    assert salt.isalnum() == True

def test_get_hash():
    hash_data, salt_exit = init_extension().generate_hash(data_for_hash, salt=salt)
    assert hash_data.isalnum() == True
    assert hash_data == exit_hash
    assert salt == salt_exit

def test_hash_len():
    hash_data, _ = init_extension().generate_hash(data_for_hash, hashlen=100)
    assert len(hash_data) == 100

def test_compare():
    result = init_extension().check_hash(exit_hash, data_for_hash, salt)
    assert isinstance(result, bool)
    assert result
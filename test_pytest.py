import pytest
from os import urandom
from flask_argonaut import Argonaut
from flask import Flask


data_for_hash = '87LE6jo32h1Cx7o5IqAUmS'


def init_extension():
    app = Flask(__name__)
    return Argonaut(app)

def test_init():
    assert isinstance(init_extension(), Argonaut) == True

def test_get_salt():
    salt = init_extension().generate_salt()
    assert salt.isalnum() == True

def test_get_hash():
    salt = urandom(10).hex()
    output_hash, salt_exit = init_extension().generate_hash(data_for_hash,
                                                            salt=salt)
    assert output_hash.isalnum() == True
    assert salt == salt_exit

def test_hash_len():
    hash_data, _ = init_extension().generate_hash(data_for_hash, hashlen=100)
    assert len(hash_data) == 100

def test_compare():
    salt = urandom(10).hex()
    output_hash, salt_exit = init_extension().generate_hash(data_for_hash,
                                                            salt)
    print(output_hash)
    result = init_extension().check_hash( output_hash, data_for_hash,salt)
    print(result)
    assert isinstance(result, bool)
    assert result
# Flask-Argonaut

Flask-Argonaut is a Flask extension that provides security hashing with hash [Argon2](https://github.com/P-H-C/phc-winner-argon2), the password-hashing function that won the Password Hashing Competition (PHC) 

Argon2 is a password-hashing function that summarizes the state of the art in the design of memory-hard functions and can be used to hash passwords for credential storage, key derivation, or other applications.

## Installation

Install the extension with one of the following commands:
    
    $ pip install flask-argonaut

## Usage

###Initialize
To use the extension simply import the class wrapper and pass the Flask app
object back to here. Do so like this:
    
    from flask import Flask
    from flask_argonaut import Argonaut
    
    app = Flask(__name__)
    argon = Argonaut(app)


if you use factory method
	
	argon = Argonaut()

	def create_app():
	    app = Flask(__name__)
        argon.init_app(app)

### Main functions
Extension have three primary function.

#### Generate salt

	salt = argon.generate_salt()

Return as results generated salt with, salt 20 chars of len.

#### Generate hash
	hashed_data, salt = argon.generate_hash(rawdata, salt, hashlen)

Return generated hash with specific len if len not set, automaticaly set 254. Same if salt not specificate salt generate too. Minimal len of salt is 8 symbols.

Salt may set in app with environment settings ARGON_SALT 

	app.config['ARGON_SALT'] = 'SOME123SECRET987SALT'

#### Checking hash

Compare hash proceed with function:

	argon.check_hash(hashed_data, data, salt)
	
Result of function is True or False.


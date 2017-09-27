"""
    Flask-Argonaut
    ------------
    Argon2 hashing for your Flask.

"""
from setuptools import setup
import re, io

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    io.open('flask_argonaut/__init__.py', encoding='utf_8_sig').read()
    ).group(1)

setup(name='Flask-Argonaut',
      version=__version__,
      description='Flask extension use hashing data with Argon2',
      author='Anton Oleynik',
      author_email='levantado@me.com',
      license='BSD',
      urls='https://github.com/Levantado/Flask-Argonaut',
      download_url = 'https://github.com/Levantado/Flask-Argonaut/tarball/master',
      packages=['flask_argonaut'],
      platforms='any',
      install_requires=['Flask', 'argon2'],
      classifiers=[
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.6',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      zip_safe=False,
      test_suite='test')

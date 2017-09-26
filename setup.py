"""
    Flask-Argonaut
    ------------
    Argon2 hashing for your Flask.

"""
from setuptools import setup

setup(name='Flask-Argonaut',
      version='0.14',
      description='Flask extension use hashing data with Argon2',
      author='Anton Oleynik',
      author_email='levantado@me.com',
      license='BSD',
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

'''
    setup.py
    Mike Overby, 4/17/2014
    Setup script for Mail Pilot game
'''

from distutils.core import setup

setup(
    name = 'MailPilot',
    version = '1.0',
    description = 'basic video game',
    author = 'Mike Overby',
    author_email = 'mikeoverby@outlook.com',
    url = 'lethargilistic.com',
    packages = ['MailPilot'],
    package_data = { 'MailPilot' : ['assets/*']}
    )

# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in sfinext/__init__.py
from sfinext import __version__ as version

setup(
	name='sfinext',
	version=version,
	description='Doctypes and website for employee portal for a home care company. Allows for documentation, mileage, reporting, and communication function in an online app',
	author='Shawn Murphy',
	author_email='shawnmurphy@sficare.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

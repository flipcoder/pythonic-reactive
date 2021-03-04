#!/usr/bin/python
from __future__ import unicode_literals
from setuptools import setup, find_packages
import sys

if sys.version_info[0] == 2:
    sys.exit("Requires python3!")
setup(
    name="pythonic_reactive",
    version="0.1.0",
    description="",
    url="https://github.com/filpcoder/python-reactive",
    author="Grady O'Connell",
    author_email="flipcoder@gmail.com",
    license="MIT",
    packages=["pythonic_reactive"],
    include_package_data=False,
    install_requires=[],
    zip_safe=True,
)

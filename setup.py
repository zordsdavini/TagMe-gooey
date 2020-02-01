# -*- coding: utf-8 -*-

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('TagMeGooey/gooey_ui.py').read(),
    re.M
    ).group(1)

setup(
    name="tagme-gooey",
    packages=["TagMeGooey"],
    entry_points={
        "console_scripts": ['tagme = TagMeGooey.gooey_ui:main']
        },
    dependency_links = ['http://github.com/zordsdavini/TagMe/tarball/master#egg=tagme-0.0.4'],
    install_requires=[
        'TagMe',
        'Gooey',
        ],
    version=version,
    description="Python Gooey application to set tags in filename based on TagMe lib.",
    long_description="TBD",
    author="Arns & Kristina Udovič",
    author_email="zordsdavini@gmail.com, kristina.udoviciene@gmail.com",
    url="https://github.com/zordsdavini/TagMe-gooey",
    )

#!/usr/bin/python
# -*- coding:utf-8 -*-

from setuptools import setup


setup(
    name='kucoin-futures-python',
    version='v1.0.0',
    packages=['kucoin', 'kucoin/base_request', 'kucoin/market', 'kucoin/trade', 'kucoin/user',
              'kucoin/websocket', 'kucoin/ws_token'],
    license="MIT",
    author='Arthur & Trevor',
    author_email="arthur.zhang@kucoin.com",
    url='https://github.com/TrevorTKern/kucoin-futures-python-sdk',
    description="kucoin-futures-api-sdk",
    install_requires=['requests', 'websockets'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

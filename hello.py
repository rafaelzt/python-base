#!/usr/bin/env python3

#DocString
""" Hello World Multi Language

Print Hello world in different languages depends on env var LANG

How to use:
You should have env var LANG setted

    export LANG=pt_BR

Execution:
    python3 hello.py
    or
    ./hello.py
"""
# Dunder
__version__ = "0.0.1"
__author__ = "Rafael Tanganelli"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, world!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg.upper()) # built-in
    

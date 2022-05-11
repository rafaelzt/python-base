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
__version__ = "0.1.2"
__author__ = "Rafael Tanganelli"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "pt_BR": "Olá mundo!",
    "en_US": "Hello World!",
    "es_SP": "Hola mundo!",
    "it_IT": "Ciao Mondo!",
    "fr_FR": "Bonjour Monde!"
}

print(msg[current_language].upper()) # built-in
    

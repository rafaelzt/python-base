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
import sys

print(f"{sys.argv=}")
arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = (arg.split('='))
    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

# current_language = os.getenv("LANG", "en_US")[:5]
current_language = arguments["lang"]

if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input(
            "Choose a language: \n"
        )

current_language = current_language[:5]

msg = {
    "pt_BR": "Olá mundo!",
    "en_US": "Hello World!",
    "es_ES": "Hola mundo!",
    "it_IT": "Ciao Mondo!",
    "fr_FR": "Bonjour Monde!"
}

print(
    msg[current_language] * int(arguments["count"])
) # built-in
    

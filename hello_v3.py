#!/usr/bin/env python3

#DocString
""" Hello World Multi Language

Print Hello world in different languages depends on env var LANG

How to use:
You should have env var LANG setted

    export LANG=pt_BR

Or pass as CLI argument `--lang`

Or type LANG in the input

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
    try:
        key, value = (arg.split('='))
    except ValueError as e:
        # TODO: Use logging
        print(f"[Err] {str(e)}")
        print(f"You have to use `=`")
        print(f"You passed {arg}")
        print("try to use --key=value")
        print()
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit(1)
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


# LBYL
# if current_language in msg:
#     message = msg[current_language]
# else:
#     print(f"Language is not valid, choose one from: \n{list(msg.keys())}")
#     sys.exit(2)

# EAFP 
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[Err] {str(e)}")
    print(f"Language is not valid, choose one from \n{list(msg.keys())}")
    sys.exit(2)

# message = msg.get(current_language, msg["en_US"])

print(
    message * int(arguments["count"])
) # built-in
    

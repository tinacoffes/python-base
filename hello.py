#!/usr/bin/env python3
"""Hello World Multi Línguas

Depending on the language configured in the environment, the program
displays the corresponding text.

How to use:

Have the LANG variable properly configured, e.g.:

export LANG=pt_BR

Execution:

python3 hello.py

or

./hello.py
"""

__version__= 0.0,1
__author__= "Ana Cristina"
__license__= "unlicense"

# meu primeiro hello world em python !!
print("hello world")
print('tina'.upper())
print(57 + 9)

import os


current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá Mundo!"
elif current_language == "es_ES":
    msg = "Hola Mundo!"
elif current_language == "ko_KR": 
    msg = "안녕하세요 세상!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!" 
    
print(msg)

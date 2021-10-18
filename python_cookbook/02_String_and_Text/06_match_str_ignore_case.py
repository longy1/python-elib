#!/usr/bin/ python3
# -*- coding: utf-8 -*-

'flags=re.IGNORECASE'

__author__ = 'Ethan Long'

import re

# naive replace with IGNORECASE
text = 'UPPER PYTHON, lower python, Mixed Python'
rtext = re.sub(r'python', r'java', text, flags=re.IGNORECASE)
print(rtext)

# using closure to dynamic replace
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

rtext = re.sub('python', matchcase('java'), text, flags=re.IGNORECASE)

print(rtext)
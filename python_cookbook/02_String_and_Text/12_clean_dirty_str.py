#!/usr/bin/python3
# -*- coding: utf-8 -*-

'use str.translate()'

__author__ = 'Ethan Long'

s = 'pýtĥöñ\fis\tawesome\r\n'

# use trans dict to translate unwanted str
clear_blank_map = {ord('\t'): ' ', ord('\f'): ' ', ord('\r'): None}

clean_s = s.translate(clear_blank_map)
print(clean_s)

# use unicodedata.normalize() to distinct combining char
import unicodedata, sys

clear_blank_map = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
clean_s = unicodedata.normalize('NFD', clean_s)
clean_s = clean_s.translate(clear_blank_map)
print(clean_s)
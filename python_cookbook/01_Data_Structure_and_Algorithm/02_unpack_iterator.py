#!/usr/bin/python3
# -*- coding: utf-8 -*-

# how to
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

name, *_, phone = record

print(type(_))
print(name, phone)

# error
record = ('Dave', '847-555-1212')
name, *_, phone, phone = record
#!/usr/bin/env python3
import re

def decode(string):
    matches = re.findall(r'(\d*)(\D)', string)
    print(''.join(int(count or 1)*char for count, char in matches))

def encode(string):
    pass

decode('2ab34c4bbca3a2c')

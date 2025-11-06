#!/usr/bin/env python3
import re

def decode(string):
    matches = re.findall(r'(\d*)(\D)', string)
    decoded_chars = [int(tup_char[0])*tup_char[1] if tup_char[0] else tup_char[1] for tup_char in matches]
    print(''.join(decoded_chars))

def encode(string):
    pass

decode('2ab34c4bbca3a2c')

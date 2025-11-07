#!/usr/bin/env python3
import re

def decode(string):
    matches = re.findall(r'(\d*)(\D)', string)
    print(''.join(int(count or 1)*char for count, char in matches))

def encode(string):
    char_list = []
    for match in re.finditer(r'(.)\1*', string): 
        full_run = match.group(0)
        
        if len(full_run) > 1:
            char_list.append(str(len(full_run)))
        char_list.append(match.group(1))
    print(''.join(char_list))

decode('2ab34c4bbca3a2c')
encode('qqbbbauuattebbbbbcvvv')

#!/usr/bin/env python3
import re

def regex(reg):
    list_letters = []
    for x in re.findall(r'[a-zA-Z]', reg):
        list_letters.append(x)
    print(''.join(list_letters))
    print(reg)

regex('q78782q*7729103bdge39trt4yr000''LAKSGHJFWFWXUHIAtdnnkjbdghjdb vjrb5%%^#@!ggdsshsva')

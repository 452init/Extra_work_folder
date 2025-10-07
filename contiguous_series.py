#!/usr/bin/env python3
def slices():
    series = 'abcdefghijklm'
    length = 5
    for cont1 in range(len(series) - length +1):
        yield series[cont1:cont1+length]
    
result_list = [i for i in slices()]
print(result_list)

def roman(number: int)-> str:
    number_str = str(number)
    number_list = list(number_str)
    roman_result: str = ''
    last_number = number_list[-1]

    roman_mapping = {'unit': {'1': "I", '2':"II", '3':"III" , '4':'IV' , '5':'V', '6':'VI', '7':'VII', '8':'VIII', '9':"IX"},
                         'tens': {'10':'X', '20':"XX", '30':"XXX", '40':'XL', '50':'L', '60':'LX', '70':'LXX', '80':'LXXX', '90':'XC'},
                         'hundreds': {'100':'C', '200':'CC', '300':'CCC', '400':'CD', '500':'D', '600':'DC', '700':'DCC', '800':'DCCC', '900':'CM'},
                         'thousands': {'1000':'M', '2000':'MM', '3000':'MMM'}}

    if len(number_str) == 1:
        return roman_mapping['unit'][last_number]
    elif len(number_str) == 2:
        if number_str in roman_mapping['tens']:
            return  roman_mapping['tens'][number_str]
        else:
            number_list[1] = '0'
            roman_result += roman_mapping['tens'][''.join(number_list)]
            if number_str[1] != 0:
                roman_result += roman_mapping['unit'][''.join(last_number[-1])]
    elif len(number_str) == 3:
        if number_str in roman_mapping['hundreds']:
            return  roman_mapping['hundreds'][number_str]
        else:
            number_list_2 = number_list[1:]
            number_list[1:] = '00'
            number_list_2[1] = '0'
            roman_result += roman_mapping['hundreds'][''.join(number_list)]
            if number_str[1] != '0':
                roman_result += roman_mapping['tens'][''.join(number_list_2)]
            roman_result += roman_mapping['unit'][''.join(last_number[-1])]
    else:
        if number_str in roman_mapping['thousands']:
            return  roman_mapping['thousands'][number_str]
        else:
            number_list_2 = number_list[1:]
            number_list_3 = number_list[2:]
            number_list[1:] = '000'
            number_list_2[1:] = '00'
            number_list_3[1] = '0'
            roman_result += roman_mapping['thousands'][''.join(number_list)]
            if number_str[1] != '0':
                roman_result += roman_mapping['hundreds'][''.join(number_list_2)]
            if number_str[2] != '0':
                roman_result += roman_mapping['tens'][''.join(number_list_3)]
            if number_str[-1] != '0':
                roman_result += roman_mapping['unit'][''.join(last_number[-1])]
    return roman_result
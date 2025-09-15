#!/usr/bin/env python3
#def decription_vigenere(cipher, key):
cipher = input('Enter Decrypted message: ')
key = input('Enter key: ')
'''decription of vignere cipher'''
alphabets = 'abcdefghijklmnopqrstuvwxyz'
result = []
key_index = 0
char_position = {x: pos for pos, x in enumerate(alphabets)}
if not key:
	print('{cipher}')
else:
	for char in cipher:
		if char.isalpha():
			#shift cipher letter by letter to plain text
			shift = alphabets.index(key[key_index % len(key)].lower())
			char_pos = char_position.get(char)
			plain_text = (char_pos - shift) % 26
			result.append(alphabets[plain_text])
			key_index += 1
		else:
			result.append(char)
	final_result = ''.join(result)

	print(f'Decrypted message is: {final_result}')

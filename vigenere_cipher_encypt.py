#!/usr/bin/env python3
#def vigenere_cipher(text, key):
"""Encrypt text using Vigenère cipher with given key."""
text_holder = input('Enter text to encript: ')
key = input('Enter the encription key ')

alphabets = 'abcdefghijklmnopqrstuvwxyz'
result = []
key_index = 0  # Track position in the key
char_position = {x: pos for pos, x in enumerate(alphabets)}
if not key:
	print(f'Sorry no encryption key!{text_holder}')
else:
	for char in text_holder.lower():
		if char.isalpha():
			# Step 1: Get shift amount from current key letter
			shift = alphabets.index(key[key_index % len(key)].lower())

			# Step 2: Find position of current character
			char_pos = char_position.get(char)

			# Step 3: Apply shift with wraparound
			new_pos = (char_pos + shift) % 26

			# Step 4: Append the new character
			result.append(alphabets[new_pos])

			# Step 5: Move to next key letter
			key_index += 1
		else:
			# Keep non-letters as-is (optional)
			result.append(char)
	final_result = ''.join(result)

	print(f'{final_result}')

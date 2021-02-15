#31


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""

word = input()
modified_word = ""

for char in word:
	if char.isupper():
		modified_word += char.lower()

	elif char.islower():
		modified_word += char.upper()

	else:
		modified_word += char

print(modified_word)
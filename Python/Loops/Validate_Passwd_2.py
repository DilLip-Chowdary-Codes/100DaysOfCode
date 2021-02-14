#29


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""

passwd = input()
contains_uppercase_letter = False

for char in passwd:
	if char.isupper():
		contains_uppercase_letter = True
		break

if contains_uppercase_letter:
	print("Valid Password")
else:
	print("Invalid Password")

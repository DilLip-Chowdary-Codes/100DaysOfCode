#30


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""

passwd = input()
is_password_valid = False

contains_uppercase_letter = False
contains_lowercase_letter = False
contains_digit = False

for char in passwd:
	if char.isupper():
		contains_uppercase_letter = True
		
	if char.islower():
		contains_lowercase_letter = True

	if char.isdigit():
		contains_digit = True

	is_password_valid = contains_digit and contains_lowercase_letter and contains_uppercase_letter

	if is_password_valid:
		break

if is_password_valid:
	print("Valid Password")
else:
	print("Invalid Password")

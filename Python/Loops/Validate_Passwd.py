#28


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""

passwd = input()
contains_digit = False

for char in passwd:
	if char.isdigit():
		contains_digit = True
		break

if contains_digit:
	print("Valid Password")
else:
	print("Invalid Password")

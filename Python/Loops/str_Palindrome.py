#45


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""

str = input()

str = str.lower()

rev_str = str[::-1]

is_palindrome = rev_str == str

if is_palindrome:
	print("Palindrome")
else:
	print("Not a Palindrome")

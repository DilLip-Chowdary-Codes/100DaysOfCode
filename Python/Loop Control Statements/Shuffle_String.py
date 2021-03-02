#55


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""


# Asked by FB, Microsoft

original_word = input()
length_of_word = len(original_word)
shuffled_word = ""

indexes = [int(input()) for n in range(length_of_word)]

for index in indexes:
	shuffled_word += original_word[index]

print(shuffled_word)
#52


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""

import math

n = input()

no_of_digits = len(n)

n_th_power_of_digits_of_n = [math.pow(int(digit), no_of_digits) for digit in n]

is_armstrong_num = sum(n_th_power_of_digits_of_n) == int(n)

if is_armstrong_num:
	print("Armstrong Number")
else:
	print("Not an Armstrong Number")

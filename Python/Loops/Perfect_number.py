#51


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""


n = int(input())

factors = [num for num in range(1, n) if n % num == 0]

is_perfect_num = sum(factors) == n

if is_perfect_num:
	print("Perfect Number")
else:
	print("Not a Perfect Number")

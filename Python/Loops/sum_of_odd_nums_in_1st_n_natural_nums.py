#35


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""

n = int(input())
sum_of_n_odd_nums = 0

for num in range(1, n + 1):
	is_odd = num % 2 != 0

	if is_odd:
		sum_of_n_odd_nums += num

print(sum_of_n_odd_nums)

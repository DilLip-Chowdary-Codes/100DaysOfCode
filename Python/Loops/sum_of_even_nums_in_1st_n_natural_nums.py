#34


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""

n = int(input())
sum_of_n_even_nums = 0

for num in range(1, n + 1):
	is_even = num % 2 == 0

	if is_even:
		sum_of_n_even_nums += num

print(sum_of_n_even_nums)

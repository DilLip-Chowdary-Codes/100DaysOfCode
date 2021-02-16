#36


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""

m = int(input())
n = int(input())
sum_of_n_even_nums = 0

for num in range(m, n + 1):
	is_even = num % 2 == 0

	if is_even:
		sum_of_n_even_nums += num

print(sum_of_n_even_nums)

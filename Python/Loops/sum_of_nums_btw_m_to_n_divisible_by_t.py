#38


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""

t = int(input())
m = int(input())
n = int(input())

sum_of_nums_from_m_to_n_divisible_by_t = 0

for num in range(m, n + 1):
	is_divisible_by_t = num % t == 0

	if is_divisible_by_t:
		sum_of_nums_from_m_to_n_divisible_by_t += num

print(sum_of_nums_from_m_to_n_divisible_by_t)

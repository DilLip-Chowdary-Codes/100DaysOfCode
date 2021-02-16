#37


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""

m = int(input())
n = int(input())
sum_of_n_odd_nums = 0

for num in range(m, n + 1):
	is_odd = num % 2 != 0

	if is_odd:
		sum_of_n_odd_nums += num

print(sum_of_n_odd_nums)

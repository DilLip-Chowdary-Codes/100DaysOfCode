#49


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""


n = int(input())

factors = [num for num in range(1, n + 1) if n % num == 0]

print(*factors, sep="\n")

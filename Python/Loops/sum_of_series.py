#48


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""



"""

Series Will be like this 2, 22, 222, 2222 , ....

"""

n = int(input())

series = [int(num * "2") for num in range(1, n + 1)]

print(sum(series))

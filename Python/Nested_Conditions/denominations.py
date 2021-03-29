#17


"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""

amount = int(input())
current_amount = amount
no_of_100_notes = current_amount // 100
current_amount -= no_of_100_notes * 100
no_of_50_notes = current_amount // 50
current_amount -= no_of_50_notes * 50
no_of_10_notes = current_amount // 10
current_amount -= no_of_10_notes * 10
no_of_1_notes = current_amount // 1
current_amount -= no_of_1_notes * 1

print(f"100:{no_of_100_notes}")
print(f"50:{no_of_50_notes}")
print(f"10:{no_of_10_notes}")
print(f"1:{no_of_1_notes}")

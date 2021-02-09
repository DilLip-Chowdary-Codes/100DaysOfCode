#2 

"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""
num = input()
is_special_num = (int(num[0]) + int(num[1])) == 7 or (num[0] == "7" or num[1] == "7") or int(num) % 7 ==0
if is_special_num:
    print("Special Number")
else:
    print("Normal Number")

#3
num = int(input())
is_spl_eleven = num % 11 == 0 or num % 11 == 1
if is_spl_eleven:
    print("Special Eleven")
else:
    print("Normal Number")

#7
num = input()
first_digit = int(num[0])
second_digit = int(num[1])
is_lucky_num = int(num) % 9 ==0 or (first_digit == 9 or second_digit == 9)
if is_lucky_num:
    print("Lucky Number")
else:
    print("Unlucky Number")

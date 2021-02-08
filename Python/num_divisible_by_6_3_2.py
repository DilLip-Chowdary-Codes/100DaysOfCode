#4
num = int(input())
if num % 6 == 0:
    print("Number is divisible by 6")
elif num % 3 == 0:
    print("Number is divisible by 3")
elif num % 2 == 0:
    print("Number is divisible by 2")
else:
    print("Number is not divisible by 2, 3 or 6")

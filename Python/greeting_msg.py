#12
time = int(input())
if time >= 4 and time < 12:
    print("Good Morning")
elif time >= 12 and time <16:
    print("Good Afternoon")
elif time >= 16 and time <20:
    print("Good Evening")
elif time >= 20 or time < 4:
    print("Good Night")

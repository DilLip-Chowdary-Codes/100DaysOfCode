#8
units = int(input())
if units <= 50:
    charge = 2 * units
elif units > 50 and units <= 150:
    charge = (2 * 50) + (units - 50) * 3
elif units > 150 and units <= 250:
    charge = (2 * 50) + (3 * 100) + (units - 150) * 5
elif units > 250:
    charge = (2 * 50) + (3 * 100) + (5 * 100) + (units - 250) * 8
surchage = (0.2 * charge)
total_bill = charge + surchage
print(total_bill)

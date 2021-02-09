#13

"""

__author__ = DilLip_Chowdary ❤️ Rayapati

"""

num_of_sides = int(input())
if num_of_sides < 3:
    print("Not Polygon")
elif num_of_sides == 3:
    print("Triangle")
elif num_of_sides == 4:
    print("Quadrilateral")
elif num_of_sides == 5 :
    print("Pentagon")
elif num_of_sides > 5:
    print("Big Polygon")
